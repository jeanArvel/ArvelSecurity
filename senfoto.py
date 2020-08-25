import time
import picamera
import os
import requests
hora = time.strftime("%H:%M:%S")
fecha = time.strftime("%d-%m-%y")
namefoto = "foto:" +fecha+"-"+hora+".png"
foto = "/home/pi/Desktop/cookie/"+namefoto
iFTTTMakerSecretKey = "fhENYLysxNY7P-3fl5qCInsEilgv_SH6TjcpGMVjvWP"
# configurar la cara
#hacer cuando este lista
with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.capture(foto)

os.system('/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload '+foto+' /ArvelSecurity')
iFTTTSunRiseURL = "https://maker.ifttt.com/trigger/delantero/with/key/" + iFTTTMakerSecretKey
print ("SunRise is here!")
r = requests.get(iFTTTSunRiseURL)
print ("The resulting HTTP GET status code was " + str(r.status_code))
