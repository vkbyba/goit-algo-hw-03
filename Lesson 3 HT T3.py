import re
phone_numbers = [
"    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   "]
def sanitized_numbers(nums):
    sanitized = []
    for num in nums:
        clean_number = re.sub(r'\D', '',num)
        formatted_number = f"+38{clean_number[-9:]}"
        sanitized.append(formatted_number)
    return sanitized
sanitized_list = sanitized_numbers(phone_numbers)
print("Нормалізовані номери телефонів для SMS-розсилки:", ", ".join(sanitized_list))