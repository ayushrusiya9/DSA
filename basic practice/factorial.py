n = int(input("Enter Number: "))

def factorial(num):
    fact = 1

    for i in range(n,1,-1):
        fact = fact * i
    
    print(f'Factorial of a number {n} is {fact}')

factorial(n)

