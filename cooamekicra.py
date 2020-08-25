import picamera
import os

# configurar la cara
#hacer cuando este lista
with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.capture("/home/pi/Desktop/cookie/newimage3.png")

os.system('/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/Desktop/cookie/newimage3.png /ArvelSecurity')
