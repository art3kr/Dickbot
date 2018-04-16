import os
import json
import requests
import wikipedia
import datetime

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

msg = 'Dickbot'

@app.route('/', methods=['POST'])
def webhook():
  message_data = request.get_json()

  print(message_data)
  print(message_data['text'][0:10])

  if message_data['name'] != 'DickBot':
    if message_data['text'] == 'Dickbot':
      msg = 'Hello, {}!'.format(message_data['name'])
      post_message(msg)
    if message_data['text'] == '!info':
      msg = 'Created by Antonio Trani. Build {}}'.format(datetime.date.today()) 
      post_message(msg)
    if message_data['text'] == '!commands':
      msg = 'List of commands \n Dickbot...greeting \n !info...bot info \n Steven...he gay \n !wiki...wikipedia search'
      post_message(msg)
    # if 'Steven' or 'steven' in message_data['text']:
    #   msg = 'Just wanna chime in to say Steven is gay'
    #   post_message(msg)
    if '!wiki' in message_data['text'][0:5]:
      wiki_query = message_data['text'][6:]
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
      summary_url = wikipedia.page(wiki_query).url
      msg = '{} \n {}'.format(summary,summary_url)
      post_message(msg)
      
  except wikipedia.exceptions.DisambiguationError:
    msg = 'cannot open summary,{},Disambiguation Error'.format(wiki_query)
    post_message(msg)
    try_search = 0
    
  except wikipedia.exceptions.PageError:
    msg = 'cannot open summary,{},Page Error'.format(wiki_query)
    post_message(msg)
    try_search = 0
    