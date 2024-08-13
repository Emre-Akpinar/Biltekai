import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_byhand = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0,55,55,55,55,55, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0,55,55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0,55,55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0,55,55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0,20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,40,40, 0, 0, 0, 0,40, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0,44,40,40,40,40, 0, 0, 0, 0,40,40, 0,40, 0, 0,40, 0,40, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0,40, 0, 0, 0, 0, 0, 0, 0, 0,40, 0, 0,40, 0, 0,40, 0, 0,40, 0, 0, 0, 0, 0, 0, 0],
    [0, 0,40,40,40,40,40, 0, 0, 0,40, 0, 0, 0, 0,40,40, 0, 0, 0,40, 0, 0, 0, 0, 0, 0, 0],
    [0, 0,40, 0, 0, 0, 0, 0, 0,40,40, 0, 0, 0, 0,40,40, 0, 0, 0,40, 0, 0, 0, 0, 0, 0, 0],
    [0, 0,40, 0, 0, 0, 0, 0, 0,40, 0, 0, 0, 0, 0,40, 0, 0, 0, 0,40, 0, 0, 0, 0, 0, 0, 0],
    [0, 0,40,40,40,40,40, 0, 0,40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,40, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0,40,40,40,40, 0, 0, 0, 0, 0,40,40,40,40,40, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0,40, 0, 0, 0,40, 0, 0, 0, 0, 0,40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0,40,40,40,40, 0, 0, 0, 0, 0,40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0,40,40, 0, 0, 0, 0, 0, 0, 0, 0,40,40,40,40,40, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0,40, 0,40, 0, 0, 0, 0, 0, 0, 0,40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0,40, 0, 0,40, 0, 0, 0, 0, 0, 0,40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0,40, 0, 0, 0,40, 0, 0, 0, 0, 0,40,40,40,40,40, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

X_byhand = np.array(X_byhand)

print(X_byhand.shape)
print(X_train[0].shape)

# Print 4 images in a row
plt.figure(figsize=(10, 5))
for i in range(5):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_train[i])
    plt.title(f"label:{y_train[i]}")
    plt.axis("off")

plt.subplot(2, 4, 6)
plt.imshow(X_byhand, cmap='gray')
plt.title(f"Label: {7, "EMRE"}")
plt.axis('off')
plt.show()
