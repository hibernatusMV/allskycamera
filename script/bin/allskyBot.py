import sys
import os
import subprocess
import time
import datetime
from datetime import timedelta
import telepot
from telepot.loop import MessageLoop

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/uptime':
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_string = str(timedelta(seconds = uptime_seconds))
            bot.sendMessage(chat_id, uptime_string[:-7])
    elif command == '/shutdown':
        bot.sendMessage(chat_id, 'shutdown system!')
        os.system("sudo shutdown now")
    elif command == '/reboot':
        bot.sendMessage(chat_id, 'rebooting system!')
        os.system("shutdown -r now")
    elif command == '/temp':
        hdl = subprocess.Popen("/home/pi/bin/getTempDetail.sh", shell=True, stdout=subprocess.PIPE).stdout
        res = hdl.read()
        bot.sendMessage(chat_id, res)
    elif command == '/heat':
        hdl = subprocess.Popen("/home/pi/bin/allskyheating.sh status", shell=True, stdout=subprocess.PIPE).stdout
        res = hdl.read()
        bot.sendMessage(chat_id, res)
    elif command == '/live':
        bot.sendPhoto (chat_id, photo=open("/home/pi/allsky/liveview-image.jpg", "rb"))

bot = telepot.Bot('1147414184:AAFEpAz2q9X-FRNKplofaXXyu6c3PxwAU-A')

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
