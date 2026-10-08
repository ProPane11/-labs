price = int(input("Введите цену одной тетради: "))

if price < 0:
    print("Ошибка: Цена не может быть отрицательной.")
    exit()

count = int(input("Введите количество тетрадей: "))

if count < 0:
    print("Ошибка: Количество не может быть отрицательным.")
    exit()

paid = int(input("Введите внесённую сумму: "))

cost = price * count
change = paid - cost

print(f"Стоимость покупки: {cost} руб.")
print(f"Сдача: {change} руб.")