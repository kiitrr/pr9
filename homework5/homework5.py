def input_numbers():
    numbers = []
    
    while True:
        user_input = input("Введите числа, разделенные пробелами (или 'end' для завершения): ")
        
        if user_input.lower() == 'end':
            break 
        
        try:
           
            numbers = [float(num) for num in user_input.split()]
            break  
        except ValueError:
            print("Пожалуйста, введите корректные числа, разделенные пробелами.")
    
    return numbers

def find_greater_than_previous(numbers):
    
    def is_greater_by_one(current, previous):
        return current == previous + 1

    
    greater_than_previous = [numbers[i] for i in range(1, len(numbers)) if is_greater_by_one(numbers[i], numbers[i - 1])]
    return greater_than_previous
numbers = input_numbers()
if numbers:  
    result = find_greater_than_previous(numbers)
    print("Элементы, которые больше предыдущего элемента на 1:", result)
else:
    print("Список чисел пуст.")
