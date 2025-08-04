arr = [1,2,3,4,1,1,2,3,2]
arr1 = []

for i in arr:
    if i not in arr1:
        arr1.append(i)

print(arr1)
