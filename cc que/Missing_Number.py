def missing_number(nums):
    n = len(nums)
    x = 0
    for i in range(n+1):
        x ^= i
    for v in nums:
        x ^= v
    return x

print(missing_number([3,0,1]))  
