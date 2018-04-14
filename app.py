import os
import json
import requests

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

msg = 'Dickbot'

@app.route('/', methods=['POST'])
def webhook():
  message_data = request.get_json()

  print(message_data)

  if message_data['text'] == 'Dickbot' and message_data['name'] != 'Dickbot':
    post_message(msg)

  return "nice", 200

def post_message(msg):
  data = {
          'bot_id' : '9cc0b27ac68c88c0ec058a1ec1',
          'text'   : msg,
         }
  post = requests.post('https://api.groupme.com/v3/bots/post', params = data)



#   # We don't want to reply to ourselves!
#   if data['name'] != 'apnorton-test-bot':
#     msg = '{}, you sent "{}".'.format(data['name'], data['text'])
#     send_message(msg)

#   return "ok", 200

# def send_message(msg):
#   url  = 'https://api.groupme.com/v3/bots/post'

#   data = {
#           'bot_id' : os.getenv('GROUPME_BOT_ID'),
#           'text'   : msg,
#          }
#   request = Request(url, urlencode(data).encode())
#   json = urlopen(request).read().decode()