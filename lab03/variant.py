signal = int(input("Введите уровень сигнала от 0 до 100: "))

if signal < 0 or signal > 100:
    print("Ошибка диапазона")

elif signal <= 34:
    print("Слабый")

elif signal <= 74:
    print("Средний")

else:
    print("Сильный")