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

  if message_data['name'] != 'newdick':
    if message_data['text'] == 'Dickbot':
      msg = 'Hello, {}!'.format(message_data['name'])
      post_message(msg)
    if message_data['text'] == '!info':
      msg = 'Created by Antonio Trani. Build 4/13/18' 
      post_message(msg)

  return "nice", 200

def post_message(msg):
  data = {
          'bot_id' : '9cc0b27ac68c88c0ec058a1ec1',
          'text'   : msg,
         }
  post = requests.post('https://api.groupme.com/v3/bots/post', params = data)

