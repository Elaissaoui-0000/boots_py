from telebot import TeleBot

TOKEN = "YOUR_BOT_TOKEN_HERE"

bot = TeleBot(TOKEN)

@bot.message_handler(commands='start')
def welcome(message):
    chat_id = message.chat.id
    user = message.from_user.first_name
    bot.send_message(chat_id=chat_id,text=f"hello {user}")
    
print('Bot is running ...')
bot.infinity_polling()