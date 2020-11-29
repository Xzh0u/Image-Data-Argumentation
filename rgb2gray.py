import cv2
import numpy as np


def rgb2gray(image):
    grayImage = np.empty([len(image), len(image[0])], dtype=np.uint8)
    for i in range(len(image)):
        for j in range(len(image[0])):
            grayImage[i][j] = int(
                image[i][j][0]*0.2126 + image[i][j][1]*0.7152
                + image[i][j][2] * 0.0722)
    return grayImage


image = cv2.imread('data/test.png', 1)
noisy_image = rgb2gray(image)
cv2.imwrite("saved/rgb2gray.png", (noisy_image))
