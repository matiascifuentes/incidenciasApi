import requests
import json
import secrets
from models.token import Token

class TokensApi:

	def __init__(self):
		self.endpoint = 'https://60280ddadd4afd001754aea8.mockapi.io/tokens'

	def get_all(self):
		tokens = requests.get(self.endpoint)
		return tokens.json()

	def generate_token(self, agent):
		token = secrets.token_hex(20)
		result = requests.post(self.endpoint, data = {'agente': agent , 'token': token})
		success = False
		if(result.status_code == 201):
			success = True
		return success, Token(agent,token).json()

	def verify_token(self, agent, token):
		tokens = self.get_all()
		i = 0
		exits = False
		while i < len(tokens) and not exits:
			if(tokens[i]['agente'] == agent and tokens[i]['token'] == token):
				exits = True
			i = i + 1
		return exits