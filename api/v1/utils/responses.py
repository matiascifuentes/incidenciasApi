from flask import jsonify
from utils.responseHeader import ResponseHeader

def response(code, success, message):
	header = ResponseHeader(code, success, message)
	return jsonify(header.info), code, {'ContentType':'application/json'} 

def http_200():
	return response(200, True, "OK")

def http_400():
	return response(400, False, "Bad request")

def http_403():
	return response(403, False, "Forbidden")
