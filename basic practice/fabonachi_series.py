# n = int(input("Enter Number: "))

# a = 0
# b = 1
# temp = 0
# print(a),print(b)

# for i in range(1, n + 1):
#     temp = a + b
#     print(temp, end=" ")
#     # a,b = b,temp
#     a = b
#     b = temp

#using while loop and witout use third veriable 

# a,b = 0,1

# while a < n:
#     print(a, end=' ')
#     a , b = b, a + b

#using for loop 
# n = int(input("Enter Number: "))

# a,b = 0,1

# for _ in range(100):
#     if a > n:
#         break

#     print(a, end=' ')
#     a,b = b, a + b


n = int(input("Enter number:"))

a = 1
b = 1
i = 1
while i <= n:
    temp = a + b
    print(a)
    a = b
    b = temp
    i = i + 1
