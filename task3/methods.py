import numpy as np
import random
import os
from scipy.optimize import minimize, root
from scipy.misc import derivative
import matplotlib.pyplot as plt

###########

def linear(param, b=0):
    global data
    f = param[0] * data[:, 0] + param[1]
    if b:
        return f
    return np.sum((f - data[:, 1]) ** 2)

def linear_lm(param, b=0):
    global data
    f = param[0] * data[:, 0] + param[1]
    if b:
        return f
    return (np.sum((f - data[:, 1]) ** 2), 0)

def racional(param, b=0):
    global data
    f = param[0] / (1 + param[1] * data[:, 0])
    if b:
        return f
    return np.sum((f - data[:, 1]) ** 2)

def racional_lm(param, b=0):
    global data
    f = param[0] / (1 + param[1] * data[:, 0])
    if b:
        return f
    return np.sum((f - data[:, 1]) ** 2), 0


def lineara(a):
    global data
    global A, B
    # f = a * data[:, 0] + B
    return np.sum(((a * data[:, 0] + B) - data[:, 1]) ** 2)

def linearb(b):
    global data
    global A, B
    # f = A * data[:, 0] + b
    return np.sum(((A * data[:, 0] + b) - data[:, 1]) ** 2)


def racionala(a):
    global data
    global A, B
    return np.sum(((a / (1 + B * data[:, 0])) - data[:, 1]) ** 2)

def racionalb(b):
    global data
    global A, B
    return np.sum(((A / (1 + b * data[:, 0])) - data[:, 1]) ** 2)

#########


def gradient(eps, func, funca, funcb):
    global A, B
    A, a0 = 0.01, 0.01
    B, b0 = 0.01, 0.01
    step_a, step_b = 0.01, 0.01
    f0 = func([a0, b0])
    pra = derivative(funca, A)
    prb = derivative(funcb, B)
    A = A - step_a * pra
    B = B - step_b * prb
    f = func([A, B])

    while abs(f - f0) >= eps:
        print(f, f0)
        prA = pra
        prB = prb
        pra = derivative(funca, A)
        prb = derivative(funcb, B)
        step_a, step_b = abs((np.array([a0, b0]) - np.array([A, B])) * (np.array([prA, prB]) - np.array([pra, prb]))) / ((np.array([prA, prB]) - np.array([pra, prb])) ** 2)
        a0 = A
        b0 = B
        A = A - step_a * pra
        B = B - step_b * prb
        f0 = f
        f = func([A, B])
    return (A, B)    


def draw_fig(data, func, grad, cg, ncg, lm):
    k = str(func).split()[1]
    ax = plt.axes()
    ax.set_title(k)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.scatter(data[:, 0], data[:, 1], label="Исходные данные")
    y_cg = func(cg, 1)
    ax.plot(data[:, 0], y_cg, label="Сопряженный градиент")
    y_ncg = func(ncg, 1)
    ax.plot(data[:, 0], y_ncg, label="Ньютон")
    y_lm = func(lm, 1)
    ax.plot(data[:, 0], y_lm, label="Левенберг-Марквардта")
    y_grad = func(grad, 1)
    ax.plot(data[:, 0], y_grad, label="Градиент")
    ax.legend()
    pth = os.getcwd()

    plt.savefig(pth + '\\' + k +'.png')
    plt.show()

if __name__ == "__main__":
    global data
    data = []
    alpha = random.uniform(0.001, 0.99)
    beta = random.uniform(0.001, 0.99)

    n = 100
    for k in range(n):
        teta = random.uniform(0.001, 0.99)
        x = (k + 1) / n
        y = alpha * x + beta + teta
        data.append([x, y])

    data = np.array(data)

    x0 = np.array([0, 0])

    for func in [[linear, linear_lm, lineara, linearb], [racional, racional_lm, racionala, racionalb]]:
        grad = gradient(0.001, func[0], func[2], func[3])
        cg = minimize(func[0], x0, method='CG', options={'xtol': 1e-3, 'disp': True})
        ncg = minimize(func[0], x0, method='TNC', options={'xtol': 1e-3, 'disp': True})
        lm = root(func[1], x0, method='lm')

        draw_fig(data, func[0], grad, cg.x, ncg.x, lm.x)