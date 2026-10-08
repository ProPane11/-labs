total = int(input("Введите общее количество игрушек: "))
capacity = int(input("Введите количество игрушек в одном наборе: "))

full_sets = total // capacity
remainder = total % capacity
sets_needed = (total + capacity - 1) // capacity

print(f"Полностью заполненных наборов: {full_sets}")
print(f"Осталось игрушек: {remainder}")
print(f"Минимальное количество наборов: {sets_needed}")