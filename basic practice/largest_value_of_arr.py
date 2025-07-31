arr = [11,2,3,4,56,6,7,8,9,10]

largest_value = arr[0]

for i in arr:
    if largest_value < i:
        largest_value = i

print(largest_value)