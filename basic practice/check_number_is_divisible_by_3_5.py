num = int(input("Enter number: "))

if num % 3 == 0 and num % 5 != 0:
    print(f'foo')
elif num % 5 == 0 and num % 3 != 0:
    print(f'bar')
elif num % 3 == 0 and num % 5 == 0:
    print(f'foo bar ')
else:
    print('Given number is not divisible by 3 and 5')