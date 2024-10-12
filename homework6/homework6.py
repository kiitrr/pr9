import random
numbers = []

while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    if user_input.lower() == 'end':
        break
    try:
        number = int(user_input)
        numbers.append(number)  
    except ValueError:
        print("Ошибка: введите корректное целое число.")

if numbers:
    
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))
    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

    print("Список после замены:", numbers)
else:
    print("Список пуст.")

