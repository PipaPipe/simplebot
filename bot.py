import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log'
					)


def start_bot(update, context):
	print(update)
	mytext = "Hello,{}! I am simple bot and understand only command {}".format(update.message.chat.first_name, '/start')
	update.message.reply_text(mytext)


def chat(update, context):
	text = update.message.text
	logging.info(text)
	update.message.reply_text(text)


def main():
	updtr = Updater(settings.TELEGRAM_API_KEY)

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))
	updtr.start_polling()
	updtr.idle()


if __name__ == "__main__":
	logging.info('Bot started')
	main()