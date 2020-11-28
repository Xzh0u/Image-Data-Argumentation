import argparse
import cv2  # cv2 is only used to read image
import numpy as np
import math


def rotate90Anti(saved_file_name="rotate90anti"):
    # anti rotate 90
    img = cv2.imread("data/test.png", 1)
    shape = img.shape
    rev = []
    rev.append(shape[1])
    rev.append(shape[0])
    revF = tuple(rev)
    rotate = np.zeros(revF, dtype=object)

    for i in range(len(img)):
        for j in range(len(img[i])):
            x = len(img[i])-1-j
            rotate[x][i] = img[i][j]

    fi = []
    for i in range(len(rotate)):
        for j in range(len(rotate[i])):
            fi.append(rotate[i][j])
    final = np.array(fi).reshape(revF[0], revF[1], 3)
    # cv2.imshow("Image", final)
    cv2.imwrite(f"saved/{saved_file_name}.png", (final))


def rotateAnyDegree(rotation_degree):
    # rotate any degree(warning: the shape of the image may changed)
    img = cv2.imread("data/test.png", 1)
    rotation_amount_rad = rotation_degree * np.pi / 180.0
    height, width, num_channels = img.shape
    max_len = int(math.sqrt(height*height + width*width))
    rotated_image = np.zeros((max_len, max_len, num_channels))

    rotated_height, rotated_width, _ = rotated_image.shape
    mid_row = int((rotated_height+1)/2)
    mid_col = int((rotated_width+1)/2)

    for r in range(rotated_height):
        for c in range(rotated_width):
            y = (r-mid_col)*math.cos(rotation_amount_rad) \
                + (c-mid_row)*math.sin(rotation_amount_rad)
            x = -(r-mid_col)*math.sin(rotation_amount_rad) \
                + (c-mid_row)*math.cos(rotation_amount_rad)
            y += mid_col
            x += mid_row
            x = round(x)
            y = round(y)
            if (x >= 0 and y >= 0 and x < width and y < height):
                rotated_image[r][c][:] = img[y][x][:]
    cv2.imwrite(f"saved/rotate{rotation_degree}.png", (rotated_image))


def main():
    # Training settings
    parser = argparse.ArgumentParser(description='Data argumentation - rotate')
    parser.add_argument('--rotate-degree', type=int,
                        default=90, help='Image rotate degree.')
    args = parser.parse_args()

    if args.rotate_degree == 90:
        rotate90Anti()
    else:
        rotateAnyDegree(args.rotate_degree)


if __name__ == "__main__":
    main()
