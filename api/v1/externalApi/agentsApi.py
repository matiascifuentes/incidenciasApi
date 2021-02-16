import requests
import json

class AgentsApi:

	def __init__(self):
		self.endpoint = 'https://60280ddadd4afd001754aea8.mockapi.io/agents'

	def create_agent(self,agent):
		success, exists = self.agent_exists(agent['nombre'])
		if success:
			if not exists:
				result = requests.post(self.endpoint, data = agent)
				if(result.status_code == 201):
					return True, 201
				return False, 502
			return False, 409
		return False, 502

	def get_all(self):
		result = requests.get(self.endpoint)
		if result.status_code == 200:
			return True, result.json()
		return False, None

	def verify_agent(self, agent):
		success, agents = self.get_all()
		if success:
			i = 0
			exists = False
			while i < len(agents) and not exists:
				if(agents[i]['nombre'] == agent['nombre'] and agents[i]['contrasena'] == agent['contrasena']):
					exists = True
				i = i + 1
			return success, exists
		return success, None

	def agent_exists(self, usuario):
		success, agents = self.get_all()
		if success:
			i = 0
			exists = False
			while i < len(agents) and not exists:
				if(agents[i]['nombre'] == usuario):
					exists = True
				i = i + 1
			return success, exists
		return success, None
