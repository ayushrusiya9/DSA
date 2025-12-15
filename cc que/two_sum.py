def two_sum(nums, target):
    seen = {}   # number : index

    for i, num in enumerate(nums):
        need = target - num

        if need in seen:
            return [seen[need], i]

        seen[num] = i
