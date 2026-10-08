# Natriz

import numpy as np
import matplotlib.pyplot as plt

matriz = np.array([[2, 4, 6], [0, 2, 10], [5, 5, 8]])

print(matriz)
print(matriz.shape)

print(matriz[0,1])

plt.imshow(matriz, cmap="Reds")
plt.colorbar()
plt.show()