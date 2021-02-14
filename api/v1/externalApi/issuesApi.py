import requests
import json

class IssuesApi:

	def __init__(self):
		self.endpoint = 'https://60280ddadd4afd001754aea8.mockapi.io/issues'

	def create_issue(self,issue):
		result = requests.post(self.endpoint, data = issue)
		return result

	def get_all(self):
		issues = requests.get(self.endpoint)
		return issues.json()

	def get_for_user(self,usuario):
		issues = self.get_all()
		result = []
		for issue in issues:
			if issue['agente'] == usuario:
				result.append(issue)
		return result

	def get_for_date(self,fecha):
		issues = self.get_all()
		result = []
		for issue in issues:
			date = issue['fecha'].split()
			if date[0] == fecha:
				result.append(issue)
		return result