import os
import subprocess
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Path to the users file
USERS_FILE = "users.txt"

# Check if the user is authorized
def is_authorized(user_id):
    if not os.path.exists(USERS_FILE):
        return False
    with open(USERS_FILE, "r") as f:
        authorized_users = f.read().splitlines()
    return str(user_id) in authorized_users

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not is_authorized(user_id):
        await update.message.reply_text("Unauthorized user. Please contact the admin.")
        return
    await update.message.reply_text("Welcome to the website processing bot! Send me a website in plain text to start.")

# Handle incoming text messages
async def process_website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not is_authorized(user_id):
        await update.message.reply_text("Unauthorized user. Please contact the admin.")
        return

    website = update.message.text.strip()

    # Validate the website format
    if not website.startswith("http://") and not website.startswith("https://"):
        await update.message.reply_text("Invalid website format. Please provide a valid URL starting with http:// or https://.")
        return

    # Cleanup old files
    for file_name in ["list.txt", "live.txt", "final.txt"]:
        if os.path.exists(file_name):
            os.remove(file_name)

    try:
        # Run katana tool
        subprocess.run(["katana", "-u", website, "-o", "list.txt"], check=True)
        
        # Run httpx tool
        subprocess.run(["httpx", "-l", "list.txt", "-o", "live.txt"], check=True)
        
        # Run subzy tool
        subprocess.run(["subzy", "run", "-targets", "live.txt"], check=True)

        # Send the final.txt file back to the user
        if os.path.exists("final.txt"):
            await update.message.reply_document(document=open("final.txt", "rb"))
        else:
            await update.message.reply_text("No results found.")

    except subprocess.CalledProcessError as e:
        await update.message.reply_text(f"An error occurred while processing: {str(e)}")

# Main function to set up the bot
async def main():
    # Your Telegram Bot Token
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

    # Initialize the application
    application = Application.builder().token(TOKEN).build()

    # Add command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_website))

    # Run the bot
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
