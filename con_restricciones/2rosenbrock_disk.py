import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rosenbrock_disk(x, y):
    return (1 - x)**2 + 100 * (y - x**2)**2

def restriccion(x, y):
    return x**2 + y**2 - 2

def rosenbrock_disk_plot():
    x = np.linspace(-1.5, 1.5, 400)
    y = np.linspace(-0.5, 2.5, 400)
    X, Y = np.meshgrid(x, y)

    Z = rosenbrock_disk(X, Y)

    R= restriccion(X, Y)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    surface = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

    fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5)

    ax.contour(X, Y, Z, levels=50, cmap='viridis', linestyles='solid', offset=-1)
    ax.contour(X, Y, R, levels=[0], colors='r', linestyles='dashed', label='x^2 + y^2 <= 2')

    ax.scatter(1, 1, rosenbrock_disk(1, 1), color='red', s=100, label='Mínimo global (1, 1)')

    ax.set_title("Función de Rosenbrock con Restricción")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    ax.legend()

    plt.show()

rosenbrock_disk_plot()