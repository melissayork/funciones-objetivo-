import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def schaffer_n4(x, y):
    term1 = np.cos(np.sin(np.abs(x**2 - y**2)))**2
    term2 = 1 + 0.001 * (x**2 + y**2)
    return 0.5 + (term1 - 0.5) / term2

def schaffer_n4_plot():
    x = np.linspace(-100, 100, 400)
    y = np.linspace(-100, 100, 400)
    X, Y = np.meshgrid(x, y)
    Z = schaffer_n4(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    contour = ax.contourf(X, Y, Z, cmap='viridis')
    fig.colorbar(contour)

    ax.set_title("Schaffer Function N. 4")
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    plt.show()
    
schaffer_n4_plot()
