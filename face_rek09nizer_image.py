# import face recognition / cv2
import face_recognition as fr
import cv2 as cv


image_side = fr.load_image_file("side.jpg")
image_front = fr.load_image_file("front.jpeg")


image_side_face = fr.face_locations(image_side);
image_front_face = fr.face_locations(image_front);

print(image_front_face)
print("===============")
print(image_side_face)

