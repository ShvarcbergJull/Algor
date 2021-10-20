import random
import math

def func1(x):
    return x ** 3

def func2(x):
    return abs(x - 0.2)

def func3(x):
    return x * math.sin(1/x)


def method_enum(func, e, a, b):
    n = ((b - a) // e) + 1
    n = int(n)
    inf = {}
    for i in range(n):
        x = a + i * (b - a / n)
        fx = func(x)
        inf[fx] = x

    key = min(inf.keys())
    ans_x = inf[key]
    return (ans_x, n , n)

def method_ditohomy(func, e, a, b):
    count_iter = 0
    count_func = 0
    d = random.uniform(0.00001, e-0.00001)
    while abs(a - b) >= e:
        x1 = (a + b + d)/2
        x2 = (a + b - d)/2

        fx1 = func(x1)
        fx2 = func(x2)

        if fx1 <= fx2:
            b = x2
        else:
            a = x1
        count_iter += 1
        count_func += 2

    return ((a + b) / 2, count_func, count_iter)

def method_golden(func, e, a, b):
    d = random.uniform(0.00001, e-0.00001)
    x1 = a + ((3 - math.sqrt(5))/2) * (b - a)
    x2 = b + ((math.sqrt(5) - 3)/2) * (b - a)

    fx1 = func(x1)
    fx2 = func(x2)

    count_iter = 1
    count_func = 2

    while abs(a - b) >= e:
        if fx1 <= fx2:
            b = x2
            x2 = x1
            fx2 = fx1
            x1 = a + ((3 - math.sqrt(5))/2) * (b - a)
            fx1 = func(x1)
        else:
            a = x1
            x1 = x2
            fx1 = fx2
            x2 = b + ((math.sqrt(5) - 3)/2) * (b - a)
            fx2 = func(x2)
        count_func += 1
        count_iter += 1
        
    
    return ((a + b) / 2, count_func, count_iter) 

if __name__ == "__main__":
    funcs = [[func1, 0, 1], [func2, 0, 1], [func3, 0.01, 1]]

    for func in funcs:
        print(method_enum(func[0], 0.001, func[1], func[2]))
        print(method_ditohomy(func[0], 0.001, func[1], func[2]))
        print(method_golden(func[0], 0.001, func[1], func[2]))