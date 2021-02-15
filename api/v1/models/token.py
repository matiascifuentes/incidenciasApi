class Token:

	def __init__(self, agente, token):
		self.agente = agente
		self.token = token

	def json(self):
		return{
			'agente': self.agente,
			'token': self.token
		}