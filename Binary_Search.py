# Binary Search
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6

left = 0
right = len(arr) - 1
found = False

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        print("Element", target, "found at index", mid)
        found = True
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

if not found:
    print("Element", target, "not found in the array.")
