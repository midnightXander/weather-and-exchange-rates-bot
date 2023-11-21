#from telegram.ext import Updater,CommandHandler
from telegram.ext import CommandHandler,ContextTypes,MessageHandler,Application,filters
from typing import final
from telegram import Update
import requests


import os

MY_URL = 'https://cryptoapi-4955.up.railway.app/get'
data = requests.get(MY_URL)
data = data.json()

curr_temp = data['temperature']
xaf_rate = data['usd_rates']['XAF']
eur_rate = data['usd_rates']['EUR']
gbp_rate = data['usd_rates']['GBP']

#async def ret_weather():
#    return "the temp in yaounde is " + str(curr_temp) + " celsius "

#async def ret_exchange_rates():
#    return "Hello. Here are the latest USD conversion rates USD -> XAF:"+str(xaf_rate)+ "\n USD -> EUR:"+str(eur_rate)+"\n USD -> GBP:"+str(gbp_rate)

async def weather(update,context):
    response = "the temp in yaounde is " + str(curr_temp) + " celsius "
    await update.message.reply_text(response)


async def currency(update,context):
    response = "Hello. Here are the latest USD conversion rates \n USD -> XAF: "+str(xaf_rate)+ "\n USD -> EUR: "+str(eur_rate)+"\n USD -> GBP: "+str(gbp_rate)
    await update.message.reply_text(response)

async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await  update.message.reply_text("Hey! tap /weather or /currency to get interesting informations")

async def error(update:Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'Update: {update} caused the error: {context.error}')

def main():

    print('start Polling...')

    TOKEN = os.getenv('BOTAPIKEY')

    BOT_USERNAME:final = '@weather_exc_bot'

    app = Application.builder().token(TOKEN).build()

    weather_handler = CommandHandler('weather',weather)
    currency_handler = CommandHandler('currency',currency)
    start_handler = CommandHandler('start',start)
    
    #commands
    app.add_handler(weather_handler)
    app.add_handler(currency_handler)
    app.add_handler(start_handler)
    
    #errors
    app.add_error_handler(error)
    
    print('Polling...')
    app.run_polling(poll_interval=3)
    
if __name__ == '__main__':    
        main()



