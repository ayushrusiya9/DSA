num = int(input("Enter Number: "))

check_num = num
sum = 0

while num > 0:
    last_digit = num % 10
    sum = (sum * 10)  + last_digit
    num = num // 10    

if check_num == sum:
    print(f'{check_num} is palindrome')
else:
    print(f'{check_num} is not palindrome')
