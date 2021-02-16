import requests
import time
from datetime import datetime
from random import seed
from random import randint
seed(1)

NUM_ISSUES = 10	#Cantidad de incidencias que se crearán

# mockAPI comienza a rechazar las peticiones, para reducir la cantidad de errores utilizo un tiempo de espera
WAIT_TIME = 1 #	Tiempo de espera en segundos

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
				"agente": usuario['nombre']
			}
			headers = {
				"token": token
			}

			time.sleep(WAIT_TIME)
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

