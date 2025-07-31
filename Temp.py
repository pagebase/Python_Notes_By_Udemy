import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load an image
image = Image.open('example.jpg')
image_array = np.array(image)

# Convert to grayscale
gray_image = np.mean(image_array, axis=2).astype(np.uint8)

# Apply a simple edge detection filter
kernel = np.array([[-1, -1, -1],
                   [-1, 8, -1],
                   [-1, -1, -1]])
edges = np.zeros_like(gray_image)
for i in range(1, gray_image.shape[0]-1):
    for j in range(1, gray_image.shape[1]-1):
        edges[i,j] = np.sum(gray_image[i-1:i+2, j-1:j+2] * kernel)

# Display results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Grayscale')
plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Edge Detection')
plt.show()
