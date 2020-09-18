# Gunjan Paul 19th Septmember 2020 😎


# importing libraries
import cv2

# image file
img_file = "./Car/Car.jpg"
# pre-trained car classifer
car_classifer = "cars.xml"


# create opencv image( a multidimensional image data)
img = cv2.imread(img_file)


# convert to greyscale
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# create  car classifer
car_tracker = cv2.CascadeClassifier(car_classifer)

# detecting car in the image
cars = car_tracker.detectMultiScale(black_n_white)

# drawing recctangle around the cars on the basis of the car cordinates
car1 = cars[0]
(x, y, w, h) = car1

cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

# for (x, y, w, h) in cars:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (o, 0, 255), 2)


cv2.imshow("detected car", img)
cv2.waitKey(0)
