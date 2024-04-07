from picamera import PiCamera
hqCamera = PiCamera(resolution=(1920, 1080), framerate=25)

from picamera import PiCamera
hqCamera = PiCamera()
hqCamera.resolution = (1920, 1080)
hqCamera.framerate = 25

from picamera import PiCamera
hqCamera = PiCamera()
#hqCamera.resolution = (1920, 1080)
hqCamera.resolution = (640, 480)
#hqCamera.framerate = 25
hqCamera.framerate = 20
hqCamera.start_recording('my_python_video.h264')
hqCamera.wait_recording(5)
hqCamera.stop_recording()
