# Importar los modulos GPIO para controlar los pines del Raspberry pi
import RPi.GPIO as GPIO
# Configurar el pines deseados con numeracion del esquema
GPIO.setmode(GPIO.BCM)
# numeracion de los pins pin numbering based on the BCM scheme
# Configurar las direciones de los GPIO pins ya sean INPUT(entrada) o OUTPUT(salida)
GPIO.setup(17, GPIO.IN)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
# Definimos la variable local en python la cual mantendra la llavede autentificacion del API:
sparkAuthorizationKey = 'Bearer MDlmNDQ0MjctNDFkMS00ODllLTlkNzYtMmE0Mjc4YjA2ZGNjMjJmNDY5MmEtYzM3'
import requests
import json
import time
# Usando las bibliotecas de solicitud , se crea un nueva solicitud HTTP GET hacia el punto final de Spark Api 
# el objeto local "r" mantendra los datos devueltos:
r = requests.get( "https://api.ciscospark.com/v1/rooms",
headers={'Authorization':sparkAuthorizationKey}
)
# Comprobar si la respuesta desde la APi llamada es correcta (resp. code 200)
if(r.status_code != 200):
    print("Something wrong has happened:")
    print("ERROR CODE: {} \nRESPONSE: {}".format(r.status_code, r.text))
    assert()
# Reemplazar de esta variable con el verdadero nombre del espacio creado en tu cuenta de Cisco Spark
roomNameToSearch = 'ArvelSecurity'
# Definimos una variable que mantendra el roomID
roomIdToMessage = None
rooms = r.json()['items']
for room in rooms:
    #print "Room name: '" + room['title'] + "' ID: " + room['id']
    if(room['title'].find(roomNameToSearch) != -1):
        roomIdToMessage = room['id']
        roomTitleToMessage = room['title']
        break
lastMessageId = None
flag = None
while True:
    # el codigo no debe golpear los servicios API con muchas solicitudes en un corto tiempo
    # para limitar en lumero de solicitudes en el bucle WHILE, comenzaremos con un 1 segundo de retraso:
    time.sleep(0.5)
    print("La siguiente iteracion esta empezando ...")
    # definimos los parametro obligatorios y opcionales GET para los mensajes del punto de salida del API:
    getMessagesUrlParameters = {# parametro obligatorio - the room ID
        "roomId": roomIdToMessage,
        # parametro opcional - numero de los ultimos mensajes a devolver
        # solo estamos interesados en el ultimo parametro del grupo
        # por lo tanto el maximo sera max = 1
        "max": 1
        }
    # Usando las bibliotecas de solicitud , se crea un nueva solicitud HTTP GET hacia el punto final de Spark Api 
    # el objeto local "r" mantendra los datos devueltos:
    r = requests.get( "https://api.ciscospark.com/v1/messages",
                      params=getMessagesUrlParameters,
                      headers={'Authorization':sparkAuthorizationKey}
                      )
    if(r.status_code != 200):
        print("Something wrong has happened:")
        print("ERROR CODE: {} \nRESPONSE: {}".format(r.status_code, r.text))
        assert()
    # Guardamos los datos json desde la respuesta
    jsonData = r.json()
    # Obtenemos los items (array of messages) desde jsonData.
    messages = jsonData['items']
    # desde la solicitud especificamos maximo 1 por lo que solo un mensaje deve retornar:
    message = messages[0]
    # Verificar si hay un mensaje nuevo:
    if(lastMessageId == message['id']):
        #si el semsaje es igual al anterior , no hay nuevos mensajes
        print("No hay mensajes nuevos.")
    else:
        # hay un nuevo mensaje ,este ID es diferente desde el ultimo ne la iteraccion previa
        print("mensaje nuevo: " + message['text'])
        # Guardar el id del mensaje para la siguiente iteraccion:
        lastMessageId = message['id']
        if(message['text'] == 'activar'):
            messageId = message['id']
            print("Se activo el sistema ArvelSecurity")
            flag = 1
            # Se enciende el LED:
            GPIO.output(6, True)
            GPIO.output(5, False)
            #break
        if(message['text'] == 'desactivar'):
            messageId = message['id']
            print("Se desactivo el sistema ArvelSecurity")
            flag = 0
            # Se enciende el LED:
            GPIO.output(5, True)
            GPIO.output(6, False)
            #break  
    while (flag == 1):
        # el codigo no debe golpear los servicios API con muchas solicitudes en un corto tiempo
        # para limitar en lumero de solicitudes en el bucle WHILE, comenzaremos con un 1 segundo de retraso:
        time.sleep(0.5)
        print("La siguiente iteracion esta empezando ...")
        # definimos los parametro obligatorios y opcionales GET para los mensajes del punto de salida del API:
        getMessagesUrlParameters = {# parametro obligatorio - the room ID
            "roomId": roomIdToMessage,
            # parametro opcional - numero de los ultimos mensajes a devolver
            # solo estamos interesados en el ultimo parametro del grupo
            # por lo tanto el maximo sera max = 1
            "max": 1
            }
        # Usando las bibliotecas de solicitud , se crea un nueva solicitud HTTP GET hacia el punto final de Spark Api 
        # el objeto local "r" mantendra los datos devueltos:
        r = requests.get( "https://api.ciscospark.com/v1/messages",
                          params=getMessagesUrlParameters,
                          headers={'Authorization':sparkAuthorizationKey}
                          )
        if(r.status_code != 200):
            print("Something wrong has happened:")
            print("ERROR CODE: {} \nRESPONSE: {}".format(r.status_code, r.text))
            assert()
        # Guardamos los datos json desde la respuesta
        jsonData = r.json()
        # Obtenemos los items (array of messages) desde jsonData.
        messages = jsonData['items']
        # desde la solicitud especificamos maximo 1 por lo que solo un mensaje deve retornar:
        message = messages[0]
        # Verificar si hay un mensaje nuevo:
        if(lastMessageId == message['id']):
            #si el semsaje es igual al anterior , no hay nuevos mensajes
            print("No hay mensajes nuevos.")
        else:
            # hay un nuevo mensaje ,este ID es diferente desde el ultimo ne la iteraccion previa
            print("mensaje nuevo: " + message['text'])
            # Guardar el id del mensaje para la siguiente iteraccion:
            lastMessageId = message['id']
            if(message['text'] == 'desactivar'):
                messageId = message['id']
                print("Se desactivo el sistema ArvelSecurity")
                flag = 0
                # Se enciende el LED:
                GPIO.output(5, True)
                GPIO.output(6, False)
                #break
