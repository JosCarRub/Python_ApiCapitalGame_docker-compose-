import requests
import json
import random
import time
import os
from mysql.connector import Error

import mysql.connector
from colorama import Fore, Style, init

init()

try:
   

    # URL de la API 
    url = "https://restcountries.com/v3.1/region/europe?lang=es" # Endpoint que me da países de europa

    # PETICIÓN GET A LA URL LA CUAL METO EN UN VAR LLAMADA RESPONSE
    response = requests.get(url)


    dicPaisesCapitalesEuropa = {} # DICCIONARIO VACÍO DONDE GUARDARÉ LOS ELEMENTOS QUE YO ELIJA

    listaCapitalesEspañol = []    # LISTA DONDE GUARDARÉ LAS CAPITALES LIMPIAS Y TRADUCIDAS PROVENIENTES DEL ARCHIVO .TXT


    # SI ES EXITOSA...
    if response.status_code == 200:
        # Carga los datos JSON
        datos = response.json()


        for i in datos: # Itero en la response para guardar en variables lo que quiero

            nombrePais = i.get("translations", {}).get("spa", {}).get("common") # Me aparecen muchos nombres solo quiero el common y en español
            capitalPais = i.get("capital") [0] # Si no pongo el indice primero me sale en formato lista y así no lo quiero // NO LA HAY EN ESPAÑOL

            

            dicPaisesCapitalesEuropa [nombrePais] = [capitalPais]
        
        

            #TRAMPA PARA DOCKER
        archivoCapitalesLimpio = "['Oslo', 'Atenas', 'Mariehamn', 'Berna', 'Zagreb', 'Reikiavik', 'Luxemburgo', 'Budapest', 'Ámsterdam', 'Vilnius', 'Bratislava', 'Vaduz', 'Chisináu', 'Roma', 'Saint Helier', 'Mónaco', 'Minsk', 'Riga', 'Andorra la Vieja', 'París', 'Gibraltar', 'Copenhague', 'Skopje', 'La Valeta', 'Praga', 'Saint Peter Port', 'Pristina', 'Longyearbyen', 'Podgorica', 'Tórshavn', 'Tirana', 'Belgrado', 'Kiev', 'Douglas', 'Tallin', 'Bucarest', 'Sofía', 'Berlín', 'Varsovia', 'Londres', 'Helsinki', 'Estocolmo', 'Ciudad del Vaticano', 'Moscú', 'Viena', 'Nicosia', 'Lisboa', 'Sarajevo', 'Bruselas', 'Madrid', 'Liubliana', 'San Marino', 'Dublín']"
        archivoCapitalesLimpio = archivoCapitalesLimpio.strip().replace("'","").replace("[","").replace("]","").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u") # LO LIMPIO COMO UNA CADENA
                
        listaCapitalesEspañol = archivoCapitalesLimpio.split(",") #SEPARA EL ARCHIVO EN CADENAS CON LA COMA COMO SEPARADOR

        # Creo un diccionario nuevo con capitales en inglés y capitales en español
        for i, capitalEspañol in enumerate(listaCapitalesEspañol):
            if i < len(dicPaisesCapitalesEuropa):  # Asegurarse de no pasarse 
                pais = list(dicPaisesCapitalesEuropa.keys())[i]  # Obtener pais
                dicPaisesCapitalesEuropa[pais] = capitalEspañol.strip()  # Reemplazar la capital por la española

            
        print(f"{Fore.CYAN}JUEGO CAPITALES EN PYTHON REALIZADO POR JOSÉ CARLOS VERSION BETA{Fore.RESET}")
        sky = (                        
    "           .      *       *   .     .          *       .     .       *        .      *       *   .     .          *       .     .     \n"
    "       .      .       *       .     *  .      *        *     *            .  *   .       *       .     *  .      *        *     *      \n"
    "           .      *     .   *   .   .      .          .     .       .        .      *     .   *   .   .      .   *       .     .     \n"
    "       .      .       *       .  *     .      *        *     *          *  .      .       *       .  *     .      *        *     *      \n"
    "          .       .     *  .      .      *     .     *    .      *      .     .       .     *  .      .      *     .     *    .         \n"
    "          .      *          .      *         .     *        .      .           .      *          .      *         .     *        .        \n"
    "           .     *  .      .           .         .      *            .       .     *  .      .      *     .     *    .      *         \n"
    "           .     *  .      .      *     .     *    .      *    *   .           .     *  .      .      *     .     *    .      *         \n"
    "      .      *   .      *   .               .         *     .        *   .      *   .      *   .       *        .         *     .      \n"
    "          *       *  .         .      *     .      *      .         .          *       *  .         .      *     .      *      .          \n"
    "       .      .     *      *   .         *       .       *   .  *          .      .     *      *   .         *       .       *   .      \n"
    "           *      .      *         *     .        *    .                      *      .      *         *     .        *    .           \n"
    "       .      *     *      .    *    .         *         *   .        *     .      *     *      .    *    .         *         *   .       \n"
    "          .     *        .        .     *      *     .      *       .           .     *        .        .     *      *     .      *         \n"
    "       .       *     *     .       *     .          .     *      .      *   .       *     *     .       *     .          .     *      \n"
    "          *         .        *       .      *     *   .       *        .       *         .        *       .      *     *   .  *           \n"
    "       .      *       *  .      *        .        .     *   .       .       .      *       *  .      *        .        .     *   .        \n"
)
    
    def print_sky_with_stars(sky):
        for line in sky.splitlines():
            colored_line = ''
            for char in line:
                if char == '*':
                    if random.random() < 0.08:
                        colored_line += Fore.YELLOW + '*' + Style.RESET_ALL
                    elif random.random() < 0.05:
                        colored_line += Fore.CYAN + '*' + Style.RESET_ALL
                    else:
                        colored_line += '*'
                else:
                    colored_line += char
            print(colored_line)
            time.sleep(0.3)  


    print_sky_with_stars(sky)
                
        

    print(f"""{Fore.GREEN}
                       ██████╗ █████╗ ██████╗ ██╗████████╗ █████╗ ██╗     ███████╗███████╗                      
         ██╗██╗██╗    ██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝██╔══██╗██║     ██╔════╝██╔════╝    ██╗██╗██╗         
         ╚═╝╚═╝╚═╝    ██║     ███████║██████╔╝██║   ██║   ███████║██║     █████╗  ███████╗    ╚═╝╚═╝╚═╝         
         ██╗██╗██╗    ██║     ██╔══██║██╔═══╝ ██║   ██║   ██╔══██║██║     ██╔══╝  ╚════██║    ██╗██╗██╗         
██╗██╗██╗╚═╝╚═╝╚═╝    ╚██████╗██║  ██║██║     ██║   ██║   ██║  ██║███████╗███████╗███████║    ╚═╝╚═╝╚═╝██╗██╗██╗
    {Fore.RESET}""")
    print(f"\nEl juego consiste en introducir la capital del país que te aparezca en la imagen\n")
    print(f"\nTu puntuación quedará guardada en una Base de Datos y podrás consultar tu posición en la tabla clasificatoria\n")
    print("\n\nEn la versión Beta solo están disponibles los países europeos\n\n")
    print(f"\n\nLa puntuación máxima son {Fore.LIGHTGREEN_EX}15 puntos{Fore.RESET}\n\n")


    numRandom = int((random.random())*len(dicPaisesCapitalesEuropa)+1) # LO CASTEO A INT Y COMO DA UN NUMERO ENTRE 0.0 Y 1.0 EXCLUYENDO EL 1.0 LO MULTIPLICO POR LO QUE MIDE EL DICCIONARIO +1

    booCapitales = True # CONDICION DEL WHILE PARA EL JUEGO
    listaPaisesJuego = list(dicPaisesCapitalesEuropa.keys()) # LISTA QUE CONTIENE LAS CLAVES DEL DIC PARA MEDIANTE NUMRANDOM ME DÉ INDICES ALEATORIOS


    # MECÁNICA DEL JUEGO
    while booCapitales:
            
            try:    
                numJugadores = int(input("\n\n¿Cuantos jugadores vais a jugar?\n"))

                if numJugadores == 1:
                    
                    print(f"\n\n{Fore.YELLOW}NO ES SENSIBLE A MAYÚSCULAS Y DEBES INTRODUCIR LA CAPITAL SIN ACENTOS{Fore.RESET}\n\n")
                    print("ADELANTE!")
                    contadorIntentos = 0
                    aciertos = 0
                    fallos = 0

                    while contadorIntentos <= 14:
                        
                        numRandom = int((random.random())*len(dicPaisesCapitalesEuropa)-1) # LO CASTEO A INT Y COMO DA UN NUMERO ENTRE 0.0 Y 1.0 EXCLUYENDO EL 1.0 LO MULTIPLICO POR LO QUE MIDE EL DICCIONARIO -1
                        paisRandom = listaPaisesJuego[numRandom]
                        introCapital = input((f"Dime la capital de {paisRandom}:\n"))

                        if introCapital.lower() == dicPaisesCapitalesEuropa.get(paisRandom,introCapital).lower():
                            print(f"{Fore.GREEN}CORRECTO!{Fore.RESET}\n")
                            contadorIntentos +=1
                            aciertos +=1
                        else:
                            print(f"\n{Fore.RED}ERROR{Fore.RESET}\n")                  # PISTA PRIMERA LETRA print(f"La capital de {paisRandom} es {dicPaisesCapitalesEuropa[paisRandom][0]}
                            print(f"La capital de {paisRandom} es {dicPaisesCapitalesEuropa[paisRandom]}") 
                            contadorIntentos +=1
                            fallos +=1

                    regNombre = input("Introduce tu nombre para guardar tus resultados: \n")
                    print(f"RESULTADO:\n\n{aciertos} ACIERTOS\n\n{fallos} FALLOS")
                    booCapitales = False



                #OPCIONES PARA LOS DOS YA QUE HAY QUE TENER EN CUENTA ACIERTOS/FALLOS Y CONTADORES DE LOS 2 JUAGADORES
                elif numJugadores == 2:
                    print("NO DISPONIBLE EL MODO UN JUGADOR EN LA VERSION BETA")                
                else:
                    print(f"\nMáximo 2 jugadores\n")

            except ValueError:
                print(f"\n{Fore.RED}Debes introducir un NÚMERO{Fore.RESET}\n")
    else:   # ERRORES EN LA RESPONSE Y RESPUESTA SEGÚN ERROR...
        if response.status_code == 403:
            print("Es probable que necesites una clave para acceder a la API")
        elif response.status_code == 404:
            print("Es probable que no estes apuntando a la ruta correcta")
        elif response.status_code == 500:
            print(f"Es probable que exista un problema interno en el servidor")
        # else:
           # print(f"Error al obtener los datos: {response.status_code}")   ME SALTA SI PONGO LA CONEXION ABAJO UN 200 RESULTADO DE LA CONEXIÓN EXITOSA, LO PONGO AHHI POR QUE QUIERO QUE LA BD SE CREE NUEVA
           # POR QUE QUIERO DOCKERIZAR LA APP Y QUE SE CREE LA BD EN EL CONTENEDOR, SI LA PONGO ANTES ME DARÁ FALLOS DE CONEXIÓN SUPONGO



        #CONEXION BBDD
        db_config = {
            'host': os.getenv('MYSQL_HOST', 'db'),
            'user': os.getenv('MYSQL_USER', 'root'),
            'password': os.getenv('MYSQL_PASSWORD', '1234'),
            'database': os.getenv('MYSQL_DATABASE', 'CAPITAL_PLAY')
        }
        connection = None
        while connection is None:
            try:
                print("Intentando conectar a la base de datos...")
                connection = mysql.connector.connect(**db_config)
                print("Conexión exitosa a la base de datos.")
            except Error as e:
                print(f"Error: {e}")
                time.sleep(5)

        if connection.is_connected():
            

        # Crear un cursor para ejecutar consultas
            bd = connection.cursor()

            bd.execute("CREATE DATABASE IF NOT EXISTS PYTHON_CAPITAL_GAME;")

            bd.execute("USE PYTHON_CAPITAL_GAME;")

            bd.execute( "CREATE TABLE IF NOT EXISTS LEADERBOARD (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, points INT NOT NULL);")
        
            insertarJugador = ("INSERT INTO LEADERBOARD (name, points) VALUES (%s , %s);")
            datosJugador = (regNombre, aciertos)

            showTableJugador = ("SELECT ID, name, points FROM LEADERBOARD ORDER BY points DESC;")

            bd.execute(insertarJugador,datosJugador)
            connection.commit()  



        getLeaderBoard = input("¿Quieres ver la tabla clasificatoria? ")
        if getLeaderBoard.lower() == "si":
            bd.execute(showTableJugador)

            resultados = bd.fetchall()
            print("\n" + "-" * 60)  # Línea separadora para mejor visualización
            print(f"{'ID':<10} | {'PLAYER':<20} | {'POINTS':<10}")
            print("-" * 60)  # Línea separadora    
            for fila in resultados:
                print(f"{fila[0]:<10} | {fila[1]:<20} | {fila[2]:<10}") 
            print("-" * 60)  # Línea separadora al final
        else:
            print(":(")






