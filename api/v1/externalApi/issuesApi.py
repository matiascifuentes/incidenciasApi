import requests
import json

class IssuesApi:

	def __init__(self):
		self.endpoint = 'https://60280ddadd4afd001754aea8.mockapi.io/'

	def get_all(self):
		issues = requests.get(self.endpoint + 'issues')
		return issues.json()

	def get_for_user(self,usuario):
		issues = self.get_all()
		result = []
		for issue in issues:
			if issue['agente'] == usuario:
				result.append(issue)
		return result
