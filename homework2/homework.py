import os

def get_squares(a, b):
    
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Оба значения должны быть целыми числами.")
    
    start = min(a, b)
    end = max(a, b)
    
