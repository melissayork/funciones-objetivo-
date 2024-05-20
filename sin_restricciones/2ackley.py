import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#ESTESI

def ackley(X, Y):
    a = 20
    b = 0.2
    c = 2 * np.pi
    suma1 = X**2 + Y**2
    suma2 = np.cos(c * X) + np.cos(c * Y)
    term1 = -a * np.exp(-b * np.sqrt(0.5 * suma1))
    term2 = -np.exp(0.5 * suma2)
    resul = term1 + term2 + a + np.exp(1)
    return resul

def ackely_plot():
    x = np.linspace(-5, 5, 400)
    y = np.linspace(-5, 5, 400)
    X, Y = np.meshgrid(x, y)

    Z = np.zeros_like(X)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = ackley(X[i, j], Y[i, j])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_title('Función de Ackley')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')

    plt.show()

ackely_plot()
