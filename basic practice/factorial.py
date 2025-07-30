# n = int(input("Enter Number: "))

# def factorial(num):
#     fact = 1

#     for i in range(n,1,-1):
#         fact = fact * i
    
#     print(f'Factorial of a number {n} is {fact}')

# factorial(n)



n = int(input("Enter Number: "))

f = 1
# i = n
while(n > 0):
    f = f * n
    n = n - 1

print(f)