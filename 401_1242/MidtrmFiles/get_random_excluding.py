import random

def get_random_excluding(input_number):
    if input_number not in [0, 1, 2, 3]:
        raise ValueError("Input number must be 0, 1, 2, or 3")
    numbers = [0, 1, 2, 3]
    numbers.remove(input_number)
    return random.choice(numbers)

# Creating 4 test cases for each input number (0, 1, 2, 3)
test_results = {}
for input_number in [0, 1, 2, 3]:
    test_results[input_number] = [get_random_excluding(input_number) for _ in range(4)]

print(test_results)
