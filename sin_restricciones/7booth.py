import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# def booth(x, y):
#     return (x+ 2*y - 7)**2 + (2*x+y-5)**2

# def booth_plot():
#     x = np.linspace(-10, 10, 400)
#     y = np.linspace(-10, 10, 400)
#     X, Y = np.meshgrid(x, y)

#     Z = booth(X, Y)

#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     ax.plot_surface(X, Y, Z, cmap='viridis')

#     ax.set_title('Función de Booth')
#     ax.set_xlabel('x')
#     ax.set_ylabel('y')
#     ax.set_zlabel('f(x, y)')

#     plt.show()

# booth_plot()

import numpy as np
import matplotlib.pyplot as plt

# Definición de la función Goldstein-Price
def goldstein_price(X, Y):
    term1 = (1 + (X + Y + 1)**2 * (19 - 14*X + 3*X**2 - 14*Y + 6*X*Y + 3*Y**2))
    term2 = (30 + (2*X - 3*Y)**2 * (18 - 32*X + 12*X**2 + 48*Y - 36*X*Y + 27*Y**2))
    return term1 * term2

# Método para graficar la función Goldstein-Price
def goldstein_price_plot():
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-2, 2, 400)
    X, Y = np.meshgrid(x, y)

    Z = goldstein_price(X, Y)

    fig, ax = plt.subplots()
    contour = ax.contourf(X, Y, Z, levels=50, cmap='viridis')
    fig.colorbar(contour)

    ax.set_title('Función Goldstein-Price')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    plt.show()

# Llamada al método para graficar la función
goldstein_price_plot()
