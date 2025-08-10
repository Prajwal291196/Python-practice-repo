# # Day 8–9: Algorithms
# # Searching (linear, binary)

# # Sorting (built-in & custom key functions)

# # Problem: Duplicate Finder

# # provide me a List for the above problem

# numbers = [5, 3, 8, 3, 9, 1, 5, 2, 7, 8, 10, 15, 2, 18, 20, 7, 25, 30, 18]
# duplicate_numbers = []

# def search_sort():
#     # sort the list in ascending order
#     numbers.sort()
#     # print the sorted list
#     print(numbers)
#     # search for duplicates in the sorted list
#     for i in range(len(numbers) - 1):
#         if numbers[i] == numbers[i + 1]:
#             print(f"Duplicate found: {numbers[i]}")
#             # remove the duplicate from the list
#             duplicate_numbers.append(numbers.pop(i))
#             # print the updated list
#             print(numbers)
#             search_sort()
#             break
        
# if __name__ == "__main__":
#     search_sort()
#     print(f"Duplicate numbers: {duplicate_numbers}")

from collections import Counter

# Original list
numbers = [5, 3, 8, 3, 9, 1, 5, 2, 7, 8, 10, 15, 2, 18, 20, 7, 25, 30, 18]

# Step 1: Find duplicates
counts = Counter(numbers)
print("counts",counts)
duplicates = [num for num, count in counts.items() if count > 1]

# Step 2: Remove duplicates and sort
unique_sorted = sorted(set(numbers))

# Step 3: Binary search function
def binary_search(arr, target):
    low, high   = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Output
print("Duplicates found:", duplicates)
print("Unique sorted list:", unique_sorted)

# Step 4: Search test
search_num = 16
if binary_search(unique_sorted, search_num):
    print(f"{search_num} found in the list!")
else:
    print(f"{search_num} not found in the list.")
