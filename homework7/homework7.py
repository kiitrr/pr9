def cyclic_shift_right(numbers):
    """Циклически сдвигает элементы списка вправо на одну позицию."""
    if not numbers: 
        return numbers

    last_element = numbers[-1]  
    for i in range(len(numbers) - 1, 0, -1):
        numbers[i] = numbers[i - 1]  
    numbers[0] = last_element  

    return numbers
