n = int(input("Enter number: "))
# s = 'A'
# # print(ord(s))
# print(chr(s))
for _ in range(0, n):
    S = 'A'
    for j in range(1,n + 1):
        print(S, end=" ")
        S = chr(ord(S) + 1)
    print()
