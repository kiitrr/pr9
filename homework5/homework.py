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

