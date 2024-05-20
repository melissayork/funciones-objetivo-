import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def goldstein_price(X, Y):
    term1 = (1 + (X + Y + 1)**2 * (19 - 14*X + 3*X**2 - 14*Y + 6*X*Y + 3*Y**2))
    term2 = (30 + (2*X - 3*Y)**2 * (18 - 32*X + 12*X**2 + 48*Y - 36*X*Y + 27*Y**2))
    return term1 * term2

def goldstein_price_plot():
    x = np.linspace(-2, 2, 800)
    y = np.linspace(-2, 2, 800)
    X, Y = np.meshgrid(x, y)

    Z = goldstein_price(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_title('Función Goldstein-Price')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')

    plt.show()

goldstein_price_plot()

