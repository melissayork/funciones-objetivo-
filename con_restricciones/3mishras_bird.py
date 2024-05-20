import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def mishras_bird(x, y):
    term1 = np.sin(y) * np.exp((1 - np.cos(x))**2)
    term2 = np.cos(x) * np.exp((1 - np.sin(y))**2)
    term3 = (x - y)**2
    return term1 + term2 + term3

def restriccion(x, y):
    return (x + 5)**2 + (y + 5)**2 - 25

def mishras_bird_plot():
    x = np.linspace(-10, 0, 400)
    y = np.linspace(-6.5, 0, 400)
    X, Y = np.meshgrid(x, y)

    Z = mishras_bird(X, Y)

    R = restriccion(X, Y)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    surface = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

    fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5)

    ax.contour(X, Y, R, levels=[0], colors='r', linestyles='dashed', label='(x+5)^2 + (y+5)^2 = 25')

    min_x, min_y = -3.1302468, -1.5821422
    ax.scatter(min_x, min_y, mishras_bird(min_x, min_y), color='red', s=100, label='Minimo global')

    ax.set_title("Función Mishra's Bird con Restricción")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    ax.legend()

    plt.show()

mishras_bird_plot()
