import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def townsend(x, y):
    return -(np.cos((x - 0.1) * y))**2 - x * np.sin(3 * x + y)

def restriccion(x, y):
    t = np.arctan2(y, x)
    return x**2 + y**2 - ((2 * np.cos(t) - 0.5 * np.cos(2 * t) - 0.25 * np.cos(3 * t) - 0.125 * np.cos(4 * t))**2 + (2 * np.sin(t))**2)

def townsend_plot():
    x = np.linspace(-2.25, 2.25, 400)
    y = np.linspace(-2.5, 1.75, 400)
    X, Y = np.meshgrid(x, y)

    Z = townsend(X, Y)

    R = restriccion(X, Y)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    surface = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

    fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5)

    ax.contour(X, Y, R, levels=[0], colors='r', linestyles='dashed', label='x^2 + y^2 = constraint')

    min_x, min_y = 2.0052938, 1.1944509
    ax.scatter(min_x, min_y, townsend(min_x, min_y), color='red', s=100, label='Global Minimum')

    ax.set_title("Función Townsend con Restricción")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    ax.legend()
    plt.show()

townsend_plot()