# telegram-chat-id-detector
Telegram Chat ID Detector Bot: Detects chat IDs, sender IDs, usernames, forwarded messages, message type, date/time, and media info from Telegram messages using Telethon.

# Telegram Chat ID Detector Bot

**Project Name:** telegram-chat-id-detector  
**Author:** MD Tamim Ikbal 
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
git clone https://github.com/95ninjatecnic/telegram-chat-id-detector.git
cd telegram-chat-id-detector
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the bot**

```bash
python chat_id.py
```

### 🔹 Provide Credentials & Start the Bot

When you first run the bot (`python chat_id.py`), it will ask for your credentials:

1. **Bot Token:**  
   - Open Telegram and start a chat with [BotFather](https://t.me/BotFather).  
   - Create a new bot using `/newbot` and follow the instructions.  
   - After creation, BotFather will give you a **Bot Token**. Copy it.  

2. **API ID & API Hash:**  
   - Go to [my.telegram.org](https://my.telegram.org).  
   - Log in with your Telegram account.  
   - Navigate to **API Development Tools** and create a new application.  
   - You will get your **API ID** (number) and **API Hash** (string).  

3. **Enter Credentials:**  
   - When the bot asks, paste your **Bot Token**, **API ID**, and **API Hash**.  
   - The bot will automatically create `credentials.json` to save these for future use.  

4. **Bot Startup:**  
   - After entering credentials, the bot will connect and start:  


**✅ Bot is running...
👉 Forward any message, type username, or send typed message to test**

## 🔹 How It Works

The **Telegram Chat ID Detector Bot** can detect Chat IDs and other details from forwarded messages, usernames, or typed messages. Here’s how it works:

---

### 🔹 Forwarded Message Detection

When a message is **forwarded** from a group or channel, the bot extracts:

- **Chat ID** of the original sender or channel  
- **Account Name**  
- **Chat Type** (Channel / Group)  
- **Sender ID**  
- **Message Title** or **Media Name**  
- **Date & Time**  
- **Forwarded Status**  
- **Media Type**  
- **Message Type:** Forwarded  

**Example Output:**

  - 📌 Chat Info:
  - 🆔 Chat ID: 2062558134
  - 💬 Account Name: Naruto anime lover
  - 📂 Chat Type: Channel
  - 👤 Sender ID: 6152817532
  - ✉️ Message Title: hi
  - 🕒 Date & Time: 2025-08-24 08:47:25
  - 📂 Forwarded: Yes
  - 📂 Media: No
  - 📂 Message Type: Forwarded

---

### 🔹 Username Lookup

Send a **Telegram username** like `@ai_syestem_fx_bot` to the bot. It detects:

- **Chat ID**  
- **Account Name**  
- **Chat Type** (User / Channel)  
- **Message Type:** Username  
- **Forwarded:** No (Username Lookup)  

**Example Output:**

 - 🔎 Username Detected: @ai_syestem_fx_bot
 - 🆔 Chat ID: 7966538878
 - 💬 Account Name: Secret FX Ti
 - 📂 Chat Type: User
 - ✉️ Message Title: [No text - Username Lookup]
 - 🕒 Date & Time: 2025-08-24 08:49:47
 - 📂 Forwarded: No (Username Lookup)
 - 📂 Media: No
 - 📂 Message Type: Username


---

### 🔹 Typed Messages in Private Chat

Send any **normal text message** directly to the bot. It detects:

- **Chat ID**  
- **Account Name**  
- **Chat Type:** Private  
- **Sender ID**  
- **Message Content**  
- **Date & Time**  
- **Message Type:** Typed Message  

**Example Output:**

 - 📌 Chat Info:
 - 💬 Account Name: Naruto anime lover
 - 📂 Chat Type: Private
 - 👤 Sender ID: 6152817532
 - ✉️ Message Title: Hi i am Tamim ikbal
 - 🕒 Date & Time: 2025-08-24 08:50:20
 - 📂 Forwarded: No
 - 📂 Media: No
 - 📂 Message Type: Typed Message

---

### ⚡ Summary

- **Forwarded messages**: Extract full info from the original sender or channel  
- **Username messages**: Detect chat ID & account info via username lookup  
- **Typed messages**: Detect chat ID and content from normal private messages  

###  🔹 Auto-Created Files
File/Folder	Purpose
credentials.json	Stores Bot Token, API ID & API Hash. Auto-created on first run.
state.json	Stores destination chat ID & bot state. Auto-created on first run.
logs/	Saves processed message logs for reference. Auto-created on first run.


###  🔹 Notes

Make sure your bot is added to groups or channels you want to monitor.
For username lookup, the bot needs to be able to see the user or channel (private usernames may not be detected).
Avoid editing credentials.json and state.json manually unless necessary.

###  ✅ Enjoy using the Telegram Chat ID Detector Bot!###
