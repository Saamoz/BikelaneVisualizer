import cv2
import numpy as np


def filter_bikelanes(input_path, output_path):
    img = cv2.imread(input_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # The color bounds for the dark green color used by maps in HSV
    lowerb = np.array([50, 0, 0])
    upperb = np.array([60, 255, 255])

    mask = cv2.inRange(hsv, lowerb, upperb) # mask just the green bikelane color

    # applies the mask to the original image
    imask = mask > 0
    final = np.zeros_like(img, np.uint8)
    final[imask] = img[imask]

    # erodes the image to get rid of any extraneous white pixels
    kernel = np.ones((2, 2), np.uint8)
    final = cv2.erode(final, kernel, iterations=1)

    # applies median blur
    final = cv2.GaussianBlur(final, (3, 3), 0)

    h, s, v = cv2.split(final)

    # find contours
    # ret, thresh = cv2.threshold(v, 1, 255, cv2.THRESH_OTSU)
    # contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(final, contours, -1, (0,255,0), 20)
    # cv2.imshow('Thresh', thresh)
    # if cv2.waitKey(0):
    #     cv2.destroyAllWindows()

    cv2.imwrite(output_path, final)
