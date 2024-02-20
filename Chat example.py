import re

# Приклад списку номерів телефонів в різних форматах
phone_numbers = [
    "123-456-7890",
    "(123) 456 7890",
    "+1 123 456-7890",
    "123.456.7890",
    "1234567890",
    "+11234567890"
]

# Функція для нормалізації номерів телефонів
def normalize_phone_numbers(numbers):
    normalized_numbers = []
    for number in numbers:
        # Видалення всіх нецифрових символів
        clean_number = re.sub(r'\D', '', number)
        
        # Додавання форматування
        # Припускаємо, що всі номери з США (+1)
        formatted_number = f"+1 ({clean_number[0:3]}) {clean_number[3:6]}-{clean_number[6:10]}"
        
        normalized_numbers.append(formatted_number)
    return normalized_numbers

# Нормалізація номерів
normalized_numbers = normalize_phone_numbers(phone_numbers)

for number in normalized_numbers:
    print(number)
