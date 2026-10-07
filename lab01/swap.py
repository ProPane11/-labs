first_room = input("Введите первую аудиторию: ")
second_room = input("Введите вторую аудиторию: ")
print(f"Исходные значения: первая аудитория — {first_room}, вторая аудитория — {second_room}")
temp = first_room
first_room = second_room
second_room = temp
print(f"После обмена: первая аудитория — {first_room}, вторая аудитория — {second_room}")