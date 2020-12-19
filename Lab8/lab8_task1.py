import cv2
import numpy as np
import random

image = cv2.imread("cats-32.jpg")
cv2.imshow("Original image", image)
image1 = cv2.bitwise_not(image)
cv2.imshow("Inverted image", image1)


def sepia(image):
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    return cv2.filter2D(image, -1, kernel)


image2 = sepia(image1)


def sp_noise(image, prob):
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


dst = sp_noise(image2, 0.01)
cv2.imshow("Salt&Pepper noise + Sepia", dst)
brighten_image = cv2.bitwise_not(image2)

new_image = np.zeros(brighten_image.shape, brighten_image.dtype)
alpha = 1.3
beta = 40
for y in range(brighten_image.shape[0]):
    for x in range(brighten_image.shape[1]):
        for c in range(brighten_image.shape[2]):
            new_image[y, x, c] = np.clip(alpha * brighten_image[y, x, c] + beta, 0, 255)

lookUpTable = np.empty((1, 256), np.uint8)
for i in range(256):
    lookUpTable[0, i] = np.clip(pow(i / 255.0, 0.8) * 255.0, 0, 255)
res = cv2.LUT(new_image, lookUpTable)

denoise_image = cv2.medianBlur(image, 5)
cv2.imshow("Denoise + brightness/contrast correction", denoise_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
