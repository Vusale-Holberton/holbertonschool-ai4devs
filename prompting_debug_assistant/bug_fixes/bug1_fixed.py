def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

my_list = [10, 20, 30, 40, 50]
result = calculate_average(my_list)
print(f"The average is: {result}")