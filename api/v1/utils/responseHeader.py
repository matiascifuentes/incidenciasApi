class ResponseHeader:

	def __init__(self, code, success, message):
		self.code = code
		self.success = success
		self.message = message

	def info(self):
		return{
			'success': self.success,
			'code': self.code,
			'message': self.message
		}