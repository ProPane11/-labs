attempts = 0

number = int(input("Введите положительное число: "))

while number <= 0:
    attempts += 1
    print("Число должно быть положительным.")

    number = int(input("Введите положительное число: "))


square = number ** 2
print(f"Число: {number}")
print(f"Квадрат числа: {square}")
print(f"Количество отклонённых попыток: {attempts}")