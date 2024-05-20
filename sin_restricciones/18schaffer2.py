import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def schaffer(x, y):
    numerador = np.sin(x**2 - y**2)**2 - 0.5
    denominador = 1 + 0.001 * (x**2 + y**2)**2
    return 0.5 + numerador / denominador

def schaffer_plot():
    x = np.linspace(-100, 100, 400)
    y = np.linspace(-100, 100, 400)
    X, Y = np.meshgrid(x, y)

    Z = schaffer(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_title("Función de Schaffer N. 2")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')

    plt.show()

schaffer_plot()