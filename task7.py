# Завдання 7. Робота з трицифровим числом

number = int(input("Введіть трицифрове число: "))

hundreds = number // 100
tens = (number // 10) % 10
units = number % 10
total_sum = hundreds + tens + units

print(f"\nСотні: {hundreds}")
print(f"Десятки: {tens}")
print(f"Одиниці: {units}")
print(f"Сума цифр: {total_sum}")