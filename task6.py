# Завдання 6. Конвертер часу

total_minutes = int(input("Введіть кількість хвилин: "))

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"\nГодини: {hours}")
print(f"Хвилини: {minutes}")