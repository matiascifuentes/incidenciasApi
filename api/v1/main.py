from flask import Flask
from flask import jsonify
from flask import request
import requests
from models.agent import Agent
from models.issue import Issue
from externalApi.issuesApi import IssuesApi
from externalApi.agentsApi import AgentsApi
from externalApi.tokensApi import TokensApi
from utils.responses import http_200, http_201, http_400, http_401, http_403, http_409, http_500, http_502
app = Flask(__name__)

@app.route('/api/v1/agent/login', methods=['POST'])
def login():
	'Genera un token de acceso si las credenciales existen'
	try:
	    if not request.json or not 'nombre' in request.json or not 'contrasena' in request.json:
	        return http_400() 
	    agent = Agent(request.json['nombre'], request.json['contrasena']).json()
	    isValidAgent = AgentsApi().verify_agent(agent)
	    if isValidAgent:
	    	success, token = TokensApi().generate_token(agent['nombre'])
	    	if success:
	    		return http_200(token)
	    	return http_502()
	    return http_403()
	except:
		return http_500()

@app.route('/api/v1/agent', methods=['POST'])
def create_agent():
    if not request.json or not 'nombre' in request.json or not 'contrasena' in request.json:
        return jsonify({'error': "Bad request"}), 400
    agent = {
        'nombre': request.json['nombre'],
        'contrasena': request.json['contrasena']
    }
    agentsApi = AgentsApi()
    result = agentsApi.create_agent(agent)
    if result.status_code == 201:
    	return jsonify({'agent': agent}), 201
    return jsonify({'error': result.reason}), result.status_code

@app.route('/api/v1/issue', methods=['POST'])
def create_issue():
	'Crea una nueva issue en la base de datos, siempre que el token sea válido'
	try:
	    if not request.json or not 'fecha' in request.json or not 'titulo' in request.json or not 'descripcion' in request.json or not 'agente' in request.json or not 'token' in request.json:
	        return http_400()
	    issue = Issue(request.json['fecha'], request.json['titulo'], request.json['descripcion'], request.json['agente']).json()
	    isValidToken = TokensApi().verify_token(request.json['agente'], request.json['token'])
	    if isValidToken:
	    	success = IssuesApi().create_issue(issue)
	    	if success:
		    	return http_201(issue)
	    	return http_502()
	    return http_401()
	except:
		return http_500()

@app.route('/api/v1/issues', methods=['GET'])
def get_issues():
	'Obtiene todas las issue desde la base de datos'
	try:
		success, issues = IssuesApi().get_all()
		if success:
			return http_200(issues)
		return http_502()
	except:
		return http_500()

@app.route('/api/v1/issues/<user>/user', methods=['GET'])
def get_issues_for_user(user):
    issuesApi = IssuesApi()
    issues = issuesApi.get_for_user(user)
    return jsonify({'issues': issues })

@app.route('/api/v1/issues/<date>/date', methods=['GET'])
def get_issues_for_date(date):
    issuesApi = IssuesApi()
    issues = issuesApi.get_for_date(date)
    return jsonify({'issues': issues })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)