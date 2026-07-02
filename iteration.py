import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_sample_image

flower = load_sample_image('flower.jpg')

output = []
for line in flower:
  for pixel in line:
    moyenne = int(np.mean(pixel))
    moyenne_3d = np.stack((moyenne, moyenne, moyenne))
    output.append(moyenne_3d)
img_black_and_white = np.array(output).reshape(flower.shape)
plt.imshow(np.concatenate((img_black_and_white, flower), axis=0))
plt.show()