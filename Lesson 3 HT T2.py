import random

def get_valid_input(prompt, low=None, high=None):
    while True:
        try:
            value = int(input(prompt))
            if (low is not None and value < low) or (high is not None and value > high):
                print(f"Please enter a value between {low} and {high}.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")

k = 5

min_value = get_valid_input("Enter MIN value of range (greater than 1 and less then 996): ", 2, 996)
max_value = get_valid_input(f"Enter MAX value of range (less than 1000 and greater than {min_value}): ", min_value + 1, 999)

if max_value - min_value + 1 < k:
    print(f"There are not enough integers in the indicated range to select {k} unique numbers. Please adjust your range.")
else:
    lottery_numbers = random.sample(range(min_value, max_value + 1), k)
    print("Your lottery numbers:", lottery_numbers)
