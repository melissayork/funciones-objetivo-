import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gomez_levy_modified(x, y):
    return 4*x**2 - 2.1*x**4 + (1/3)*x**6 + x*y - 4*y**2 + 4*y**4

def restriccion(x, y):
    return -np.sin(4 * np.pi * x) + 2 * (np.sin(2 * np.pi * y))**2 - 1.5

def gomez_levy_modified_plot():
    x = np.linspace(-1, 0.75, 400)
    y = np.linspace(-1, 1, 400)
    X, Y = np.meshgrid(x, y)

    Z = gomez_levy_modified(X, Y)

    R = restriccion(X, Y)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    surface=ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

    fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5)

    ax.contour(X, Y, R, levels=[0], colors='r', linestyles='dashed', label='Restricción')

    min_x, min_y = 0.08984201, -0.7126564
    ax.scatter(min_x, min_y, gomez_levy_modified(min_x, min_y), color='red', s=100, label='Mínimo Global')

    ax.set_title("Función Gómez y Levy Modificada con Restricción")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    ax.legend()

    plt.show()

gomez_levy_modified_plot()