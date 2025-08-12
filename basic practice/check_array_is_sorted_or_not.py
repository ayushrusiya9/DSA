# Write a program to check if array is sorted.

def sortedArr(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# a = sortedArr([1,2,3,4,5])
a = sortedArr([3,2,3,4,5])

if a :
    print("Array are soted")
else:
    print("Array are not sorted")