from collections import Counter

def operation_counter(operations, categories):
    count = {category: 0 for category in categories}
    counts = Counter()
    for operation in operations:
        description = operation["description"].lower()
        for category in categories:
            if category.lower() in operation["description"].lower():
                count[category] += 1
    return count
            if category.lower() in description:
                counts[category] += 1
    return counts
