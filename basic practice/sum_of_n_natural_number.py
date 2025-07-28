# n = int(input("Enter Number: "))

# def sum_n_natural_num(n):
    
#     sum = 0
#     for i in range(1, n + 1):
#         sum = sum + i
#         if i < n:
#             print(i, end=' + ')
#         else:
#             print(i, end=' = ')
    
#     # print(sum)
#     return sum

# s = sum_n_natural_num(n)

# print(s)

n = int(input("Enter Number: "))

def SumOfNaturalNum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    
    return sum

nat = SumOfNaturalNum(n)
print(nat)