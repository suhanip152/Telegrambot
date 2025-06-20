from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
import os
import asyncio
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Constants
TOKEN: Final = "7750847720:AAFdzV-QY_KxE15oTXX2I8t1EFiMxkVpS9o"
GOOGLE_API_KEY: Final = "AIzaSyCFnhKwNOfULOCJW6oukTrqeIyrFBJBo9g"
CHAT_ID: Final = 5545366860  # Your Chat ID

# Gemini API Configuration
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# Scheduler
scheduler = BackgroundScheduler()

# Generate coding idea
async def generate_coding_idea():
    prompt = "Give me a creative and beginner-friendly coding project idea in 1 sentence."
    response = model.generate_content(prompt)
    return response.text.strip()

# Scheduled task wrapper (runs outside asyncio loop)
def send_idea_wrapper(application):
    asyncio.run(send_idea(application))

# Send idea to Telegram
async def send_idea(application):
    idea = await generate_coding_idea()
    await application.bot.send_message(chat_id=CHAT_ID, text=f"💡 Coding Idea:\n{idea}")

# Start the scheduler
def start_scheduler(application):
    scheduler.add_job(lambda: send_idea_wrapper(application), 'interval', hours = 3)
    scheduler.start()

# Bot commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hello! Your Chat ID is: {update.effective_chat.id}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I will help you in your coding journey!")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")

# Simple message responses
def handle_response(text: str) -> str:
    text = text.lower()
    if "hello" in text:
        return "Hey there!"
    elif "how are you" in text:
        return "I am good!"
    elif "what is your name" in text:
        return "I am your coding uncle."
    return "I'm not sure how to respond to that."

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = handle_response(update.message.text)
    await update.message.reply_text(response)

# Main bot app
def main():
    app = Application.builder().token(TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the scheduler
    start_scheduler(app)

    print("🚀 Bot is running and will send coding ideas every 3 hours...")
    app.run_polling()

if __name__ == "__main__":
    main()
