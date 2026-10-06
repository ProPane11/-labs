surname = input("Фамилия: ")
name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст: "))
if age < 1 or age > 120:
    print("Ошибка:возраст должен быть от 1 до 120")
    exit()
subject = input("Любимый предмет: ")
study_hours = float(input("Часов подготовки в неделю: "))
if study_hours < 0:
    print("Ошибка:Количество часов не может быть отрицательным")
    exit()
age_after_4_years = age + 4
hours_for_4_weeks = study_hours * 4
hours_per_day = study_hours / 7
print()
print("Карточка студента")
print(f"Имя и фамилия: {name} {surname}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст: {age}")
print(f"Возраст через 4 года: {age_after_4_years}")
print(f"Любимый предмет: {subject}")
print(f"Подготовка за неделю: {study_hours:.2f} ч")
print(f"Подготовка за 4 недели: {hours_for_4_weeks:.2f} ч")
print(f"Подготовка в среднем за день: {hours_per_day:.2f} ч")