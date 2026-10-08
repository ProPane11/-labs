n = int(input("Введите количество чисел: "))

count = 0
total_sum = 0

for i in range(n):
    number = int(input("Введите число: "))

    if number > 0 and number % 2 == 0:
        count += 1
        total_sum += number

print(f"Количество подходящих чисел: {count}")
print(f"Сумма подходящих чисел: {total_sum}")