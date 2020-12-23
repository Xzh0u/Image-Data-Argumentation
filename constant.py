import argparse
import cv2
import numpy as np
import random


def addConstant(image_file_name='data/test.png', length=50, num=5):
    image = cv2.imread(image_file_name, 1)
    modifiedImage = np.empty(
        [len(image),  len(image[0]), 3], dtype=np.uint8)
    for i in range(len(image)):
        for j in range(len(image[0])):
            for k in range(3):
                modifiedImage[i][j][k] = image[i][j][k]
    for i in range(num):
        startX = random.randint(0, len(image) - length)
        startY = random.randint(0, len(image) - length)
        addConstantOnce(modifiedImage, length, startX, startY)
    cv2.imwrite("saved/constant.png", (modifiedImage))


def addConstantOnce(modifiedImage, length, startX, startY):
    for i in range(startX, startX + length):
        for j in range(startY, startY + length):
            for k in range(3):
                modifiedImage[i][j][k] = 0

    return modifiedImage


addConstant(num=20)
