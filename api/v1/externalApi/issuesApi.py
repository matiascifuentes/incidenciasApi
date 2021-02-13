import requests

class IssuesApi:

	def __init__(self):
		self.endpoint = 'https://60280ddadd4afd001754aea8.mockapi.io/'

	def get_all(self):
		issues = requests.get(self.endpoint + 'issues')
		return issues.json()