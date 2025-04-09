def operation_counter(operations, categories):
    count = {category: 0 for category in categories}
    for operation in operations:
        for category in categories:
            if category.lower() in operation["description"].lower():
                count[category] += 1
    return count
