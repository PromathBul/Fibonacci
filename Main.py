import ftplib
from Methods import Enter
from Methods import Fibonacci

import os

os.system('cls')

num = Enter('Введите количество членов ряда Фибоначчи: ')

fib = Fibonacci(num)
print(fib)