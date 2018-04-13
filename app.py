import requests
import time

request_params = {'token': 'gDGDnvNxy2zQ82YIQJS4WTyBeTs73tC7j85tFpg0'}
# response_messages = requests.post('https://api.groupme.com/v3/groups/39366350/messages', params = request_params).json()['response']['messages']

data = {
          'bot_id' : '9cc0b27ac68c88c0ec058a1ec1',
          'text'   : 'tiddies',
         }


while True:
	read_messages = requests.get('https://api.groupme.com/v3/groups/39366350/messages', params = request_params).json()['response']['messages']

	# for message in read_messages:
	print(read_messages[0]['text'])
 #   		#print(read_messages[-1])
 #   		if message[1]['text'] == 'Dickbot':
 #   			post = requests.post('https://api.groupme.com/v3/bots/post', params = data)
	if read_messages[0]['text'] == 'Dickbot':
   		post = requests.post('https://api.groupme.com/v3/bots/post', params = data)


	time.sleep(1)