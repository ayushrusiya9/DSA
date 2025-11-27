def group_consecutive(nums):
    if not nums:
        return []

    nums.sort()                
    result = []
    group = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            group.append(nums[i])
        else:
            result.append(group)
            group = [nums[i]]

    result.append(group)
    return result


arr = [1, 2, 3, 7, 8, 10, 11, 12, 20]
print(group_consecutive(arr))
