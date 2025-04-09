# функции:
def y(x) -> float:
    """
    Оригинальная функция
    :param x: Входное значение (точка на отрезке)
    :return:
    """
    return (x + 7) / (6 * (x*x + 2*x + 7)**(1/2))

def f1_center(x, h) -> float:
    return (y(x+h) - y(x-h)) / (2*h)