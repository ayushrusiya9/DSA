n = int(input("Enter any number: "))

def table(x):
    for i in range(1, 11):
        print(f'{x} x {i}  = {x * i}')
    
    return

table(n)