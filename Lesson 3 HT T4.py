from datetime import datetime,timedelta

users = [
    {"name": "John Doe", "birthday": "1985.02.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
birthdays = [user["birthday"] for user in users]

def get_upcoming_birthday(users):
    today = datetime.today().date()
    date_in_a_week = today + timedelta(days=7)
    upcoming_birthdays = []
    for user in users:
        birthday_str = user["birthday"]
        birthday = datetime.strptime(birthday_str, "%Y.%m.%d")
        birthday_this_year = birthday.replace(year=today.year).date()
        if today <= birthday_this_year <= date_in_a_week:
            upcoming_birthdays.append(user)
    
    return upcoming_birthdays
upcoming_birthdays = get_upcoming_birthday(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
