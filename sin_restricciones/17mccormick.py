import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def mccormick(x, y):
    return np.sin(x + y) + (x - y)**2 - 1.5*x + 2.5*y + 1

def mccormick_plot():
    x = np.linspace(-1.5, 4, 400)
    y = np.linspace(-3, 4, 400)
    X, Y = np.meshgrid(x, y)

    Z = mccormick(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_title("Función McCormick")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')

    plt.show()

mccormick_plot()
