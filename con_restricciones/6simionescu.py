import numpy as np
import matplotlib.pyplot as plt

def simionescu(x, y):
    return 0.1 * x * y

def restriccion(x, y, r_T=1, r_S=0.2, n=8):
    return x**2 + y**2 - (r_T + r_S * np.cos(n * np.arctan2(y, x)))**2

def simionescu_plot():
    x = np.linspace(-1.25, 1.25, 400)
    y = np.linspace(-1.25, 1.25, 400)
    X, Y = np.meshgrid(x, y)

    Z = simionescu(X, Y)

    R = restriccion(X, Y)

    fig, ax = plt.subplots(figsize=(8, 8))
    contour = ax.contourf(X, Y, Z, levels=50, cmap='viridis')
    fig.colorbar(contour, ax=ax, shrink=0.5, aspect=5)

    restriccion_contour = ax.contour(X, Y, R, levels=[0], colors='r', linestyles='dashed', label='Restricción')

    puntos_min = [
        (0.84852813, 0.84852813),
        (-0.84852813, 0.84852813),
        (0.84852813, -0.84852813),
        (-0.84852813, -0.84852813)
    ]

    for min_x, min_y in puntos_min:
        ax.scatter(min_x, min_y, color='red', s=100, label='Mínimo Global')

    ax.set_title("Función Simionescu con Restricción")
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    plt.show()

simionescu_plot()