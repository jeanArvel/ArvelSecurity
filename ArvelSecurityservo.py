import RPi.GPIO as GPIO
import time
import picamera
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(4, GPIO.IN)
GPIO.setup(3, GPIO.IN)
GPIO.setup(2, GPIO.IN)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
p = GPIO.PWM(13,50)
p.start(7.5)  
while True:
    sensordelantero = GPIO.input(22)
    capo = GPIO.input(27)
    puertapiloto = GPIO.input(17)
    puertacopiloto = GPIO.input(4)
    maletera = GPIO.input(3)
    sensortrasero = GPIO.input(2)
    if(sensordelantero == False):
        p.ChangeDutyCycle(3)    
        time.sleep(0.5)
        GPIO.output(6, True)
        print("Se detecto impacto en la parte delantera ----> "+str(sensordelantero))
        with picamera.PiCamera() as camera:
            camera.resolution = (1280,720)
            camera.capture("/home/pi/Desktop/cookie/newimage.png")
        time.sleep(0.5)
    elif(capo == False):
        p.ChangeDutyCycle(3)   #Enviamos un pulso del 10.5% para girar el servo hacia la derecha
        time.sleep(0.5)  
        GPIO.output(6, True)
        print("Se detecto anomalia en el capo ----> "+str(capo))
        with picamera.PiCamera() as camera:
            camera.resolution = (1280,720)
            camera.capture("/home/pi/Desktop/cookie/newimage.png")
        time.sleep(0.5)
    elif(puertapiloto == False):
        p.ChangeDutyCycle(7)   #Enviamos un pulso del 10.5% para girar el servo hacia la derecha
        time.sleep(0.5)  
        GPIO.output(6, True)
        print("Se detecto anomalia en la puerte del piloto ----> "+str(puertapiloto))
        with picamera.PiCamera() as camera:
            camera.resolution = (1280,720)
            camera.capture("/home/pi/Desktop/cookie/newimage.png")
        time.sleep(0.5)
    elif(puertacopiloto == False):
        p.ChangeDutyCycle(7)   #Enviamos un pulso del 10.5% para girar el servo hacia la derecha
        time.sleep(0.5) 
        GPIO.output(6, True)
        print("Se detecto anomalia en la puerte del copiloto ----> "+str(puertacopiloto))
        with picamera.PiCamera() as camera:
            camera.resolution = (1280,720)
            camera.capture("/home/pi/Desktop/cookie/newimage.png")
        time.sleep(0.5)
    elif(maletera == False):
        p.ChangeDutyCycle(11)   #Enviamos un pulso del 10.5% para girar el servo hacia la derecha
        time.sleep(0.5) 
        GPIO.output(6, True)
        print("Se detecto anomalia en la maletera ----> "+str(maletera))
        with picamera.PiCamera() as camera:
            camera.resolution = (1280,720)
            camera.capture("/home/pi/Desktop/cookie/newimage.png")
        time.sleep(0.5)
    elif(sensortrasero == False):
        p.ChangeDutyCycle(11)   #Enviamos un pulso del 10.5% para girar el servo hacia la derecha
        time.sleep(0.5) 
        GPIO.output(6, True)
        print("Se detecto impacto en la parte trasera ----> "+str(sensortrasero))
        with picamera.PiCamera() as camera:
            camera.resolution = (1280,720)
            camera.capture("/home/pi/Desktop/cookie/newimage.png")
        time.sleep(0.5)
    else:
        GPIO.output(6, False)

    
