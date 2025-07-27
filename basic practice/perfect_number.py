n = int(input("Enter Number: "))

def perfect_num(x):
    sum = 0
    for i in range(1, n+1):
        if i < x:
            if x % i == 0:
                # print(i)
                sum = sum + i
    
    return sum

result = perfect_num(n)

if n == result:
    print(f'Given number {n} is perfect number.')
else:
    print(f'Given number {n} is not perfect number')  