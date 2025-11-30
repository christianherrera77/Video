# https://yedhu.medium.com/image-manipulation-in-python-98db79cc0c1
import numpy as np
import imageio
import matplotlib.pyplot as plt
image = imageio.imread('grey_tree.jpg')

bright_image = image + 50
bright_image[bright_image > 255] = 255
imageio.imwrite("bright_grey_tree.jpg", bright_image.astype(np.uint8))
dark_image = image - 50
dark_image[dark_image < 0] = 0
imageio.imwrite("dark_grey_tree.jpg", dark_image.astype(np.uint8))
high_contrast_image = image * 1.5
high_contrast_image[high_contrast_image > 255] = 255
imageio.imwrite("high_contrast_grey_tree.jpg", high_contrast_image.astype(np.uint8))
low_contrast_image = image * 0.5
low_contrast_image[low_contrast_image > 255] = 255
imageio.imwrite("low_contrast_grey_tree.jpg", low_contrast_image.astype(np.uint8))
