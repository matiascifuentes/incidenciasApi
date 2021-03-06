from flask import jsonify
from utils.error import Error

def response(success, code, reason = None, message = None, data = None):
	response = {}
	if success:
		if data:
			response = data
	else:
		response = Error(code, reason, message).info()
	return jsonify(response), code, {'ContentType':'application/json'} 

def http_200(data):
	return response(True, 200, data = data)

def http_201(data):
	return response(True, 201, data = data)

def http_400():
	return response(False, 400, "Bad Request", "El cuerpo de la solicitud es incorrecto")

def http_401():
	return response(False, 401, "Unauthorized", "El token utilizado no es válido")

def http_403():
	return response(False, 403, "Forbidden", "Usuario o clave incorrecto")

def http_404():
	return response(False, 404, "Not Found", "El recurso solicitado no existe")

def http_405():
	return response(False, 405, "Method Not Allowed ", "El método no es permitido")

def http_409():
	return response(False, 409, "Conflict", "El registro ya existe")

def http_422():
	return response(False, 422, "Unprocessable Entity", "El formato de la fecha es incorrecto o no existe")

def http_500():
	return response(False, 500, "Internal Server Error", "Ha ocurrido un error inesperado en el servidor")

def http_502():
	return response(False, 502, "Bad Gateway", "Ha ocurrido un error al conectar a la base de datos")