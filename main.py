from pyrogram import Client, filters
from pyrogram.types import Message
import requests
from config import API_ID, API_HASH, BOT_TOKEN

# Telegraph API endpoint
TELEGRAPH_API_URL = "https://api.telegra.ph/upload"
# Max file size in bytes (10 MB)
MAX_FILE_SIZE = 10 * 1024 * 1024

app = Client("my_upload_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def upload_to_telegraph(file_path):
    files = {"file": open(file_path, "rb")}
    response = requests.post(TELEGRAPH_API_URL, files=files)
    if response.status_code == 200:
        result = response.json()
        return result["src"]
    else:
        return None

@app.on_message(filters.command("start"))
def start_command(client, message):
    message.reply_text("✨ Welcome to the upload bot! Send me a file or photo to upload to Telegraph.")

@app.on_message(filters.document | filters.photo)
def handle_media(client, message):
    if message.document:
        media_type = "document"
        media = message.document
    elif message.photo:
        media_type = "photo"
        media = message.photo[-1]

    if media.file_size > MAX_FILE_SIZE:
        message.reply_text("📚 File size exceeds the limit (10MB). Please send a smaller file.")
        return

    file_path = client.download_media(message, file_name="uploaded_file")
    telegraph_url = upload_to_telegraph(file_path)
    if telegraph_url:
        message.reply_text(f"🎊 {media_type.capitalize()} uploaded successfully!\n\n[View on Telegraph]({telegraph_url})", parse_mode="Markdown")
    else:
        message.reply_text("🧰 Failed to upload file. Please try again later.")

print("Bot Run")
app.run()
