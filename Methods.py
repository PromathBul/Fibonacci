def Enter (message):
    num = int(input(message))
    return num

def Fibonacci (number):
    fib = [1, 1]
    if number == 1:
        return [1]
    elif number == 2:
        return fib
    elif number > 2:
        for item in range (number - 2):
            fib.append(fib[-1] + fib[-2])
        return fib
    else:
        return 'Вы ввели число меньше или равное 0'
