import requests

class simpleBot:

	def __init__(self, bot_key, bot_name):
		self.bot_url = f'https://api.telegram.org/bot{bot_key}/'
		self.bot_name = bot_name

	def getRequest(self, url, data):
		result = requests.get(url = url, data = data)
		return result.json()

	def postRequest(self, **kargs):
		result = requests.post(**kargs)
		return result.json()

	def sendMessage(self, chat_id, text):
		return self.postRequest(url = f'{self.bot_url}sendMessage', data = {'chat_id': chat_id, 'text': text})

	def sendPhoto(self, chat_id, photo_url, is_upload = False, caption = None):
		files = None
		data = {}
		data['chat_id'] = chat_id
		if is_upload:
			files = {'photo': open(f'{photo_url}', 'rb')}
			data['caption'] = caption
		else:
			data['photo'] = photo_url
		return self.postRequest(url = f'{self.bot_url}sendPhoto', data = data, files = files)

	def deleteMessage(self, chat_id, message_id):
		return self.postRequest(url = f'{self.bot_url}deleteMessage', data = {'chat_id': chat_id, 'message_id': message_id})

	def sendAnswerCallbackQuery(self, json_data):
		return self.postRequest(url = f'{self.bot_url}answerCallbackQuery', json = json_data)

	def createKeyboard(self, chat_id, text, json_keyboard):
		return self.postRequest(url = f'{self.bot_url}sendMessage', json = {'chat_id': chat_id, 'text': text, 'reply_markup': json_keyboard})

	def removeKeyboard(self, chat_id):
		data = self.postRequest(url = f'{self.bot_url}sendMessage', json = {'chat_id': chat_id, 'text': 'Remove keyboard', 'reply_markup': {'remove_keyboard': True} })
		self.deleteMessage(chat_id, data['result']['message_id'])

	def getChatMembersCount(self, chat_id):
		r = self.getRequest(f'{self.bot_url}getChatMembersCount', {'chat_id':chat_id})
		return r['result']

	def getChatMember(self, chat_id, user_id):
		r = self.getRequest(f'{self.bot_url}getChatMember', {'chat_id':chat_id, 'user_id':user_id})
		return r['result']