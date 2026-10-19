import matplotlib.pyplot as plt
from pathlib import Path
import rasterio
import numpy as np

carpeta = Path(__file__).parent 

with rasterio.open(carpeta / "B04.tif") as src:
    rojo = src.read(1)
with rasterio.open(carpeta / "B03.tif") as src:
    verde = src.read(1)
with rasterio.open(carpeta / "B02.tif") as src:
    azul = src.read(1)
with rasterio.open(carpeta / "B08.tif") as src:
    ir = src.read(1)
with rasterio.open(carpeta / "B12.tif") as src:
    swir = src.read(1)


rgb = np.dstack((swir,ir,verde))

plt.figure(1)
plt.imshow(rgb)

ndvi = (ir - rojo) / (ir + rojo)

plt.figure(2)
plt.imshow(ndvi, cmap="RdYlGn", vmin= -1, vmax= 1)
plt.colorbar()

vegetacion = ndvi > 0.4

plt.figure(3)
plt.imshow(vegetacion, cmap="gray")
plt.show()