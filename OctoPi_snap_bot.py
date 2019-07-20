## Simple bot that sending pictures online from octoprint to telegram bot with refresh button !
# For make it happen you only need to -
# Install requests libary, install telepy libary, change ip string, change token string. 
# Created by www.github.com/thethinker1001 

# pip install telepy
from Tele import *
from requests import get 

# Put OctoPrint ip adress here. * NOTE: if you run this program in the board that octoprint run on so the ip should be 127.0.0.1
OCTOPI_IP = "IP" 

# PUT telegram bot token you recived from @BotFather 
TOKEN = "TOKEN" 

def snap(): 
    """ Saving picture in folder called images.jpg """
    with open('image.jpg', 'wb') as file:
        file.write(get("http://{}/webcam/?action=snapshot".format(OCTOPI_IP)).content)


@bot(command='start') 
def start(update):
    """ Response for /start command """
    snap()
    sendPhoto(update.chat.id, file='image.jpg',reply_markup=inline_keyboard([[{'refresh': 1}]]))
     

@bot(callback_query="1") 
def refresh(update):
    """ Response for button clicked """
    snap()
    edit_message_media(media=input_media_photo('image.jpg'), update=update, reply_markup=inline_keyboard([[{'refresh': 1}]]))

account(TOKEN) 
bot_run() 
# If you want threads for response for many users at the same time you can add above [ example : bot_run(multi=True) ]



