# telegram-chat-id-detector
Telegram Chat ID Detector Bot: Detects chat IDs, sender IDs, usernames, forwarded messages, message type, date/time, and media info from Telegram messages using Telethon.

# Telegram Chat ID Detector Bot

**Project Name:** telegram-chat-id-detector  
**Author:** MR  
**License:** MIT  

---

## 🔹 Overview

This is a **Telegram bot** that helps you detect and display **Chat IDs** along with other detailed information for any Telegram message. It is useful for developers, admins, or anyone who needs to quickly find Telegram user or group IDs.  

The bot works in multiple scenarios:

1. **Forwarded Messages:** Detects forwarded messages from any **group or channel** and provides the original sender’s chat ID and other details.  
2. **Username Lookup:** Send a Telegram username (e.g., `@username`) to the bot, and it fetches the chat ID and details of the user or channel.  
3. **Typed Messages:** Any direct message sent to the bot will show the sender’s chat ID and details.  

---

## 🔹 Features

- ✅ Detect **forwarded messages** and original sender’s info.  
- ✅ Lookup **username** to get chat ID and other details.  
- ✅ Detect **typed messages** in private chats.  
- ✅ Auto-create and manage **logs** in the `logs/` folder.  
- ✅ Stores **bot state** in `state.json` (destination chat ID).  
- ✅ Stores **bot credentials** in `credentials.json` (bot token, API ID, API hash).  
- ✅ Shows comprehensive info including:

📌 Chat Info:
- 🆔 Chat ID  
- 💬 Account Name  
- 📂 Chat Type  
- 👤 Sender ID  
- ✉️ Message Title / Media Info  
- 🕒 Date & Time  
- 📂 Forwarded status  
- 📂 Media Type  
- 📂 Message Type (Forwarded / Typed / Username)  

---

## 🔹 Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/<your-username>/telegram-chat-id-detector.git
cd telegram-chat-id-detector


Install dependencies:

pip install -r requirements.txt


Run the bot:

python chat_id.py


Provide credentials when prompted:

Bot Token: Create a bot using BotFather
 and get the token.

API ID & API Hash: Obtain from my.telegram.org
.

After entering the credentials, the bot will start:

✅ Bot is running...
👉 Forward any message, type username, or send typed message to test

🔹 How It Works
1️⃣ Forwarded Message Detection

When a message is forwarded from a group or channel, the bot extracts:

Chat ID of the original sender or channel

Account Name

Chat Type (Channel / Group)

Sender ID

Message Title or Media Name

Date & Time

Forwarded status

Media type

Message Type: Forwarded

Example Output:

📌 Chat Info:
🆔 Chat ID: 2062558134
💬 Account Name: Naruto anime lover
📂 Chat Type: Channel
👤 Sender ID: 6152817532
✉️ Message Title: hi
🕒 Date & Time: 2025-08-24 08:47:25
📂 Forwarded: Yes
📂 Media: No
📂 Message Type: Forwarded

2️⃣ Username Lookup

Send a Telegram username like @ai_syestem_fx_bot to the bot. It detects:

Chat ID

Account Name

Chat Type (User / Channel)

Message Type: Username

Forwarded: No (Username Lookup)

Example Output:

🔎 Username Detected: @ai_syestem_fx_bot
🆔 Chat ID: 7966538878
💬 Account Name: Secret FX Ti
📂 Chat Type: User
✉️ Message Title: [No text - Username Lookup]
🕒 Date & Time: 2025-08-24 08:49:47
📂 Forwarded: No (Username Lookup)
📂 Media: No
📂 Message Type: Username

3️⃣ Typed Messages in Private Chat

Send any normal text message directly to the bot. It detects:

Chat ID

Account Name

Chat Type: Private

Sender ID

Message content

Date & Time

Message Type: Typed Message

Example Output:

📌 Chat Info:
💬 Account Name: Naruto anime lover
📂 Chat Type: Private
👤 Sender ID: 6152817532
✉️ Message Title: Hi i am Tamim ikbal
🕒 Date & Time: 2025-08-24 08:50:20
📂 Forwarded: No
📂 Media: No
📂 Message Type: Typed Message

🔹 Auto-Created Files
File/Folder	Purpose
credentials.json	Stores Bot Token, API ID & API Hash. Auto-created on first run.
state.json	Stores destination chat ID & bot state. Auto-created on first run.
logs/	Saves processed messages logs for reference. Auto-created on first run.
🔹 Notes

Make sure your bot is added to groups or channels you want to monitor.

For username lookup, the bot needs to be able to see the user or channel (private usernames may not be detected).

Avoid editing credentials.json and state.json manually unless necessary.

🔹 Bot Workflow (Visual Diagram)
User / Group / Channel
       │
       ▼
    Send Message
       │
 ┌───────────────┐
 │  Bot Receives │
 └───────────────┘
       │
       ├─ Forwarded Message ──► Detect Chat ID + Other Info
       │
       ├─ Typed Message ─────► Detect Chat ID + Other Info
       │
       └─ Username Lookup ───► Detect Chat ID + Other Info
       │
       ▼
  Display Info in Telegram
       │
       ▼
  Optional: Save Logs (logs/)
