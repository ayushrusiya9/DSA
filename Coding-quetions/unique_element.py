def unique_elements(nums):
    seen = set()
    result = []
    for n in nums:
        if n not in seen:
            result.append(n)
            seen.add(n)
    return result


print(unique_elements([4, 5, 4, 2, 5, 7, 2]))

