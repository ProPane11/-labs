subject1 = input("Введите название первого предмета: ")
lessons1 = int(input(f"Количество занятий в неделю по предмету '{subject1}':  "))
if lessons1 < 0:
    print("Ошибка: Количество занятий не может быть отрицательным.")
duration1 = int(input(f"Продолжительность одного занятия по предмету '{subject1}' в минутах: "))
if duration1 <= 0:
    print("Ошибка: Продолжительность занятия должна быть положительной")
subject2 = input("Введите название второго предмета: ")
lessons2 = int(input(f"Количество занятий в неделю по предмету '{subject2}': "))
if lessons2 < 0:
    print("Ошибка: Количество занятий не может быть отрицательным.")
duration2 = int(input(f"Продолжительность одного занятия по предмету '{subject2}' в минутах: "))
if duration2 <= 0:
    print("Ошибка: Продолжительность занятия должна быть положительной.")
time_available = float(input("Введите количество часов, доступных для подготовки в неделю: "))
time1 = lessons1 * duration1
time2 = lessons2 * duration2
total_minutes = time1 + time2
total_hours = total_minutes / 60
free_hours = time_available - total_hours
four_weeks= total_hours * 4
if time_available < total_hours:
    print("Недостаточно времени для подготовки по обоим предметам.")
else: 
    print ()
    print("Учебная нагрузка по предметам:")
    print(f"{subject1}: {time1} минут")
    print(f"{subject2}: {time2} минут")
    print(f"Общее количество минут подготовки: {total_minutes} минут")
    print(f"Общая учебная нагрузка: {total_hours:.2f} часов")
print(f"Свободное время: {free_hours:.2f} часов")
print(f"Учебная нагрузка за 4 недели: {four_weeks:.2f} часов")



