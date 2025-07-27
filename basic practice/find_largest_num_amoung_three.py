first_num = int(input("Enter First Number: "))
second_num = int(input("Enter Second Number: "))
third_num = int(input("Enter Third Number: "))

def largest_num(a,b,c):
    if a > b and a > c:
        print(f'First num {a} is greater then {b} and {c}')
    elif b > a and b > c:
        print(f'Second num {b} is greater then {a} and {c}')
    else:
        print(f'First num {c} is greater then {a} and {b}')


largest_num(first_num,second_num,third_num)

# largest = max(first_num,second_num,third_num)

# print("Largest number is: ",largest)