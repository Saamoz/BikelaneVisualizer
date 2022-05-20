import cv2
import numpy as np


def filter_bikelanes(input_path, output_path):
    img = cv2.imread(input_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # The color bounds for the dark green color used by maps in HSV
    lowerb = np.array([60, 0, 0])
    upperb = np.array([60, 255, 255])

    mask = cv2.inRange(hsv, lowerb, upperb) # mask just the green bikelane color

    # applies the mask to the original image
    imask = mask > 0
    final = np.zeros_like(img, np.uint8)
    final[imask] = img[imask]

    # erodes the image to get rid of any extraneous white pixels
    kernel = np.ones((2, 2), np.uint8)
    final = cv2.erode(final, kernel, iterations=1)

    cv2.imwrite(output_path, final)
