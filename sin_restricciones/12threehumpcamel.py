import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def three_hump_camel(x, y):
    return 2 * x**2 - 1.05 * x**4 + x**6 / 6 + x * y + y**2

def three_hump_camel_plot():
    x = np.linspace(-5, 5, 400)
    y = np.linspace(-5, 5, 400)
    X, Y = np.meshgrid(x, y)

    Z = three_hump_camel(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_title("Función de Three-hump Camel")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')

    plt.show()

three_hump_camel_plot()
