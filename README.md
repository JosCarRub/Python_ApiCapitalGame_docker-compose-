# Python_ApiCapitalGame_docker-compose-
Juego desarrollado en Python que consiste en acertar capitales de una serie de países. Muestra una tabla clasificatoria de todos los usuarios que persiste gracias a un volumen. Toma datos de una Api y se puede ejecutar en la terminal mediante un docker-compose que conecta con una imagen de mysql que levanta un contenedor conectado con el de la aplicación.


PASOS PARA PODER JUGAR DESDE TU MÁQUINA:

1. Crea un directorio e introduce el archivo docker-compose.yml

2. Desde la terminal, dirigeté hacia el directorio creado en el paso 1 y ejecuta: docker-compose up -d (IMPORTANTE -d YA QUE SE EJECUTARÍA LA APLICACIÓN SIN PODER INTERACTUAR CON ELLA)
   
3. Posteriormente ejecuta el comando: docker exec -it python_app_capitales /bin/bash

4. Mediante el comando anterior estaremos dentro del contenedor de nuestra aplicación, donde ya podremos interacturar con la misma introduciendo: python main.py

5. Una vez culminada la ejecución de la aplicación, ejecuta "exit" para salir del contenedor y desarma el compose mediante el comando: docker-compose down

   * CONSIDERACIONES *

      Si existe algun problema tras ejecutar el compose comprueba que tanto el contenedor de mysql como el de la aplicación están corriendo        (docker compose ps). No debería existir ningún problema pero si el contenedor "mysql_basedatos_juego" no está corriendo arrancalo            mediante el comando: docker start mysql_basedatos_juego

     Ten en cuenta que el contenedor mysql_basedatos_juego está mapeado de la siguiente forma: "3307:3306" . Si existe algún problema de          conexión con la base de datos asegúrate de que tu máquina tiene libre el puerto 3307 (De hecho que escuche por 3307 está hecho a             propósito para no coincidir con el puerto 3306, que es el puerto predeterminado de MySQL y podría estar siendo utilizado por otro            servicio o contenedor en tu sistema.

