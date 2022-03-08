import os as os
import face_recognition
import cv2

print('start')
current_path = os.getcwd()
added = "Duże fotki"
folder_path = os.path.join(current_path, added)

# print(current_path)
# print(folder_path)

list_of_files = os.listdir(folder_path)
# print(list_of_files)
list_of_photos = []
margines = 50
i=1
# for i in range(len(list_of_files)):
for file in list_of_files:
    if '.jpg' in file:
        print(i, "/", len(list_of_files))
        img = face_recognition.load_image_file(os.path.join(added, file))
        face_coordinates = face_recognition.face_locations(img)
        print(face_coordinates)
        for (top,right,bottom,left) in face_coordinates:
            new_img = img[top-margines:bottom+margines,left-margines:right+margines]
            new_img_bgr = cv2.cvtColor(new_img, cv2.COLOR_RGB2BGR)
            cv2.imwrite(file, new_img_bgr)
            break
#             cv2.imshow(file, new_img_bgr)
#             cv2.waitKey()
        i+=1
print('end')                                               