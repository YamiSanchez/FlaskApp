# FlaskApp
Primero se verifica si se tiene descargado python
Después se genera el ambiente virtual con el comando $ python3 -m venv env
Luego lo activamos con .\env\Scripts\activate
Instalamos flask dentro del ambiente: pip install flask
Desacargamos los archivos del repositorio 
Se ejecuta el archivo app.py con: run app docker run -it --publish 7000:5000 app.py
**Como el archivo app.py tiene especificado que imagen se usa de docker, al ejecutarlo descarga la isma imagen**
