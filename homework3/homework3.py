numbers = []

while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    
    if user_input.lower() == 'end':
        break  
    
    try:
        
        number = int(user_input)
        numbers.append(number)  
    except ValueError:
        print("Пожалуйста, введите корректное целое число.")

