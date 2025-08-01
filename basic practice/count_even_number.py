arr = [1,2,3,4,5,6,7,8,9]
count = 0

for i in arr:
    if i % 2 == 0:
        count = count + 1

# print(count)
print(f'{count} even numbers in this array {arr}')