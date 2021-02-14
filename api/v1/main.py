from flask import Flask
from flask import jsonify
from flask import request
import requests
from externalApi.issuesApi import IssuesApi
from externalApi.agentsApi import AgentsApi
from externalApi.tokensApi import TokensApi
app = Flask(__name__)

@app.route('/api/v1/agents', methods=['POST'])
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
    if not request.json or not 'fecha' in request.json or not 'titulo' in request.json or not 'descripcion' in request.json or not 'agente' in request.json or not 'token' in request.json:
        return jsonify({'error': "Bad request"}), 400
    issue = {
        'fecha': request.json['fecha'],
        'titulo': request.json['titulo'],
        'descripcion': request.json['descripcion'],
        'agente': request.json['agente']
    }
    tokensApi = TokensApi()
    correctToken = tokensApi.verify_token(request.json['agente'], request.json['token'])
    if correctToken:
    	issueApi = IssuesApi()
    	result = issueApi.create_issue(issue)
    	if result.status_code == 201:
	    	return jsonify({'issue': issue}), 201
    	return jsonify({'error': result.reason}), result.status_code
    return jsonify({'error': "Acceso denegado"}), 401

@app.route('/api/v1/issues', methods=['GET'])
def get_issues():
    issuesApi = IssuesApi()
    issues = issuesApi.get_all()
    return jsonify({'issues': issues })

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
    app.run(debug=True)