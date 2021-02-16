import requests
import json
import secrets
from models.token import Token

class TokensApi:

	def __init__(self):
		self.endpoint = 'https://60280ddadd4afd001754aea8.mockapi.io/tokens'

	def get_all(self):
		result = requests.get(self.endpoint)
		if result.status_code == 200:
			return True, result.json()
		return False, None

	def generate_token(self, agent):
		token = secrets.token_hex(20)
		result = requests.post(self.endpoint, data = {'agente': agent , 'token': token})
		success = False
		if(result.status_code == 201):
			success = True
		return success, Token(agent,token).json()

	def verify_token(self, agent, token):
		success, tokens = self.get_all()
		if success:
			i = 0
			exists = False
			while i < len(tokens) and not exists:
				if(tokens[i]['agente'] == agent and tokens[i]['token'] == token):
					exists = True
				i = i + 1
			return success, exists
		return success, None