except SystemError as e:
    print(f"{Fore.RED}Error al conectar con la Base de Datos:{Fore.RESET} {e}")

finally:
    if connection and connection.is_connected():
        bd.close()
        connection.close()
        print("La conexión MySQL ha sido cerrada\n")
        print("FIN DEL JUEGO CAPITALES V.BETA")
        print("PERMANECE ATENTO A POSTERIORES AJUSTES DE LA APLICACIÓN")
        ascii_art = r"""
          __ooooooooo__
              oOOOOOOOOOOOOOOOOOOOOOo
          oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
       oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
     oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
   oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
  oOOOOOOOOOOO*  *OOOOOOOOOOOOOO*  *OOOOOOOOOOOOo
 oOOOOOOOOOOO      OOOOOOOOOOOO      OOOOOOOOOOOOo
 oOOOOOOOOOOOOo  oOOOOOOOOOOOOOOo  oOOOOOOOOOOOOOo
oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
oOOOO     OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO     OOOOo
oOOOOOO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOo
 *OOOOO  OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  OOOOO*
 *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
  *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
   *OOOOOOo  *OOOOOOOOOOOOOOOOOOOOOOO*  oOOOOOO*
     *OOOOOOOo  *OOOOOOOOOOOOOOOOO*  oOOOOOOO*
       *OOOOOOOOo  *OOOOOOOOOOO*  oOOOOOOOO*      
          *OOOOOOOOo           oOOOOOOOO*      
              *OOOOOOOOOOOOOOOOOOOOO*          
                   ""ooooooooo""                  
"""

print(ascii_art)
