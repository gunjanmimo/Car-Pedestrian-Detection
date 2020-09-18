# this is the main code file for this project 😁
# Gunjan Paul 19th Septmember 2020


# importing libraries
import cv2

# image file
img_file = "Car.jpg"


# pre-trained car classifer
car_classifer = "cars.xml"

# create opencv image( a multidimensional image data)
img = cv2.imread(img_file)
