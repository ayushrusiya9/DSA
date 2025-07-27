n = int(input("Enter number: "))

for i in range(1,n+1):
    ch = 'A'
    for j in range(1,i + 1):
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)
    print()
