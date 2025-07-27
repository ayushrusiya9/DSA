l = [2,0,4,0,6,0,8]

# for i in range(len(l)):
#     swapped = 0
#     for j in range(len(l)-1):
#         if l[j] < l[j + 1]:
#             l[j],l[j + 1] = l[j + 1],l[j]
#             swapped = 1
    
#     if swapped == 0:
#         break

l1 = []
for i in l:
    if i != 0:
        l1.append(i)

n = len(l) - len(l1)
for _ in range(n):
    l1.append(0)

print(l1)