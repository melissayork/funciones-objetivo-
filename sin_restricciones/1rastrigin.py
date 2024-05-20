import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rastrigin(X):
    A = 10
    return A * len(X) + sum([(x**2 - A * np.cos(2 * np.pi * x)) for x in X])

x = np.linspace(-5.12, 5.12, 400)
y = np.linspace(-5.12, 5.12, 400)
X, Y = np.meshgrid(x, y)

Z = np.zeros_like(X)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i, j] = rastrigin([X[i, j], Y[i, j]])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

punto_inicial = [1, 2]  
punto_z = rastrigin(punto_inicial)
ax.scatter(punto_inicial[0], punto_inicial[1], punto_z, color='red', s=50, label='Punto')

ax.set_title('Función de Rastrigin')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.legend()

plt.show()

# def rastrigin(X):
#     A = 10
#     return A * len(X) + sum([(x**2 - A * np.cos(2 * np.pi * x)) for x in X])

# x = np.linspace(-5.12, 5.12, 400)
# y = np.linspace(-5.12, 5.12, 400)
# X, Y = np.meshgrid(x, y)

# Z = np.zeros_like(X)
# for i in range(X.shape[0]):
#     for j in range(X.shape[1]):
#         Z[i, j] = rastrigin([X[i, j], Y[i, j]])

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(X, Y, Z, cmap='viridis')

# ax.set_title('Función de Rastrigin')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('f(x, y)')

# plt.show()

# def rastrigin(x):
#     A = 10
#     return A * len(x) + sum([(xi**2 - A * np.cos(2 * np.pi * xi)) for xi in x])

# def plot_rastrigin_function():
#     fig=plt.figure()
#     ax=fig.add_subplot(111, projection='3d')
#     x=np.linspace(-5.12, 5.12, 100)
#     y = np.linspace(-5.12, 5.12, 100)
#     x, y = np.meshgrid(x, y)
#     z=rastrigin([x,y])
#     ax.plot_surface(x,y,z,cmap='viridis')
#     punto_inicial=[-2,-2,-2]
#     ax.scatter(punto_inicial[0], punto_inicial[1], rastrigin(punto_inicial), color='red', label='Punto inicial')
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Rastrigin Function')
#     plt.legend()
#     plt.show()
# plot_rastrigin_function()

