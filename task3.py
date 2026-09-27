# Завдання 3. Покупка в магазині

item_name = input("Назва товару: ")
price = float(input("Ціна: "))
quantity = int(input("Кількість: "))

total_cost = price * quantity

print("\n------ ЧЕК ------")
print(f"Товар: {item_name}")
print(f"Ціна: {price} грн")
print(f"Кількість: {quantity}")
print(f"До сплати: {total_cost} грн")
print("-----------------")