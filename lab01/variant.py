order_name = input("Название заказа: ")
name_client = input("Имя заказчика: ")
item1_name = input("Название первой позиции: ")
item1_quantity = int(input(f"Количество '{item1_name}': "))
item1_price = float(input(f"Цена одной единицы '{item1_name}' (руб.): "))
item2_name = input("Название второй позиции: ")
item2_quantity = int(input(f"Количество '{item2_name}': "))
item2_price = float(input(f"Цена одной единицы '{item2_name}' (руб.): "))
delivery = float(input("Стоимость доставки (руб.): "))
paid = float(input("Внесённая сумма (руб.): "))
offpriceinput = int(input('Введите размер скидки от 0 до 100: '))
item1_cost = item1_quantity * item1_price
item2_cost = item2_quantity * item2_price
goods_total = item1_cost + item2_cost
discount = goods_total * (offpriceinput / 100)
goods_with_discount =goods_total-discount
total_with_delivery =goods_with_discount + delivery
all_count = item1_quantity + item2_quantity
change = paid - total_with_delivery


print(f"Номер заказа: {order_name}")
print(f"Заказчик: {name_client}")
print(f"{item1_name} | {item1_quantity} | {item1_price:.2f} | {item1_cost:.2f}")
print(f"{item2_name} | {item2_quantity} | {item2_price:.2f} | {item2_cost:.2f}")
print(f"Стоимость товаров без доставки: {goods_total:.2f}")
print(f"Скидка ({offpriceinput}%): {discount:.2f} руб.")
print(f"Стоимость товаров со скидкой: {goods_with_discount:.2f}")
print(f"Стоимость с доставкой (Итого к оплате): {total_with_delivery:.2f}")
print(f"Общее количество единиц: {all_count}")
print(f"Сдача: {change:.2f}")