import argparse
import cv2
import numpy as np


def flipVertical(image_file_name='data/test.png'):
    image = cv2.imread(image_file_name, 1)
    image = np.array(list(reversed(image)))
    cv2.imshow('window', image)
    cv2.imwrite("saved/flip_vertical.png", (image))


def flipHorizontal(image_file_name='data/test.png'):
    image = cv2.imread(image_file_name, 1)
    image = np.array([list(reversed(row)) for row in image])
    cv2.imshow('window', image)
    cv2.imwrite("saved/flip_horizontal.png", (image))


def main():
    # Training settings
    parser = argparse.ArgumentParser(description='Data argumentation - flip')
    parser.add_argument('--mode', type=str,
                        default='vertical', help='Flip vertical / horizontal.')
    args = parser.parse_args()

    if args.mode == 'vertical':
        flipVertical()
    elif args.mode == 'horizontal':
        flipHorizontal()


if __name__ == "__main__":
    main()
