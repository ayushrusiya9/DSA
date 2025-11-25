def find_dup(nums):
    f = {}     
    d = []     
    
    for n in nums:
        if n in f:
            f[n] += 1
        else:
            f[n] = 1

    for k in f:
        if f[k] > 1:
            d.append(k)
    
    return d


print(find_dup([1,5,2,5,1,3,4,3,3]))
