import numpy as np
import random
from scipy.optimize import minimize, root, basinhopping, differential_evolution
import matplotlib.pyplot as plt
import os

def approks(param, b=0):
    global data
    f = (param[0] * data[:, 0] + param[1]) / (data[:, 0] ** 2 + param[2] * data[:, 0] + param[3])
    if b == 1:
        return f
    return np.sum((f - data[:, 1]) ** 2)

def lev(param):
    return approks(param), 0, 0, 0


def draw_fig(data, func, nm, lm, bh, de):
    k = str(func).split()[1]
    ax = plt.axes()
    ax.set_title(k)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.scatter(data[:, 0], data[:, 1], label="Исходные данные")
    y_nm = func(nm, 1)
    ax.plot(data[:, 0], y_nm, label="Нелдер-Мид", color="green")
    y_lm = func(lm, 1)
    ax.plot(data[:, 0], y_lm, label="Левенберг", color="red")
    y_bh = func(bh, 1)
    ax.plot(data[:, 0], y_bh, label="Имитация ожига", color="orange")
    y_de = func(de, 1)
    ax.plot(data[:, 0], y_de, label="Деффиринциальная эволюция", color="purple")
    ax.legend()
    pth = os.getcwd()

    plt.savefig(pth + '\\' + k +'.png')
    plt.show()

if __name__ == "__main__":
    global data
    data = []
    for i in range(1000):
        theta = random.uniform(0.001, 0.99)
        x = 3 * (i + 1) / 1000
        f = 1 / (x ** 2 - 3 * x + 2)
        y = 0
        if f < -100:
            y = -100 + theta
        elif abs(f) <= 100:
            y = f + theta
        else:
            y = 100 + theta
        data.append([x, y])

    data = np.array(data)

    x0 = np.array([0, 0, 0, 0])

    nm = minimize(approks, x0, method='Nelder-Mead', options={'xtol': 1e-3, 'disp': True})
    lm = root(lev, x0, method='lm')
    bh = basinhopping(approks, x0, niter=1000)
    de = differential_evolution(approks, [(-5, 5), (-5, 5), (-5, 5), (-5, 5)])

    print(nm.fun, nm.nit)
    print(lm.fun, lm.nfev)
    print(bh.fun, bh.nit)
    print(de.fun, de.nit)

    draw_fig(data, approks, nm.x, lm.x, bh.x, de.x)





        
