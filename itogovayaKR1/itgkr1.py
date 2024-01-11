def filter_strings(arr):
    new_arr = []
    for s in arr:
        if len(s) <= 3:
            new_arr.append(s)
    return new_arr

# Примеры:
arr1 = ["Hello", "2", "world", ":-)"]
arr2 = ["1234", "1567", "-2", "computer science"]
arr3 = ["Russia", "Denmark", "Kazan"]

print(filter_strings(arr1))  # ["2", ":-)"]
print(filter_strings(arr2))  # ["-2"]
print(filter_strings(arr3))  # []