n = int(input("Enter Number: "))

def odd_even_check(n):
    if n % 2 != 0:
        print(f'Given number {n} is odd.')
    else:
        print(f'Given number {n} is even.')
    
    return

odd_even_check(n)