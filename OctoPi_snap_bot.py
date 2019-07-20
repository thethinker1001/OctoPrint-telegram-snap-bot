## Simple bot that sending pictures online from octoprint to telegram bot with refresh button !
## For make it happen you only need to -
## Install requests libary, install telepy libary, change ip string, change token string. 
## Created by www.github.com/thethinker1001 ##


from Tele import * # pip install telepy
from requests import get # pip install requests


octoprint_ip = "IP" # Put OctoPrint ip adress here. * NOTE: if you run this program in the board that octoprint run on so the ip should be 127.0.0.1
token = "TOKEN" # PUT telegram bot token you recived from @BotFather 


def snap(): # Saving picture in folder called images.jpg
    file = open("image.jpg", 'wb')
    file.write(get("http://{}/webcam/?action=snapshot".format(octoprint_ip)).content)
    file.close()


@bot(command='start') # Response for /start command
def start(update):
    snap()
    sendPhoto(update.chat.id, file='image.jpg',reply_markup=inline_keyboard([[{'refresh': 1}]]))
        
@bot(callback_query="1") # Response for button clicked
def refresh(update):
    snap()
    edit_message_media(media=input_media_photo('image.jpg'), update=update, reply_markup=inline_keyboard([[{'refresh': 1}]]))

account(token) 
bot_run() # If you want threads for response for many users at the same time you can add [ example : bot_run(multi=True) ]



