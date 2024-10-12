import os

def get_squares(a, b):
    
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Оба значения должны быть целыми числами.")
    
    start = min(a, b)
    end = max(a, b)
    

    squares = [i**2 for i in range(start, end + 1)]
    return squares

try:
    a = int(input("Введите первое целое число (a): "))
    b = int(input("Введите второе целое число (b): "))    