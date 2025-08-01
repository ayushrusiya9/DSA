arr = [3,2,3,4,5,6,7,8,9,1]

min_value = arr[0]

for i in arr:
    if min_value > i:
        min_value = i

print(min_value)