arr = [1,2,3,4,5,6,7,9,2,1]

count = 0

for i in arr:
    if i % 2 != 0:
        count = count + i

print(count)