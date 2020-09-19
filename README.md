# Car-Pedestrian-Detection

This is a AI based car and pedestrian detection for road safety using OpenCV

## Main steps

1. collecting image data of cars and pedestrians
2. convert images into greyscale to make the model faster and color is not important to detect object in this project
3. train algorithm to detect cars and pedestrains

## How the algorithm works behind?

Using the Haar featue computer calculate the correlation bewteen pixels of the model and the object

A Haar Cascade is based on “Haar Wavelets” which Wikipedia defines as:
A sequence of rescaled “square-shaped” functions which together form a wavelet family or basis.
It is based on the Haar Wavelet technique to analyze pixels in the image into squares by function. This uses machine learning techniques to get a high degree of accuracy from what is called “training data”. This uses “integral image” concepts to compute the “features” detected. Haar Cascades use the Adaboost learning algorithm which selects a small number of important features from a large set to give an efficient result of classifiers.
![This is a brief illustration of Features Extraction and the difference between Face Detection and Face Recognition. Face detection is about locating, while face recognition is about identifying.](https://miro.medium.com/max/1400/1*Qs62ETmtyShs9yQUWZxb8Q.png)


# Requirement 
```
pip install opencv-python
```
