import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def func1(x, a, b):
    return a * x + b

def func2(x, a, b):
    return a/(1 + b * x)


def test_func1(param):
    global data
    Fx = param[0] * data[:, 0] + param[1]
    return np.sum((Fx - data[:, 1]) ** 2)

def test_func2(param):
    global data
    Fx = param[0] / (1 + data[:, 0] * param[1])
    return np.sum((Fx - data[:, 1]) ** 2)


def method_prm(func, e, k, data):
    a = -1
    b = -1
    dct = {}
    count_i = 0
    count_f = 0
    while a <= 2:
        b = 0
        while b <= 2:
            F = func(data[:, 0], a, b)
            sm = np.sum((F - data[:, 1]) ** 2)
            dct[sm] = [a, b]
            b += 0.001
            count_i += 1
            count_f += 1
        a += 0.001
    
    key = min(dct.keys())
    ans_x = dct[key]

    return ans_x, count_f, count_i

def dop(a, b, func):
    count_f = 0
    k = -1
    dct = {}
    while k <= 2:
        sm = np.sum((func(data[:, 0], k, b) - data[:, 1]) ** 2)
        dct[sm] = [k, b]
        k += 0.001
        count_f += 1
    
    key = min(dct.keys())
    a = dct[key][0]
    fa = key

    k = -1
    dct = {}
    while k <= 2:
        sm = np.sum((func(data[:, 0], a, k) - data[:, 1]) ** 2)
        dct[sm] = [a, k]
        k += 0.001
        count_f += 1
    
    key = min(dct.keys())
    b = dct[key][1]
    fb = key

    return a, b, fb, count_f


def method_gaus(func, e, k, data):
    a =-1
    b = -1

    F = np.sum((func(data[:, 0], a, b) - data[:, 1]) ** 2)

    flaga = False
    flagb = False

    count_i = 1
    count_f = 0

    a0, b0, F0, count_f = dop(a, b, func)

    while abs(F - F0) >= e:
        # print(F, F0)
        a = a0
        b = b0
        F = F0
        # b = b0
        a0, b0, F0, cnt = dop(a, b, func)
        count_f += cnt
        count_i += 1

    return [a, b], count_f, count_i


def draw_fig(data, prm, gaus, ned):
    ax = plt.axes()
    ax.set_title("Линейная аппроксимирующая функция")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    n = list(range(1, 2001))
    ax.scatter(data[:, 0], data[:, 1], label="Исходные данные")
    y = func1(data[:, 0], prm[0], prm[1])
    ax.plot(data[:, 0], y, label="Перебор")
    y = func1(data[:, 0], gaus[0], gaus[1])
    ax.plot(data[:, 0], y, label="Гаус")
    y = func1(data[:, 0], ned[0], ned[1])
    ax.plot(data[:, 0], y, label="Нелдер-Мида")
    ax.legend()

    plt.savefig('C:\\Users\\yulia\\OneDrive\\Рабочий стол\\ntvc\\ITMO\\алгоритмы\\task_2\\func1.png')
    plt.show()


# data = []

if __name__ == '__main__':
    a = random.uniform(0, 1)
    b = random.uniform(0, 1)
    n = 100
    global data
    data = []
    for i in range(n):
        d = random.uniform(0, 1)
        x = i / 100
        y = a * x + b + d
        data.append([x, y])
    
    e = 0.001

    data = np.array(data)
    
    answer = {}

    for func in [func1, func2]:
        k = str(func).split()[1]
        param = method_prm(func1, e, n, data)
        print(param[1], param[2])
        param1 = method_gaus(func1, e, n, data)
        print(param1[1], param1[2])
        if not k in answer:
            answer[k] = []
        answer[k].append(param[0])
        answer[k].append(param1[0])



    x0 = np.array([0 ,0])

    res = minimize(test_func1, x0, method="Nelder-Mead", options={'xtol': 1e-3, 'disp': True})
    answer['func1'].append(res.x)
    print(res.nfev, res.nit)

    res = minimize(test_func2, x0, method="Nelder-Mead", options={'xtol': 1e-3, 'disp': True})
    answer['func2'].append(res.x)
    print(res.nfev, res.nit)

    print(answer)

    draw_fig(data, answer['func1'][0], answer['func1'][1], answer['func1'][2])



    # plt.plot(data[:, 0], data[:, 1])
    # plt.plot(data[:, 0], func2(data[:, 0], param[0], param[1]))

    # plt.show()