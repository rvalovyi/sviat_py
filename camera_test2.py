
from picamera import PiCamera
import time
hqCamera = PiCamera()
hqCamera.resolution = (1920, 1080)
hqCamera.vflip = True 
hqCamera.start_preview()
time.sleep(5)
hqCamera.capture('my_python_image.jpg')