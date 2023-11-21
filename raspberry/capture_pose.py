from picamera2 import Picamera2, Preview
from time import sleep
import requests
camera = Picamera2()
camera.configure()

import requests

#camera.start_preview(Preview.QTGL)
#camera start
camera.start()
sleep(1)
#capture image

while True:
    img = camera.capture_file(f'./capture_pose.jpg')
    sleep(1)


    #camera.stop_preview()

    '''
    #upload image

    f = {'image': open('capture_pose.jpg', 'rb')}
    r = requests.post('http://127.0.0.1:8888/file',files=f)
    print("img##")
    print(r.json())
    '''

    f = {'image': open('capture_pose.jpg', 'rb')}
    #r = requests.get('http://192.168.0.132:8888/ps')
    r = requests.post('http://192.168.0.132:5000/file',files=f)
    print(r)
    type(r)
    if r.status_code ==200:
        print('success')
    else:
        print('fail')
    print(r.json())
    sleep(5)

camera.stop()
