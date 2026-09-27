# Завдання 9. Мініпроєкт «Замовлення»

buyer = input("Ім'я покупця: ")
item_name = input("Назву товару: ")
price = float(input("Ціна одного товару: "))
quantity = int(input("Кількість: "))
money_given = float(input("Суму грошей покупця: "))

total_cost = price * quantity
change = money_given - total_cost

print("\n========== ЗАМОВЛЕННЯ ==========")
print(f"Покупець: {buyer}")
print(f"Товар: {item_name}")
print(f"Ціна: {price} грн")
print(f"Кількість: {quantity}")
print(f"\nЗагальна вартість: {total_cost} грн")
print(f"Внесено: {money_given} грн")
print(f"Решта: {change} грн")
print("===============================")