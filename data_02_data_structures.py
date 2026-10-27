
# Example order data created for practice
order_statuses = [
    "completed",
    "pending",
    "completed",
    "cancelled",
    "pending",
    "completed",
    "pending",
    "completed",
    "cancelled",
]

customer_ids = [201, 202, 201, 203, 202, 204, 201]
unique_customer_ids = set(customer_ids)

print("Unique customer IDs:", unique_customer_ids)
print("Number of unique customers:", len(unique_customer_ids))


def linear_search(items, target):
    """Return the index of target, or -1 if it is absent."""

    for index, item in enumerate(items):
        if item == target:
            return index

    return -1


customer_ids = [201, 202, 204, 203, 205]

print(linear_search(customer_ids, 203))
print(linear_search(customer_ids, 999))

customer_ids = [201, 202, 203, 204, 205, 206, 207]

def binary_search(sorted_items, target):
    """Find target in ascending sorted data; return its index or -1."""

    left = 0
    right = len(sorted_items) - 1

    while left <= right:
        middle = (left + right) // 2
        current = sorted_items[middle]

        if current == target:
            return middle

        elif current < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1


sorted_customer_ids = [201, 202, 203, 204, 205, 206, 207]

print(binary_search(sorted_customer_ids, 206))
print(binary_search(sorted_customer_ids, 200))
customer_ids = [201, 202, 201, 203, 202, 204, 201]

def unique_preserving_order(items):
    """Remove duplicates while keeping first occurrences."""

    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


customer_ids = [201, 202, 201, 203, 202, 204, 201]

print(unique_preserving_order(customer_ids))

# Start with an empty dictionary
status_counts = {}

# Count how many times each status appears
for status in order_statuses:
    if status in status_counts:
        status_counts[status] += 1
    else:
        status_counts[status] = 1


print("Orders by status:")
print(status_counts)
{
    "completed": 3,
    "pending": 3,
    "cancelled": 1
}

