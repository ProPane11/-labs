# Запрос данных

# region

subject1 = input("Введите название 1-го предмета: ")
lessons1 = int(input(f"Количество занятий в неделю по предмету '{subject1}': "))
duration1 = int(input(f"Продолжительность одного занятия по предмету '{subject1}' (в минутах): "))
subject2 = input("Введите название 2-го предмета: ")
lessons2 = int(input(f"Количество занятий в неделю по предмету '{subject2}': "))
duration2 = int(input(f"Продолжительность одного занятия по предмету '{subject2}' (в минутах): "))
available_hours = float(input(f"Введите доступное время на неделю в часах: "))

# endregion

# Вычисления

# region

time_sub1_min = lessons1 * duration1
time_sub2_min = lessons2 * duration2
total_workload_min = time_sub1_min + time_sub2_min
total_workload_hours = total_workload_min / 60
free_time_hours = available_hours - total_workload_hours
workload_4_weeks_hours = total_workload_hours * 4

# endregion

# Вывод результатов

# region

print("\n" + "="*40)
print("           АНАЛИЗ УЧЕБНОЙ НАГРУЗКИ           ")
print("="*40)
print(f"Время на предмет '{subject1}': {time_sub1_min} мин.")
print(f"Время на предмет '{subject2}': {time_sub2_min} min.")
print("-"*40)
print(f"Общая нагрузка за неделю: {total_workload_min} мин. ({total_workload_hours:.2f} ч.)")
print(f"Остаток свободного времени: {free_time_hours:.2f} ч.")
print(f"Общая нагрузка за 4 недели: {workload_4_weeks_hours:.2f} ч.")
print("="*40)
