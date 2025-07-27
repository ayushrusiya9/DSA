n = int(input("Enter number: "))
sum = 0

for i in range(1,n):
    if n % i == 0:
        sum = sum + i

if n == sum:
    print(f'Number {n} is pefect number.')
else:
    print(f'number {n} is not a perfect number.')