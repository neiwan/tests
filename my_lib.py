def fibonacciElement(n):
    if n in (1, 2):
        return 1
    return fibonacciElement(n - 1) + fibonacciElement(n - 2)


def fibonacci(n):
    if n <= 0:
        raise IndexError
    list = []
    for i in range(1, n + 1, 1):
        list.append(fibonacciElement(i))
    return list


def calc(a, b, operator):
    match operator:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b


def bubbleSort(array):
    length = len(array)
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array
