import requests
import json

class AgentsApi:

	def __init__(self):
		self.endpoint = 'https://60280ddadd4afd001754aea8.mockapi.io/agents'

	def create_agent(self,agent):
		result = requests.post(self.endpoint, data = agent)
		return result

	def get_all(self):
		agents = requests.get(self.endpoint)
		return agents.json()
