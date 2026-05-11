def process_numbers(data):
    if not data:
        return 0
    
    total = 0
    count = 0
    for value in data:
        total += value
        count += 1
    
    result = total / count
    return result

values = [15, 25, 35, 45, 55]
final_score = process_numbers(values)
print(f"Processing complete. Average score: {final_score}")

empty_data = []
print(f"Empty list result: {process_numbers(empty_data)}")