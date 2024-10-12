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

even_count = len([num for num in numbers if num % 2 == 0])
odd_count = len([num for num in numbers if num % 2 != 0])

print(f"Количество четных чисел: {even_count}")
print(f"Количество нечетных чисел: {odd_count}")
