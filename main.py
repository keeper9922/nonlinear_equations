from sympy import symbols, zeros, diff
from funcs import *
def field(divisions, first, last):
    _h = (first - last) / divisions
    _field = []
    for _ in range(divisions + 1):
        _field.append(first + _ * _h)
    return _field, _h
def newton(dimension_field:tuple[list[int | float], float], limits=100, eps=0.1):
    _field, _h = dimension_field
    x = [_field[0]]
    found = False
    k = 0
    n = 0
    while True:
        differ = f1_center(x[n], _h)
        try:
            # print(x[n], y(x[n]), x[n] - y(x[n]), differ)
            x.append(x[n] - y(x[n]) / differ)
            if n >= 1 and abs((x[n + 1] - x[n]) / (1 - (x[n + 1] - x[n]) / (x[n] - x[n - 1]))) < eps:
                k = n + 1
                found = True
                break
            n += 1
        except ZeroDivisionError:
            print(f"Деление на 0: {n}, {x[n]} , {differ}")
            break
    if found:
        print(f"Найден корень x = {x[n - 1]}, Число итераций: {k}")
        return
    print("Нет корней")

newton(field(100, -10, 10),10, 1e-7)
