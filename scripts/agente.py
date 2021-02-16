import requests
from datetime import datetime
from random import seed
from random import randint
seed(1)

NUM_ISSUES = 20	#Cantidad de incidencias que se crearán

login_url = "http://localhost:8000/api/v1/agent/login"
issue_url = "http://localhost:8000/api/v1/issue"

usuario = {
	"nombre": "ejemplo@ejemplo.com",
	"contrasena": "12345"
}
headers = {}

try:
	response = requests.request("POST", login_url, headers=headers, json=usuario)
	if response.status_code == 201:
		print("Login: OK")
		datos = response.json()
		agente = datos['agente']
		token = datos['token']

		for i in range(0,NUM_ISSUES):
			now = datetime.now()
			fecha = now.strftime("%d-%m-%Y %H:%M:%S")
			
			datos = {
				"fecha": fecha,
				"titulo": "Incidencia " + str(randint(1,1000)),
				"descripcion": "Descripcion",
				"agente": usuario['nombre'],
				"token": token
			}
			headers = {}

			response = requests.request("POST", issue_url, headers=headers, json=datos)
			if response.status_code == 201:
				print("Issue " + str(i) + ": OK")
			else:
				print("Issue " + str(i) + ": FAILED - " + str(response.status_code))
	else:
		print("Login: FAILED")
		print(response.text)
except:
	print("Error al conectarse a la API")

