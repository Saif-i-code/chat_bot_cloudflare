# chat_bot_cloudflare
This tool connects the Telegram bot to the Cloudflare Workers AI service using a company token
This tool is a simple bridge that connects AI with a Telegram bot.

## Getting Started

1. Create a bot on Telegram via **BotFather** and get your `TELEGRAM_TOKEN`.
2. From your **Cloudflare** dashboard, get your `CLOUDFLARE_ACCOUNT_ID` and `CLOUDFLARE_TOKEN`.
3. Place these variables inside your `.env` file.
4. Run the application.

## Customization Notes
* **Change AI Model:** You can change the model inside `cloudflare.py` on **line 14**.
* **Change Token Size:** You can adjust the token limit inside `cloudflare.py` on **line 25**.

  Developed with 🖤 by **Saif Ali**
