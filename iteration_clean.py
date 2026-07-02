import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_sample_image

flower = load_sample_image('flower.jpg')

moyenne = np.mean(flower, axis=2, dtype=int)
img_np = np.repeat(moyenne, 3).reshape(flower.shape)
plt.imshow(np.concatenate((img_np, flower), axis=0))
plt.show()