numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))
 
if len(numbers) == 0:
    print("Нет данных")
else:
    maximum = max(numbers)
    indexes = []
    for index, number in enumerate(numbers):
        if number == maximum:
            indexes.append(index)
    print(indexes)