import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
import datetime

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


def send_planet(update, context):

	planet_input = (update.message.text.split()[1]).lower().capitalize()
	print(planet_input)

	today = datetime.datetime.today()
	format_today = today.strftime("%Y/%m/%d")

	planets = {"Mercury": ephem.Mercury(format_today), 
    "Venus": ephem.Venus(format_today), 
    "Mars" : ephem.Mars(format_today), 
    "Jupiter": ephem.Jupiter(format_today), 
    "Saturn": ephem.Saturn(format_today), 
    "Uranus": ephem.Uranus(format_today), 
    "Neptune": ephem.Neptune(format_today)
    }
	if planet_input in planets.keys():
		result_to_send = (ephem.constellation(planets[planet_input]))[1]
		update.message.reply_text(result_to_send)
	else:
		result_to_send = "there is no planet {}".format(planet_input)
		update.message.reply_text(result_to_send)
    
def main():
	updtr = Updater(settings.TELEGRAM_API_KEY)

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
	updtr.dispatcher.add_handler(CommandHandler("planet", send_planet))
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

	updtr.start_polling()
	updtr.idle()


if __name__ == "__main__":
	logging.info('Bot started')
	main()
