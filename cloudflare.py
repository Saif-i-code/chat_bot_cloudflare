import telebot
import requests
import json
import os 
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), "chat_cloudflare.env"))

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CLOUDFLARE_ACCOUNT_ID = os.getenv('CLOUDFLARE_ACCOUNT_ID')
CLOUDFLARE_TOKEN = os.getenv('CLOUDFLARE_TOKEN')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

MODEL = "@cf/google/gemma-4-26b-a4b-it"

def cf(prompt_text):
    url = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/run/{MODEL}"
    
    head = {
        'Authorization': f'Bearer {CLOUDFLARE_TOKEN}',
        'Content-Type': 'application/json'    
    }

    data = {
        "max_tokens": 4000,
        "temperature": 0.3,
        "messages": [
            {"role": "system", "content": "you are ai"},
            {"role": "user", "content": prompt_text}
        ]
    }
    
    try:
        res = requests.post(url, headers=head, json=data)
        response_data = res.json()
        if response_data.get('success') and 'result' in response_data:
            result = response_data['result']
            if 'response' in result:
                return result['response']
            elif 'choices' in result and len(result['choices']) > 0:
                return result['choices'][0]['message']['content']
        return f"خطأ: {response_data}"
            
    except Exception as e:
        print(f"Error: {e}")
        return "عذراً، حدث خلل."

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_chat_action(message.chat.id, 'typing')
    ai_resp = cf(message.text)
    bot.reply_to(message, ai_resp)

print("البوت شغال")
bot.infinity_polling()
