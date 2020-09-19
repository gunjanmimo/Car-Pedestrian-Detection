# Car-Pedestrian-Detection

This is a AI based car and pedestrian detection for road safety using OpenCV

## Main steps

1. collecting image data of cars and pedestrians
2. convert images into greyscale to make the model faster and color is not important to detect object in this project
3. train algorithm to detect cars and pedestrains

## How the algorithm works behind?


A Haar Cascade is based on “Haar Wavelets” which Wikipedia defines as:
A sequence of rescaled “square-shaped” functions which together form a wavelet family or basis.
It is based on the Haar Wavelet technique to analyze pixels in the image into squares by function. This uses machine learning techniques to get a high degree of accuracy from what is called “training data”. This uses “integral image” concepts to compute the “features” detected. Haar Cascades use the Adaboost learning algorithm which selects a small number of important features from a large set to give an efficient result of classifiers.
![This is a brief illustration of Features Extraction and the difference between Face Detection and Face Recognition. Face detection is about locating, while face recognition is about identifying.](https://miro.medium.com/max/1400/1*Qs62ETmtyShs9yQUWZxb8Q.png)

### Feature Extraction

As I mentioned earlier, Haar Cascades use machine learning techniques in which a function is trained from a lot of positive and negative images. This process in the algorithm is feature extraction.
![In feature extraction, the algorithm uses training data to best identify features that it can consider a face.](https://miro.medium.com/max/1400/1*XFbTIeG91oW9Tj4uXl2yOg.png)

## Requirement 
```
pip install opencv-python
```

## Run the project

copy a road video in the ```Car``` file and in the code change the file name and run the code from your terminal

```python file_path/Car and Pedestrian Tracking.py```
