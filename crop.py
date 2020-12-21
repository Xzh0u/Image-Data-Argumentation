import argparse
import cv2
import numpy as np


def crop(image_file_name='data/test.png', precent=0.6):
    image = cv2.imread(image_file_name, 1)
    cropImage = np.empty(
        [int(precent * len(image)), int(precent * len(image[0])), 3], dtype=np.uint8)
    for i in range(int(precent * len(image))):
        for j in range(int(precent * len(image[0]))):
            for k in range(3):
                cropImage[i][j][k] = image[i][j][k]
    cv2.imwrite("saved/crop.png", (cropImage))
    return cropImage


crop()
