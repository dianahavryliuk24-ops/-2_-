# Завдання 8. Конвертер секунд

total_seconds = int(input("Введіть кількість секунд: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"\nГодини: {hours}")
print(f"Хвилини: {minutes}")
print(f"Секунди: {seconds}")