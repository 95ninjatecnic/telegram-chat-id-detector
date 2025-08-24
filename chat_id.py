import asyncio
import json
import os
import re
from telethon import TelegramClient, events
from telethon.errors import UsernameInvalidError, UsernameNotOccupiedError

# ----------------------------
# Setup directories & state
# ----------------------------
os.makedirs("logs", exist_ok=True)
STATE_FILE = "state.json"

if os.path.exists(STATE_FILE):
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            state = json.load(f)
    except Exception as e:
        print(f"Warning: Failed to load state.json: {e}. Initializing empty state.")
        state = {}
else:
    state = {}

def save_state():
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Failed to save state.json: {e}")

# ----------------------------
# Load credentials
# ----------------------------
CREDENTIALS_FILE = "credentials.json"
if os.path.exists(CREDENTIALS_FILE):
    with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
        creds = json.load(f)
else:
    creds = {}
    creds['bot_token'] = input("Enter your Bot API Token: ").strip()
    creds['api_id'] = int(input("Enter your API ID (from my.telegram.org): ").strip())
    creds['api_hash'] = input("Enter your API Hash (from my.telegram.org): ").strip()
    creds['destination_chat'] = ""  # leave blank first
    with open(CREDENTIALS_FILE, "w", encoding="utf-8") as f:
        json.dump(creds, f, indent=4)

bot_token = creds['bot_token']
api_id = creds['api_id']
api_hash = creds['api_hash']

destination_chat = creds.get('destination_chat', "")
if destination_chat and destination_chat != "me":
    try:
        destination_chat = int(destination_chat)  # Force integer
    except:
        print("⚠️ Destination chat ID invalid, resetting.")
        destination_chat = ""

# ----------------------------
# Initialize Telegram Client
# ----------------------------
client = TelegramClient("bot_debug_session", api_id, api_hash)

# ----------------------------
# Helper: get chat info safely
# ----------------------------
async def get_chat_info(msg):
    chat_id = None
    chat_name = "Unknown"
    chat_type = "Private"
    sender_id = None

    if msg.sender:
        sender_id = getattr(msg.sender, "id", None)
        chat_name = getattr(msg.sender, "first_name", getattr(msg.sender, "username", "Unknown"))

    if msg.chat:
        chat_id = getattr(msg.chat, "id", None)
        if getattr(msg.chat, "broadcast", False):
            chat_type = "Channel"
        elif getattr(msg.chat, "megagroup", False) or getattr(msg.chat, "gigagroup", False):
            chat_type = "Group"
        else:
            chat_type = "Private"

    if msg.fwd_from:  # forwarded
        fwd = msg.fwd_from
        try:
            if getattr(fwd, "from_id", None):
                if hasattr(fwd.from_id, "channel_id"):
                    chat_id = fwd.from_id.channel_id
                    chat_type = "Channel"
                elif hasattr(fwd.from_id, "user_id"):
                    chat_id = fwd.from_id.user_id
                    chat_type = "Private"
            elif getattr(fwd, "channel_id", None):
                chat_id = fwd.channel_id
                chat_type = "Channel"
        except:
            pass

    return chat_id, chat_name, chat_type, sender_id

# ----------------------------
# Send message to bot/group
# ----------------------------
async def notify_bot(msg_text):
    global destination_chat
    if not destination_chat:
        print("Destination chat not set, cannot send message.")
        return
    try:
        MAX_CHARS = 400
        if len(msg_text) > MAX_CHARS:
            msg_text = msg_text[:MAX_CHARS] + "\n…[Message truncated]…"
        await client.send_message(destination_chat, msg_text)
    except Exception as e:
        print(f"Failed to send notification to Telegram: {e}")

# ----------------------------
# Resolve username if only username typed
# ----------------------------
async def resolve_username(text):
    username_match = re.match(r"^(?:@|https://t\.me/)([a-zA-Z0-9_]+)$", text.strip())
    if not username_match:
        return None
    username = username_match.group(1)
    try:
        entity = await client.get_entity(username)
        chat_id = getattr(entity, "id", None)
        chat_name = getattr(entity, "title", getattr(entity, "first_name", username))
        chat_type = entity.__class__.__name__
        return {
            "chat_id": chat_id,
            "chat_name": chat_name,
            "chat_type": chat_type,
            "username": username
        }
    except (UsernameInvalidError, UsernameNotOccupiedError):
        return None

# ----------------------------
# Event handler
# ----------------------------
@client.on(events.NewMessage)
async def handler(event):
    global destination_chat
    msg = event.message

    # First-time destination setup
    if not destination_chat and msg.sender:
        destination_chat = msg.sender.id
        creds['destination_chat'] = str(destination_chat)
        with open(CREDENTIALS_FILE, "w", encoding="utf-8") as f:
            json.dump(creds, f, indent=4)
        print(f"✅ Destination chat set to Sender ID: {destination_chat}")

    # Username typed detection
    if msg.text:
        resolved = await resolve_username(msg.text)
        if resolved:
            chat_id = resolved["chat_id"]
            chat_name = resolved["chat_name"]
            chat_type = resolved["chat_type"]
            username = resolved["username"]

            info = (
                f"🔎 Username Detected: @{username}\n"
                f"🆔 Chat ID: {chat_id}\n"
                f"💬 Account Name: {chat_name}\n"
                f"📂 Chat Type: {chat_type}\n"
                f"✉️ Message Title: [No text - Username Lookup]\n"
                f"🕒 Date & Time: {msg.date.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"📂 Forwarded: No (Username Lookup)\n"
                f"📂 Media: No\n"
                f"📂 Message Type: Username\n"
            )

            print(info)
            await notify_bot(info)
            return

    # Otherwise, normal processing
    chat_id, chat_name, chat_type, sender_id = await get_chat_info(msg)

    if msg.media and not msg.text:
        message_title = f"[{msg.media.__class__.__name__}]"
    else:
        message_title = msg.text.splitlines()[0] if msg.text else "[No text]"

    date_info = msg.date.strftime("%Y-%m-%d %H:%M:%S")

    # Chat ID আর Sender ID একই হলে Chat ID দেখাবে না
    chat_id_text = f"🆔 Chat ID: {chat_id}\n" if chat_id and chat_id != sender_id else ""

    extra_info = (
        f"📌 Chat Info:\n"
        f"{chat_id_text}"
        f"💬 Account Name: {chat_name}\n"
        f"📂 Chat Type: {chat_type}\n"
        f"👤 Sender ID: {sender_id}\n"
        f"✉️ Message Title: {message_title}\n"
        f"🕒 Date & Time: {date_info}\n"
        f"📂 Forwarded: {'Yes' if msg.fwd_from else 'No'}\n"
        f"📂 Media: {msg.media.__class__.__name__ if msg.media else 'No'}\n"
        f"📂 Message Type: {'Typed Message' if not msg.fwd_from else 'Forwarded'}\n"
    )

    print(extra_info)
    await notify_bot(extra_info)

# ----------------------------
# Run Bot
# ----------------------------
async def main():
    await client.start(bot_token=bot_token)
    print("✅ Bot is running...")
    print("👉 Forward any message, type username, or send typed message to test")
    await client.run_until_disconnected()

asyncio.run(main())
