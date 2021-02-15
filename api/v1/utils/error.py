class Error:

	def __init__(self, code, reason, message):
		self.code = code
		self.reason = reason
		self.message = message

	def info(self):
		return{
			'error':{
				'code': self.code,
				'reason': self.reason,
				'message': self.message
			}
		}