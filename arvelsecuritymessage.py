import RPi.GPIO as GPIO
import time
import picamera
import requests
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(4, GPIO.IN)
GPIO.setup(3, GPIO.IN)
GPIO.setup(2, GPIO.IN)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
iFTTTMakerSecretKey = "fhENYLysxNY7P-3fl5qCInsEilgv_SH6TjcpGMVjvWP"
iFTTTdelantero = "https://maker.ifttt.com/trigger/delantero/with/key/" + iFTTTMakerSecretKey
iFTTTcapo = "https://maker.ifttt.com/trigger/capo/with/key/" + iFTTTMakerSecretKey
iFTTTpiloto = "https://maker.ifttt.com/trigger/piloto/with/key/" + iFTTTMakerSecretKey
iFTTTcopiloto = "https://maker.ifttt.com/trigger/copiloto/with/key/" + iFTTTMakerSecretKey
iFTTTmaletera = "https://maker.ifttt.com/trigger/maletera/with/key/" + iFTTTMakerSecretKey
iFTTTtrasero = "https://maker.ifttt.com/trigger/trasero/with/key/" + iFTTTMakerSecretKey
while True:
    sensordelantero = GPIO.input(22)
    capo = GPIO.input(27)
    puertapiloto = GPIO.input(17)
    puertacopiloto = GPIO.input(4)
    maletera = GPIO.input(3)
    sensortrasero = GPIO.input(2)
    if(sensordelantero == False):        
        GPIO.output(6, True)
        print("Se detecto impacto en la parte delantera ----> "+str(sensordelantero))
        with picamera.PiCamera() as camera:
            camera.resolution = (1280,720)
            camera.capture("/home/pi/Desktop/cookie/newimage.png")
        time.sleep(0.5)
        r = requests.get(iFTTTdelantero)
        print ("The resulting HTTP GET status code was " + str(r.status_code))
    elif(capo == False):
        GPIO.output(6, True)
        print("Se detecto anomalia en el capo ----> "+str(capo))
        with picamera.PiCamera() as camera:
            camera.resolution = (1280,720)
            camera.capture("/home/pi/Desktop/cookie/newimage.png")
        time.sleep(0.5)
        r = requests.get(iFTTTcapo)
        print ("The resulting HTTP GET status code was " + str(r.status_code))
    elif(puertapiloto == False):
        GPIO.output(6, True)
        print("Se detecto anomalia en la puerte del piloto ----> "+str(puertapiloto))
        with picamera.PiCamera() as camera:
            camera.resolution = (1280,720)
            camera.capture("/home/pi/Desktop/cookie/newimage.png")
        time.sleep(0.5)
        r = requests.get(iFTTTpiloto)
        print ("The resulting HTTP GET status code was " + str(r.status_code))
    elif(puertacopiloto == False):
        GPIO.output(6, True)
        print("Se detecto anomalia en la puerte del copiloto ----> "+str(puertacopiloto))
        with picamera.PiCamera() as camera:
            camera.resolution = (1280,720)
            camera.capture("/home/pi/Desktop/cookie/newimage.png")
        time.sleep(0.5)
        r = requests.get(iFTTTcopiloto)
        print ("The resulting HTTP GET status code was " + str(r.status_code))
    elif(maletera == False):
        GPIO.output(6, True)
        print("Se detecto anomalia en la maletera ----> "+str(maletera))
        with picamera.PiCamera() as camera:
            camera.resolution = (1280,720)
            camera.capture("/home/pi/Desktop/cookie/newimage.png")
        time.sleep(0.5)
        r = requests.get(iFTTTmaletera)
        print ("The resulting HTTP GET status code was " + str(r.status_code))
    elif(sensortrasero == False):
        GPIO.output(6, True)
        print("Se detecto impacto en la parte trasera ----> "+str(sensortrasero))
        with picamera.PiCamera() as camera:
            camera.resolution = (1280,720)
            camera.capture("/home/pi/Desktop/cookie/newimage.png")
        time.sleep(0.5)
        r = requests.get(iFTTTtrasero)
        print ("The resulting HTTP GET status code was " + str(r.status_code))
    else:
        GPIO.output(6, False)


