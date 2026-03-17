import math


x = [2, 4, 9, 16, 25]


def forLoop(x: list) -> list:
    '''用for循环实现'''
    result = []
    for i in x:
        result.append(math.sqrt(i))
    return result


def mapFunction(x: list) -> list:
    '''用map函数实现'''
    return list(map(lambda i: math.sqrt(i), x))


def listComprehension(x: list) -> list:
    '''用列表推导式实现'''
    return [math.sqrt(i) for i in x]


func = [forLoop, mapFunction, listComprehension]
[print(f.__doc__, f(x)) for f in func]