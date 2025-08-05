arr = [2,12,12,43,33,65,32]

for i in range(0, len(arr)):
    for j in range(0, len(arr) - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1],arr[j]

print(arr[-2])