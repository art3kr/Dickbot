import os
import json
import requests
import wikipedia

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

msg = 'Dickbot'

@app.route('/', methods=['POST'])
def webhook():
  message_data = request.get_json()

  print(message_data)
  print(message_data['text'][0:5])

  if message_data['name'] != 'DickBot':
    if message_data['text'] == 'Dickbot':
      msg = 'Hello, {}!'.format(message_data['name'])
      post_message(msg)
    if message_data['text'] == '!info':
      msg = 'Created by Antonio Trani. Build 4/13/18' 
      post_message(msg)
    if message_data['text'] == '!commands':
      msg = 'List of commands \n Dickbot...greeting \n !info...bot info \n Steven...he gay \n !wiki...wikipedia search'
      post_message(msg)
    # if 'Steven' or 'steven' in message_data['text']:
    #   msg = 'Just wanna chime in to say Steven is gay'
    #   post_message(msg)
    if '!wiki' in message_data['text'][0:5]:
      wiki_query = message_data['text'][7:]
      wikisearch(wiki_query)


  return "nice", 200

def post_message(msg):
  data = {
          'bot_id' : 'b63310218dbf4c7b3880291f61',
          'text'   : msg,
         }
  post = requests.post('https://api.groupme.com/v3/bots/post', params = data)


def wikisearch(wiki_query):
  # wiki_query = wikipedia.suggest(wiki_query)
  try_search = 1
  try: 
    if try_search == 1:
      summary = wikipedia.summary(wiki_query, sentences = 3)
      post_message(summary)
      
  except wikipedia.exceptions.DisambiguationError:
    print('cannot open summary',wiki_query,'Disambiguation Error')
    try_search = 0
    
  except wikipedia.exceptions.PageError:
    print('cannot open summary',wiki_query,'Page Error')
    try_search = 0
    