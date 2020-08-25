import time
import picamera
hora = time.strftime("%H:%M:%S")
fecha = time.strftime("%d-%m-%y")
namefoto = "foto:" +fecha+"-"+hora+".png"
foto = "/home/pi/Desktop/cookie/"+namefoto
# configurar la cara
#hacer cuando este lista
with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.capture(foto)
