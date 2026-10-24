numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))
 
result = []
for number in numbers:
    result.append(abs(number))
 
print(f"Исходный список: {numbers}")
print(f"Новый список: {result}")
