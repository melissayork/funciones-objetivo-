import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def shekel(x, y, a, c):
    result = 0
    for i in range(len(c)):
        result += 1 / (c[i] + (x - a[0, i])**2 + (y - a[1, i])**2)
    return result

x = np.linspace(0, 6, 400)
y = np.linspace(0, 6, 400)
X, Y = np.meshgrid(x, y)

a = np.array([[4, 4, 4, 4],
              [1, 1, 1, 1]])
c = np.array([0.1, 0.2, 0.2, 0.4])

Z = shekel(X, Y, a, c)

punto_x = 1
punto_y = 1
print("Valor de la función Shekel en (1, 1):", shekel(punto_x, punto_y, a, c))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_title("Función de Shekel")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')

plt.show()

