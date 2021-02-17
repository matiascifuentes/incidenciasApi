# API INCIDENCIAS

## API

### Pre-requisitos
	_Docker instalado y ejecutandose_

### Instalación

	_Para crear una imagen a partir del archivo Dockerfile se debe ejecutar en la raíz de la carpeta 'incidenciasApi' la siguiente instrucción:_
	```
		docker build -t incidencias .
	```

	_Para ejecutar el contenedor con la imagen creada se debe ejecutar el siguiente comando:_
	```
		docker run -it --publish 8000:4000 incidencias
	```

	_Una vez desplegada se puede acceder a la api mediante el dominio http://localhost:8000_
	
## Script

	_Inserta 10 incidencias en la base de datos_

### Pre-requisitos
	_API ejecutandose_
	_Abrir otra terminal_
	_El usuario utilizado es ejemplo@ejemplo.com con contraseña 12345, el cual debe existir en la base de datos_

### Ejecución

#### En caso de tener instalado python3 y la biblioteca requests
	_Acceder a la carpeta scripts y ejecutar la instrucción:_
	```
		python agente.py
	```

#### En caso contrario utilizar entorno virtual
	_Acceder a la carpeta venv/Scripts y ejecutar:_
	```
		activate.bat
	```

	_Volver a la carpeta raíz de incidenciasApi y acceder a la carpeta scripts, ejecutar:_
	```
		python agente.py
	```
