import random

ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

def get_user_numbers():
    """Получает числа от пользователя."""
    user_numbers = []
    for i in range(len(ticket)):
        while True:
            try:
                num = int(input(f"Выберите число из строки {i + 1} {ticket[i]}: "))
                if num in ticket[i]:
                    user_numbers.append(num)
                    break
                else:
                    print("Число не входит в строку. Попробуйте снова.")
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число.")
    return user_numbers

def generate_random_numbers():
    """Генерирует случайные числа из лотерейного билета."""
    random_numbers = []
    for row in ticket:
        random_numbers.append(random.choice(row))
    return random_numbers

def compare_numbers(user_numbers, random_numbers):
    """Сравнивает числа пользователя и случайные числа."""
    matches = set(user_numbers) & set(random_numbers)
    return matches
