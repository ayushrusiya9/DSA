# num = int(input("Enter Number: "))

# #this is fast
# def is_prime(num):
#     if num <= 1:
#         return False
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     for i in range(3,num,2):
#         if num % i == 0:
#             return False

#     return True

# prime = is_prime(num)

# if prime == True:
#     print(f'Given number {num} is prime number.')
# else:
#     print(f'Given number {num} is not a prime number.')


#this is slow
# def is_prime(num):
#     if num <= 1:
#         return False
    
#     for i in range(3,num,2):
#         if num % i == 0:
#             return False
    
#     return True

def PrimeNum(n):
    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    for i in range(3, num, 2):
        if n % i == 0:
            return False
        return True

            
        
        
num = int(input("Enter Number: "))

print(PrimeNum(num))


# if :
#     print(f"Given NUMBER {num} is a prime number.")
# else:
#     print(f"Given number {num} is not a prime number")