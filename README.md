
# Telegram Website Security Scanner Bot

A Telegram bot that performs automated website scanning using Katana, httpx, and subzy tools to gather information and check for subdomain takeovers.

## Features
- URL validation and processing
- Automated scanning with Katana (crawling)
- Live URL checking with httpx
- Subdomain takeover detection with subzy
- Secure user authorization system
- Results delivered directly in Telegram

## Prerequisites
Before using this bot, you need to install the following tools:

### Required Tools Installation

1. **Katana** (Web crawling):
   ```bash
   go install github.com/projectdiscovery/katana/cmd/katana@latest
   ```

2. **httpx** (HTTP toolkit):
   ```bash
   go install github.com/projectdiscovery/httpx/cmd/httpx@latest
   ```

3. **subzy** (Subdomain takeover detection):
   ```bash
   go install github.com/LukaSikic/subzy@latest
   ```

4. **Python dependencies**:
   ```bash
   pip install python-telegram-bot
   ```

## Setup Instructions

1. **Clone the repository** (if applicable) or create a new file with the bot code.

2. **Create a users.txt file** to store authorized Telegram user IDs (one per line):
   ```bash
   touch users.txt
   ```

3. **Edit the bot token** in the script:
   ```python
   TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
   ```

4. **Run the bot**:
   ```bash
   python3 bot.py
   ```

## Usage
1. Start the bot with `/start` command
2. Send a valid URL (starting with http:// or https://)
3. The bot will process the URL and send back the results

## Bot Commands
- `/start` - Initialize the bot and check authorization

## Security Notes
- Only users listed in `users.txt` can interact with the bot
- Always validate URLs before processing
- The bot automatically cleans up temporary files after each scan


## Note
Make sure all required tools (katana, httpx, subzy) are installed and available in your system's PATH before running the bot.
```
