import telebot

bot_token = '6324323527:AAHYFu4nvzqMVnYK5jmDKgw1bGEVvHjoI9o'
bot = telebot.TeleBot(bot_token)

@bot.message_handler()
def echo(message):
    bot.reply_to(message, message)

bot.polling()
