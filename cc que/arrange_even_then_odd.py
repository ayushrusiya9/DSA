l = [2,1,3,8,4,8,5]
l1 = []
for i in l:
    if i % 2 == 0:
        l1.append(i)
    
for i in l:
    if i % 2 != 0:
        l1.append(i)

print(l1)