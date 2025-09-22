s1 = input("Enter First string: ")
s2 = input("Enter Second string: ")

s1 = list(s1)
s2 = list(s2)
for i in range(len(s1)-1):
    for j in range(len(s1)-1):
        if s1[j] > s1[j+1]:
            temp = s1[j]
            s1[j] = s1[j+1]
            s1[j+1] = temp
# print(s1)

for i in range(len(s2) - 1):
    for j in range(len(s2) - 1):
        if s2[j] > s2[j + 1]:
            s2[j],s2[j + 1] = s2[j + 1],s2[j]

s1 = "".join(s1)
s2 = "".join(s2)

# print(s1)
# print(s2)
if s1 == s2:
    print('Given string\'s are anagram.')
else:
    print('Given string\'s are not anagram.')