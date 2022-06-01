import cv2
import numpy as np


def filter_bikelanes(input_path, output_path):
    img = cv2.imread(input_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # The color bounds for the dark green color used by maps in HSV
    lowerb = np.array([50, 40, 0])
    upperb = np.array([60, 255, 255])

    mask = cv2.inRange(hsv, lowerb, upperb)  # mask just the green bikelane color
    write_pbm(mask)

    # applies the mask to the original image
    imask = mask > 0
    final = np.zeros_like(img, np.uint8)
    final[imask] = img[imask]

    # erodes the image to get rid of any extraneous white pixels
    kernel = np.ones((2, 2), np.uint8)
    final = cv2.erode(final, kernel, iterations=1)

    # final = cv2.GaussianBlur(final, (3, 3), 0)

    cv2.imwrite(output_path, final)


def crop_image(image_path):
    screenshot = cv2.imread(image_path)

    # crops image to remove UI elements and make it square
    vert_img_size = 800
    hor_image_size = 800
    width, height, _ = screenshot.shape
    left = (width - hor_image_size) // 2
    top = (height - vert_img_size) // 2
    right = (width + hor_image_size) // 2
    bottom = (height + vert_img_size) // 2
    cropped_ss = screenshot[left:right, top:bottom]
    output_path = 'temp/cropped_ss.png'
    cv2.imwrite(output_path, cropped_ss)
    return output_path


def write_svg(contours, output_path):
    with open(output_path, "w+") as f:
        f.write(f'<svg width="{800}" height="{800}" xmlns="http://www.w3.org/2000/svg"> ')

        for c in contours:
            f.write('<path d="M')
            for i in range(len(c)):
                x, y = c[i][0]
                f.write(f"{x} {y} ")
            f.write('" style="stroke:black"/>')
        f.write("</svg>")


def write_pbm(image):
    image = np.copy(image)
    image[image <= 1] = 1
    image[image > 1] = 0
    with open('temp/pbm_image.pbm', 'w') as fd:
        fd.write("P1\n%i %i\n" % image.shape[::-1])
        fd.write("\n".join(" ".join(str(i) for i in j) for j in image))
