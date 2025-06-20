import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get environment variables
GOOGLE_API_KEY = os.environ.get("")
TELEGRAM_BOT_TOKEN = os.environ.get("")

print("Google API Key:", GOOGLE_API_KEY)
print("Telegram Bot Token:", TELEGRAM_BOT_TOKEN)


