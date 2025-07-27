n = 123456

# temp = n
# count = 0
# while temp > 0:
#     temp = temp // 10
#     count = count + 1

# # print(count)

# first_digit = n // (10 ** (count - 1))
# last_digit = n % 10

# # print(first_digit)
# # print(last_digit)

# middle = (n % (10 ** (count - 1))) // 10
# # print(middle)

# swapped_digit = last_digit * (10 ** (count - 1)) + middle * 10 + first_digit

# print(swapped_digit)

s = str(n)
l = list(s)
l[0],l[-1] = l[-1],l[0]
s = ''.join(l)
n = int(s)
print(n)