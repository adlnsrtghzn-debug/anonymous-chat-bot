import telebot

TOKEN = "8725143532:AAEXolKE16YSQKGBwdJV60dGyaDeaYiaWNs"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, f"سلام!\nآیدی شما: {message.from_user.id}")

bot.infinity_polling()
