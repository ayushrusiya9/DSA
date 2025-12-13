def second_largest(arr):
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second if second != float('-inf') else None

arr = [10, 5, 20, 20, 8]
print(second_largest(arr))
