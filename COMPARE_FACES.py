 
import face_recognition

# Load the jpg files into numpy arrays
boris_image = face_recognition.load_image_file("boris.jpeg")
kacper_image = face_recognition.load_image_file("Kacper.jpg")
buffy_image = face_recognition.load_image_file("buffy2.jpeg")
unknown_image = face_recognition.load_image_file("Kacper.jpg")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
try:
    boris_face_encoding = face_recognition.face_encodings(boris_image)[0]
    kacper_face_encoding = face_recognition.face_encodings(kacper_image)[0]
    buffy_face_encoding = face_recognition.face_encodings(buffy_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

known_faces = [
    boris_face_encoding,
    buffy_face_encoding,
    kacper_face_encoding
]

# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

print("Is the unknown face a picture of Boris? {}".format(results[0]))
print("Is the unknown face a picture of Buffy? {}".format(results[1]))
print("Is the unknown face a picture of Kacper? {}".format(results[2]))
print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))
