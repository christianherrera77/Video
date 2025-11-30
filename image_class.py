import numpy as np
from PIL import Image

square = np.zeros((600, 600))
square[300:500, 200:400] = 255
square[30:50, 20:40] = 127

square_img = Image.fromarray(square)

square_img.show()