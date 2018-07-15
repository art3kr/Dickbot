import os
import json
import requests
import wikipedia
import datetime
import googlesearch
import giphypop
import urbandictionary as ud

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

msg = 'Dickbot'

@app.route('/', methods=['POST'])
def webhook():
  message_data = request.get_json()

  global group_id
  group_id = message_data['group_id']

  print(message_data)
  print(message_data['text'][0:4])

  if message_data['name'] != 'DickBot':
    if message_data['text'] == 'Dickbot':
      msg = 'Hello, {}!'.format(message_data['name'])
      post_message(msg)
    if message_data['text'] == '!info':
      msg = 'Created by Antonio Trani. Build {}'.format(datetime.date.today()) 
      post_message(msg)
    if message_data['text'] == '!commands':
      msg = 'List of commands \n Dickbot...greeting \n !info...bot info \n !gif...giphy search \n !search...Google text search \n !ud...urban dictionary search \n !wiki...wikipedia search'
      post_message(msg)
    # if 'Steven' or 'steven' in message_data['text']:
    #   msg = 'Just wanna chime in to say Steven is gay'
    #   post_message(msg)
    if '!wiki' in message_data['text'][0:5]:
      wiki_query = message_data['text'][6:]
      wikisearch(wiki_query)
    if '!search' in message_data['text'][0:7]:
      search_query = message_data['text'][8:]
      google_search(search_query)
    if '!gif' in message_data['text'][0:4]:
      giphy_query = message_data['text'][5:]
      giphy_search(giphy_query)
    if '!ud' in message_data['text'][0:3]:
      ud_query = message_data['text'][4:]
      urban_dictionary_search(ud_query)



  return "nice", 200

def post_message(msg):
  if group_id == '20300243':
    bot_id = 'f922569adbdbfdbfe3bb4b9f52'
  if group_id == '40048618':
    bot_id = 'b63310218dbf4c7b3880291f61'
  if group_id == '39366350':
    bot_id = '1c78008e0593154b5c04be0a87'
  if group_id == '40252458':
  	bot_id = 'ccd80a0c800d1da0a443c847f6'
  if group_id == '40670730':
  	bot_id = '22566247d9f91eb7147475446d'
  data = {
          'bot_id' : bot_id,
          'text'   : msg,
         }
  post = requests.post('https://api.groupme.com/v3/bots/post', params = data)

def post_image(msg):
  if group_id == '20300243':
    bot_id = 'f922569adbdbfdbfe3bb4b9f52'
  if group_id == '40048618':
    bot_id = 'b63310218dbf4c7b3880291f61'
  if group_id == '39366350':
    bot_id = '1c78008e0593154b5c04be0a87'
  if group_id == '40252458':
  	bot_id = 'ccd80a0c800d1da0a443c847f6'

  attachments = {
          'type' : 'image',
          'url'   : msg,
         }

  data = {
          'bot_id'      : bot_id,
          'attachments' : [attachments],
         }
  post = requests.post('https://api.groupme.com/v3/bots/post', params = data)

def wikisearch(wiki_query):
  # wiki_query = wikipedia.suggest(wiki_query)
  try_search = 1
  try: 
    if try_search == 1:
      summary = wikipedia.summary(wiki_query, sentences = 3)
      summary_url = wikipedia.page(wiki_query).url
      msg = '{} \n{}'.format(summary,summary_url)
      post_message(msg)
      
  except wikipedia.exceptions.DisambiguationError:
    msg = 'cannot open summary: "{}" \nDisambiguation Error'.format(wiki_query)
    post_message(msg)
    try_search = 0
    
  except wikipedia.exceptions.PageError:
    msg = 'cannot open summary: "{}" \nPage Error'.format(wiki_query)
    post_message(msg)
    try_search = 0
    
def google_search(search_query):
  urls = []
  for url in googlesearch.search(search_query, stop = 1):
    urls.append(url)
  msg = '{} {} {} {} {}'.format(urls[0],urls[1],urls[2],urls[3],urls[4])
  print(msg)
  post_message(msg)

def giphy_search(giphy_query):
	msg = giphypop.Giphy().translate(phrase=giphy_query).media_url
	# post_image(msg)
	post_message(msg)

def urban_dictionary_search(ud_query):
	definitions = ud.define(ud_query)
	msg = ud_query + '\n\n'

	for num, d in enumerate(definitions):
		msg = msg + d.definition
		msg = msg + '\n\n'
		msg = msg + d.example

		if num == 0:
			break
		elif num < 0:
			msg = msg + '\n\n'

	post_message(msg)
