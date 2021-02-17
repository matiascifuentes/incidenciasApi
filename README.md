# API INCIDENCIAS

## API

### Pre-requisitos
	* Docker instalado y ejecutandose

### Instalación

	Para crear una imagen a partir del archivo Dockerfile se debe ejecutar en la raíz de la carpeta 'incidenciasApi' la siguiente instrucción:

		docker build -t incidencias .


	Para ejecutar el contenedor con la imagen creada se debe ejecutar el siguiente comando:

		docker run -it --publish 8000:4000 incidencias


	Una vez desplegada se puede acceder a la api mediante el dominio http://localhost:8000
	
## Script

	Inserta 10 incidencias en la base de datos

### Pre-requisitos
	* API ejecutandose
	* Abrir otra terminal
	* El usuario utilizado es ejemplo@ejemplo.com con contraseña 12345, el cual debe existir en la base de datos

### Ejecución

#### En caso de tener instalado python3 y la biblioteca requests
	Acceder a la carpeta scripts y ejecutar la instrucción:
	
		python agente.py
	

#### En caso contrario utilizar entorno virtual
	Acceder a la carpeta venv/Scripts y ejecutar:

		activate.bat
	

	Volver a la carpeta raíz de incidenciasApi y acceder a la carpeta scripts, ejecutar:
	
		python agente.py
