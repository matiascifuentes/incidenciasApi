import requests
import json
import secrets

class TokensApi:

	def __init__(self):
		self.endpoint = 'https://60280ddadd4afd001754aea8.mockapi.io/tokens'

	def get_all(self):
		tokens = requests.get(self.endpoint)
		return tokens.json()

	def generate_token(self):
		return secrets.token_hex(20)

	def verify_token(self, agent, token):
		tokens = self.get_all()
		i = 0
		exits = False
		while i < len(tokens) and not exits:
			if(tokens[i]['agente'] == agent and tokens[i]['token'] == token):
				exits = True
			i = i + 1
		return exits