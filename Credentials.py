import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get environment variables
GOOGLE_API_KEY = os.environ.get("AIzaSyCFnhKwNOfULOCJW6oukTrqeIyrFBJBo9g")
TELEGRAM_BOT_TOKEN = os.environ.get("AAFdzV-QY_KxE15oTXX2I8t1EFiMxkVpS9o")

print("Google API Key:", GOOGLE_API_KEY)
print("Telegram Bot Token:", TELEGRAM_BOT_TOKEN)


