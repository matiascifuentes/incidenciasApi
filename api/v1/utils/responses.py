from flask import jsonify
from utils.responseHeader import ResponseHeader

def response(code, success, message, data = None):
	header = ResponseHeader(code, success, message).info()
	response = {
		'status': header
	}
	if data:
		response['data'] = data
	return jsonify(response), code, {'ContentType':'application/json'} 

def http_200(data):
	return response(200, True, "OK", data)

def http_201():
	return response(201, True, "Created")

def http_400():
	return response(400, False, "Bad request")

def http_401():
	return response(401, False, "Unauthorized")

def http_403():
	return response(403, False, "Forbidden")

def http_409():
	return response(409, False, "Conflict. Already exists")

def http_502():
	return response(502, False, "Bad Gateway")