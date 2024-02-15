# Telegram Upload Bot

This Telegram bot, built using Pyrogram, allows users to upload files and photos to Telegraph, a platform for publishing and sharing articles. The bot provides a simple and intuitive interface for uploading files and generates a shareable link to view the uploaded content on Telegraph.

## Features
- Supports uploading of documents (e.g., PDFs, DOCX) and photos
- Checks file size before uploading to ensure it does not exceed the limit
- Provides a link to view the uploaded content on Telegraph

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites
- Python 3.6 or higher
- Telegram Bot API token (obtain from BotFather)
- Telegraph account (for viewing uploaded content)

### Installation
- Clone the repository:
   ```bash
   git clone https://github.com/cnn2345/telegraph-upload-bot.git
   cd telegraph-upload-bot
   pip install -r requirements.txt
   # Update the config.py file with your API credentials.
   python bot.py

### Usage
- Start the bot and send a file or photo to upload.
- The bot will upload the file to Telegraph and provide a link to view it.

### Technologies Used
- Pyrogram: Python wrapper for the Telegram API
- Telegraph API: Used for uploading files and photos

### Contributing
- Contributions are welcome! Please fork the repository and submit a pull request.

### License
- This project is licensed under the GNU General Public License v3.0 - see the ```LICENSE``` file for details.
