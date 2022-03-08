import face_recognition
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import RPi.GPIO as GPIO
import datetime
import time

#settings: GPIOs
print('Started: settings GPIOs')
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.HIGH)

#settings: Camera
print('Started: settings Camera')
name = 'EXAMPLE' #replace with your name
cam = PiCamera()
cam.resolution = (1408, 1008)
cam.framerate = 10
#that was at the beginnning rawCapture = PiRGBArray(cam, size=(512, 304))
rawCapture = PiRGBArray(cam, size=(1408, 1008))
img_counter = 0

#settings: face models
print('Started: settings face models')
print('Started: reading imgs from files')
unknown_image = face_recognition.load_image_file("EXAMPLE.jpg")
kacper_image = face_recognition.load_image_file("Kacper.jpg")
pawel_image = face_recognition.load_image_file("Pawel.jpg")
piotr_image = face_recognition.load_image_file("Piotr.jpg")
damian_image = face_recognition.load_image_file("Damian.jpg")
emilk_image = face_recognition.load_image_file("Emilk.jpg")
lukasz_image = face_recognition.load_image_file("Lukasz.jpg")
maciej_image = face_recognition.load_image_file("Maciej.jpg")
panpiotr_image = face_recognition.load_image_file("PanPiotr.jpg")
przemek_image = face_recognition.load_image_file("Przemek.jpg")
artur_image = face_recognition.load_image_file("Artur.jpg")
tomek_image = face_recognition.load_image_file("Tomek.jpg")
emil_image = face_recognition.load_image_file("Emil.jpg")
kuba_image = face_recognition.load_image_file("Kuba.jpg")
hubert_image = face_recognition.load_image_file("Hubert.jpg")

table = [
    'Kacper',
    'Pawel',
    'Piotr',
    'Damian',
    'EmilK',
    'Łukasz',
    'Maciej',
    'Pan Piotr',
    'Przemek',
    'Artur',
    'Tomek',
    'Emil',
    'Kuba',
    'Hubert'
]

print('Started: encodings(try)')
try:
    kacper_face_encoding = face_recognition.face_encodings(kacper_image)[0]
    pawel_face_encoding = face_recognition.face_encodings(pawel_image)[0]
    piotr_face_encoding = face_recognition.face_encodings(piotr_image)[0]
    damian_face_encoding = face_recognition.face_encodings(damian_image)[0]
    emilk_face_encoding = face_recognition.face_encodings(emilk_image)[0]
    lukasz_face_encoding = face_recognition.face_encodings(lukasz_image)[0]
    maciej_face_encoding = face_recognition.face_encodings(maciej_image)[0]
    panpiotr_face_encoding = face_recognition.face_encodings(panpiotr_image)[0]
    przemek_face_encoding = face_recognition.face_encodings(przemek_image)[0]
    artur_face_encoding = face_recognition.face_encodings(artur_image)[0]
    tomek_face_encoding = face_recognition.face_encodings(tomek_image)[0]
    emil_face_encoding = face_recognition.face_encodings(emil_image)[0]
    kuba_face_encoding = face_recognition.face_encodings(kuba_image)[0]
    hubert_face_encoding = face_recognition.face_encodings(hubert_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()
print('Started: creating known_faces vector')
known_faces = [
    kacper_face_encoding,
    pawel_face_encoding,
    piotr_face_encoding,
    damian_face_encoding,
    emilk_face_encoding,
    lukasz_face_encoding,
    maciej_face_encoding,
    panpiotr_face_encoding,
    przemek_face_encoding,
    artur_face_encoding,
    tomek_face_encoding,
    emil_face_encoding,
    kuba_face_encoding,
    hubert_face_encoding
]

print('Program: started...')
print('Instructions:')
print('->Press SPACE to take a photo')
print('->Press ESC to shut down program')
while True:
    for frame in cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        cv2.imshow("Press Space to take a photo", image)
        rawCapture.truncate(0)
    
        k = cv2.waitKey(1)
        rawCapture.truncate(0)
        if k%256 == 27: # ESC pressed
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "dataset/"+ name +"/image_{}.jpg".format(img_counter)
            cv2.imwrite('/home/pi/Desktop/luty/EXAMPLE.jpg', image)
            print('Program: photo taken')
            unknown_image = face_recognition.load_image_file("EXAMPLE.jpg")
            try:
                unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
                results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
                print("Program: face detected")
                print(results)
                flag = False
                counter = -1
                index = 0
                is_or_not = False
                for i in results:
                    counter += 1
                    if i == True:
                        index  = counter
                        is_or_not = True
                        break
                if is_or_not == True:
                    print('Program: The Face is: ' + table[index])
                    GPIO.output(21, GPIO.LOW)
                    time.sleep(0.1)
                    GPIO.output(21, GPIO.HIGH)
                else:
                    print('Program: The face is not in DataBase')
                GPIO.output(21, GPIO.HIGH)
            except IndexError:
                print("Program: face undetected")
                #quit()      
    if k%256 == 27:
        print("Escape hit, closing...")
        break

cv2.destroyAllWindows()


# results is an array of True/False telling if the unknown face matched anyone in the known_faces array


