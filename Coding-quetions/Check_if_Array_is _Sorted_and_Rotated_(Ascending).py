def is_sorted_and_rotated(nums):
    n = len(nums)
    if n <= 1:
        return True  

    drops = 0  
    
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            drops += 1
            if drops > 1:
                return False

    return True


# Tests
print(is_sorted_and_rotated([3, 4, 5, 1, 2]))  
print(is_sorted_and_rotated([2, 1, 3, 4]))     
print(is_sorted_and_rotated([1, 2, 3, 4]))     
print(is_sorted_and_rotated([2, 3, 4, 1]))     

