# Linear Search
arr = [5, 2, 8, 1, 6]
target = 8

found = False
for i in range(len(arr)):
    if arr[i] == target:
        print("Element", target, "found at index", i)
        found = True
        break

if not found:
    print("Element", target, "not found in the array.")
