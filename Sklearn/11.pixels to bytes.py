from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("10.eightorzero.png")
data = list(img.getdata())

for i in range(len(data)):
    data[i] = 255 - data[i]


print(len(data))
print(data)
