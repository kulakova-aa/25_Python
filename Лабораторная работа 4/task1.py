
import json

def task(json_filename):
    with open(json_filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    total_sum = 0.0
    for item in data:
        score = item.get('score', 0)
        weight = item.get('weight', 0)
        total_sum += score * weight

    return round(total_sum, 3)

print(task('input.json'))