## Simple bot that sending pictures online from octoprint to telegram bot with refresh button !
# For make it happen you only need to -
# Install requests libary, install telepy libary, change ip string, change token string. 
# Created by www.github.com/thethinker1001 

# pip install telepy
from Tele import *
from requests import get 

# Put OctoPrint ip adress here. * NOTE: if you run this program in the board that octoprint run on so the ip should be 127.0.0.1
octoprint_ip = "IP" 

# PUT telegram bot token you recived from @BotFather 
token = "TOKEN" 


# Saving picture in folder called images.jpg
def snap(): 
    with open('image.jpg', 'wb') as file:
        file.write(get("http://{}/webcam/?action=snapshot".format(octoprint_ip)).content)

# Response for /start command
@bot(command='start') 
def start(update):
    snap()
    sendPhoto(update.chat.id, file='image.jpg',reply_markup=inline_keyboard([[{'refresh': 1}]]))
     
# Response for button clicked
@bot(callback_query="1") 
def refresh(update):
    snap()
    edit_message_media(media=input_media_photo('image.jpg'), update=update, reply_markup=inline_keyboard([[{'refresh': 1}]]))

    
account(token) 
# If you want threads for response for many users at the same time you can add [ example : bot_run(multi=True) ]
bot_run() 



