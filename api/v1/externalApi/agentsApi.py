import requests
import json

class AgentsApi:

	def __init__(self):
		self.endpoint = 'https://60280ddadd4afd001754aea8.mockapi.io/agents'

	def create_agent(self,agent):
		result = requests.post(self.endpoint, data = agent)
		success = False
		if(result.status_code == 201):
			success = True
		return success

	def get_all(self):
		agents = requests.get(self.endpoint)
		return agents.json()

	def verify_agent(self, agent):
		agents = self.get_all()
		i = 0
		exits = False
		while i < len(agents) and not exits:
			if(agents[i]['nombre'] == agent['nombre'] and agents[i]['contrasena'] == agent['contrasena']):
				exits = True
			i = i + 1
		return exits