# https://yedhu.medium.com/image-manipulation-in-python-98db79cc0c1
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

im = Image.open(r"gradiente.jpg")
gradiente = np.asarray(im)
#gradiente = np.zeros((255, 255))
#for offset in range(0, 255):
#    gradiente[0:255 , offset] = offset

#plt.hist(gradiente,bins=range(255))
#plt.show()

image = Image.fromarray(gradiente)
image.show()

bright_gradiente = gradiente + 50
bright_gradiente[bright_gradiente > 255] = 255
bright_image = Image.fromarray(bright_gradiente)
bright_image.show()
#imageio.imwrite("gradiente.jpg", gradiente.astype(np.uint8))
#print(gradiente)
dark_gradiente = gradiente - 50
dark_gradiente[dark_gradiente < 0] = 0
dark_image = Image.fromarray(dark_gradiente)
dark_image.show()

high_contrast_gradiente = gradiente * 1.5
high_contrast_gradiente[high_contrast_gradiente > 255] = 255
high_contrast = Image.fromarray(high_contrast_gradiente)
high_contrast.show()

low_contrast_gradiente = gradiente * 0.5
low_contrast_gradiente[low_contrast_gradiente < 0] = 0
low_contrast = Image.fromarray(low_contrast_gradiente)
low_contrast.show()
