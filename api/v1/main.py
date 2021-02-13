from flask import Flask
from flask import jsonify
import requests
from externalApi.issuesApi import IssuesApi
app = Flask(__name__)

issuesDB = 'https://60280ddadd4afd001754aea8.mockapi.io/issues'
agentsDB = 'https://60280ddadd4afd001754aea8.mockapi.io/agents'

@app.route('/api/v1/issues', methods=['GET'])
def get_issues():
    issuesApi = IssuesApi()
    issues = issuesApi.get_all()
    return jsonify({'issues': issues })

@app.route('/api/v1/issues/<user>', methods=['GET'])
def get_issues_for_user(user):
    issuesApi = IssuesApi()
    issues = issuesApi.get_for_user(user)
    return jsonify({'issues': issues })

if __name__ == '__main__':
    app.run(debug=True)