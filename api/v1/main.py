from flask import Flask
from flask import jsonify
from flask import request
import requests
from externalApi.issuesApi import IssuesApi
from externalApi.agentsApi import AgentsApi
app = Flask(__name__)

@app.route('/api/v1/agents', methods=['POST'])
def create_agent():
    if not request.json or not 'nombre' in request.json or not 'contrasena' in request.json:
        abort(400)
    agent = {
        'nombre': request.json['nombre'],
        'contrasena': request.json['contrasena']
    }
    agentsApi = AgentsApi()
    result = agentsApi.create_agent(agent)
    if result.status_code == 201:
    	return jsonify({'agent': agent}), 201
    return jsonify({'error': result.reason}), result.status_code

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