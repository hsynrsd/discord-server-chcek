# Discord Server Creation Date Checker 🔍

Ever got kicked from a server and wondered *"When was that server even created?"*  
This little script reveals the **creation date** of any Discord server (or user/message/etc.) using its **Snowflake ID**.

## 🧠 How It Works

Discord IDs (called *Snowflakes*) actually contain a timestamp.  
This script decodes that timestamp and tells you **exactly when the server (or whatever) was born.**

## 🛠 Usage

1. Grab the server ID (or any Snowflake).
   - Right-click a server (or user/message) > Copy ID
   - Make sure **Developer Mode** is on in Discord settings!

2. Edit the script:

```python
# Replace this line:
guild_id = "insert id here"
# With your actual ID:
guild_id = 123456789012345678
