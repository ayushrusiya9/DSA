arr = [1,22,3,4,87,6,7,83]

max_value = arr[0]

for i in arr:
    if max_value < i:
        max_value = i

print(max_value)