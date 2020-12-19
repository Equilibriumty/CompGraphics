import random
import numpy as np
import cv2

image = cv2.imread('cats-32.jpg')
cv2.imshow("Original Image", image)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", grayImage)


def sp_noise(image, prob):
    """
    Add salt and pepper noise to image
    prob: Probability of the noise
    """
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


noise_img = sp_noise(grayImage, 0.05)
cv2.imshow("Salt and pepper noise", noise_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
