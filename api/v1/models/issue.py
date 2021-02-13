class Issue:

	def __init__(self, fecha, titulo, descripcion, agente):
		self.fecha = fecha
		self.titulo = titulo
		self.descripcion = descripcion
		self.agente = agente

	def json(self):
		return{
			'fecha': self.fecha,
			'titulo': self.titulo,
			'descripcion': self.descripcion,
			'agente': self.agente
		}