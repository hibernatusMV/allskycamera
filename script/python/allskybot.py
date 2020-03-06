#!/usr/bin python2.7
import sys
import os
import subprocess
import urllib2
import emoji
import telepot
import time
from datetime import datetime
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config.constants import SHELL_SCRIPT_PATH, ALLSKY_IMAGE_PATH
from config.auth import TOKEN, CHAT_ID

def init():
    global bot
    bot = telepot.Bot(TOKEN)

# calling process to shutdown, reboot etc. Pi
def call_shutdown(option):
    subprocess.Popen("sudo shutdown " + "--" + option + " now", shell=True, stdout=subprocess.PIPE).stdout
    sys.exit()

# call heater specific actions    
def call_heater(option):
    hdl = subprocess.Popen(SHELL_SCRIPT_PATH + "/allskyheating.sh " + option, shell=True, stdout=subprocess.PIPE).stdout
    res = hdl.read()
    return res

# get temperature of sensor
def get_temp():
    hdl = subprocess.Popen(SHELL_SCRIPT_PATH + "/getTempDetail.sh", shell=True, stdout=subprocess.PIPE).stdout
    res = hdl.read()
    return res

# display time since Pi is up and running    
def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds = uptime_seconds))
    return uptime_string

# routine to listen to user input
def on_chat_message(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    
    print 'Got command: %s' % command
    
    # define button menu
    shtdnkeyboard = ReplyKeyboardMarkup(keyboard=[
        #/shutdown
        [KeyboardButton(text="Shutdown"), KeyboardButton(text="Cancel")]
    ], resize_keyboard=True)

    rbootkeyboard = ReplyKeyboardMarkup(keyboard=[
        #/reboot
        [KeyboardButton(text="Reboot"), KeyboardButton(text="Cancel")]
    ], resize_keyboard=True)
    
    allskykeyboard = ReplyKeyboardMarkup(keyboard=[
        #/system
        [KeyboardButton(text='Dome Temp.'), KeyboardButton(text='Heater Status'), KeyboardButton(text='Live-View')],
        [KeyboardButton(text='Heater: ON'), KeyboardButton(text='Heater: OFF')]
    ], resize_keyboard=True)
    
    # user action input
    if command == '/uptime':
        uptime_string = get_uptime()
        bot.sendMessage(chat_id, emoji.emojize(':hourglass_flowing_sand: ' + uptime_string[:-7], use_aliases=True))
    elif command == '/shutdown':
        bot.sendMessage(chat_id, emoji.emojize('Do you really want to shutdown? :scream:', use_aliases=True), reply_markup = shtdnkeyboard)
    elif command == '/reboot':
        bot.sendMessage(chat_id, emoji.emojize('Do you really want to reboot? :confused:', use_aliases=True), reply_markup = rbootkeyboard)
    elif command == '/system':
        bot.sendMessage(chat_id, emoji.emojize(':camera: Allsky Camera Status', use_aliases=True), reply_markup = allskykeyboard)
    
    # button click events
    if command == 'Cancel':
        bot.sendMessage(chat_id, emoji.emojize('aborted. :relaxed:', use_aliases=True), reply_markup = ReplyKeyboardRemove(remove_keyboard=True))
    elif command == 'Dome Temp.':
        res = get_temp()
        bot.sendMessage(chat_id, res)
    elif command == 'Heater Status':
        res = call_heater("status")
        bot.sendMessage(chat_id, res)
    elif command == 'Heater: ON':
        res = call_heater("on")
        bot.sendMessage(chat_id, emoji.emojize(':zap: ' + res, use_aliases=True))
    elif command == 'Heater: OFF':
        res = call_heater("off")
        bot.sendMessage(chat_id, emoji.emojize(':snowflake: ' + res, use_aliases=True))
    elif command == 'Live-View':
        bot.sendPhoto (chat_id, photo=open(ALLSKY_IMAGE_PATH, "rb"))
    elif command == 'Shutdown':
        bot.sendMessage(chat_id, emoji.emojize(':dizzy_face::zzz: shutting down system. Bye.', use_aliases=True), reply_markup = ReplyKeyboardRemove(remove_keyboard=True))
        call_shutdown("poweroff")
    elif command == 'Reboot':
        bot.sendMessage(chat_id, emoji.emojize(':cyclone: rebooting system. Hold on.', use_aliases=True), reply_markup = ReplyKeyboardRemove(remove_keyboard=True))
        call_shutdown("reboot")
        
def wait_for_internet_connection():
    while True:
        try:
            response = urllib2.urlopen('http://www.google.com',timeout=1)
            return
        except urllib2.URLError:
            pass

def main():
    init()
    wait_for_internet_connection()
    
    # loop to listen for user input
    MessageLoop(bot, on_chat_message).run_as_thread()
    print 'I am listening ...'
    
    dt_now = datetime.now()
    starttime = dt_now.strftime("%d.%m.%Y %H:%M:%S")
    print 'Start time: ', starttime
    
    ip_address = subprocess.check_output("hostname -I | awk '{print $1}'", shell=True).decode('ascii')
    bot.sendMessage(CHAT_ID, emoji.emojize(":rocket: Hello, I\'m online and my IP-Address is " + ip_address, use_aliases=True))

    while 1:
        time.sleep(10)
        
if __name__ == "__main__":
    main()