# # phle nikalne wala code for prectice/
# num = input("Enter number: ")

# if num.isdigit():
#     num_of_digit = len(num)
#     number = int(num)
#     divisor = 10 ** (num_of_digit - 1)
#     result = number // divisor
#     print(f'First digit is {result}')
#     print('Last digit is ', number % 10)
# else:
#     print('inalid input!')

#actual using list
# n = input("Enter number: ")

# if n.isdigit():
#     num = list(n)
#     num[0],num[-1] = num[-1],num[0]
#     # print(num)
#     swap_digit = int(''.join(map(str, num)))
#     print(f'swaped digit is {swap_digit}')
# else:
#     print("invalid input!")

#using string

n = input("Enter number: ")

if n.isdigit():
    num = n[-1] + n[1:-1] + n[0]
    number = int(num)
    print("swaped number is ", number)
else:
    print("invalid input")