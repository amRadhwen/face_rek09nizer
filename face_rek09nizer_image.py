# import face recognition / cv2
import face_recognition as fr
import cv2 as cv
import sys

image_side = fr.load_image_file("side.jpg")
image_front = fr.load_image_file("front.jpeg")
image_many = fr.load_image_file("many_faces.jpg")


image_side_face = fr.face_locations(image_side)
image_front_face = fr.face_locations(image_front)
image_many_face = fr.face_locations(image_many)





