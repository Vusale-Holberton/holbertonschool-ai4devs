def process_numbers(data):
    total = 0
    count = 0
    for value in data:
        total += value
        count += 1
    
    result = total / count 
    return result

values = [15, 25, 35, 45, 55]
final_score = process_numbers(values)
print("Processing complete.")
print("Average score: " + final_score)

empty_data = []
print(process_numbers(empty_data))