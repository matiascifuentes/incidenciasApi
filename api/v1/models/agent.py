class Agent:

	def __init__(self, nombre, contrasena):
		self.nombre = nombre
		self.contrasena = contrasena

	def json(self):
		return{
			'nombre': self.nombre,
			'contrasena': self.contrasena
		}