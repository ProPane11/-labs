n = int(input("Введите количество чисел: "))

total_sum = 0
positive_count = 0

number = int(input("Введите число: "))
total_sum += number

if number > 0:
    positive_count += 1

maximum = number


for i in range(n - 1):
    number = int(input("Введите число: "))

    total_sum += number

    if number > 0:
        positive_count += 1

    if number > maximum:
        maximum = number


print("\nРезультат:")
print(f"Сумма чисел: {total_sum}")
print(f"Количество положительных чисел: {positive_count}")
print(f"Максимальное число: {maximum}")