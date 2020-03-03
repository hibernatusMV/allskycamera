import sys
import os
import subprocess
import time
import datetime
from datetime import timedelta
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

# routine to proceed different functions
def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    chat_id = msg['message']['chat']['id']
    
    if query_data == 'cancel':
        bot.sendMessage(chat_id, 'Cancelled.', reply_markup = ReplyKeyboardRemove())
    elif query_data == 'shutdown':
        bot.sendMessage(chat_id, 'shutting down system. Bye.', reply_markup = ReplyKeyboardRemove())
        os.system("sudo shutdown -h now")
    elif query_data == 'reboot':
        bot.sendMessage(chat_id, 'rebooting system. Hold on.', reply_markup = ReplyKeyboardRemove())
        os.system("sudo reboot")
    elif query_data == 'temp':
        hdl = subprocess.Popen("/home/pi/bin/getTempDetail.sh", shell=True, stdout=subprocess.PIPE).stdout
        res = hdl.read()
        bot.sendMessage(chat_id, res)
    elif query_data == 'heat':
        hdl = subprocess.Popen("/home/pi/bin/allskyheating.sh status", shell=True, stdout=subprocess.PIPE).stdout
        res = hdl.read()
        bot.sendMessage(chat_id, res)
    elif query_data == 'live':
        bot.sendPhoto (chat_id, photo=open("/home/pi/allsky/liveview-image.jpg", "rb"))

# routine to listen to user input
def on_chat_message(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    # define button menu
    shtdnkeyboard = InlineKeyboardMarkup(inline_keyboard=[
        #/shutdown
        [InlineKeyboardButton(text="Shutdown",callback_data='shutdown'), InlineKeyboardButton(text="Cancel",callback_data='cancel')]
    ])

    rbootkeyboard = InlineKeyboardMarkup(inline_keyboard=[
        #/reboot
        [InlineKeyboardButton(text="Reboot",callback_data='reboot'), InlineKeyboardButton(text="Cancel",callback_data='cancel')]
    ])
    
    allskykeyboard = InlineKeyboardMarkup(inline_keyboard=[
        #/system
        [InlineKeyboardButton(text="Env. Temp.",callback_data='temp'), InlineKeyboardButton(text="Heat Status",callback_data='heat'), InlineKeyboardButton(text="Live-View",callback_data='live')]
    ])
        
    if command == '/uptime':
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_string = str(timedelta(seconds = uptime_seconds))
            bot.sendMessage(chat_id, uptime_string[:-7])
    elif command == '/shutdown':
        bot.sendMessage(chat_id, 'Do you really want to shutdown?', reply_markup = shtdnkeyboard)
    elif command == '/reboot':
        bot.sendMessage(chat_id, 'Do you really want to reboot?', reply_markup = rbootkeyboard)
    elif command == '/system':
        bot.sendMessage(chat_id, 'Allsky Camera System', reply_markup = allskykeyboard)

# define token generated by Telegram itself (by running /newbot in botfather chat)
bot = telepot.Bot('1147414184:AAFEpAz2q9X-FRNKplofaXXyu6c3PxwAU-A')

# loop to listen for user input
MessageLoop(bot, { 'chat': on_chat_message, 'callback_query': on_callback_query }).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
