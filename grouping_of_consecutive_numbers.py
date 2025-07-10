def group_consecutive(nums):
    print("nums before sorting:", nums)
    if not nums:
        return []

    nums.sort()  # Optional: ensures the list is sorted
    print("nums after sorting:", nums)
    result = []
    group = [nums[0]]
    print(type(group))

    for i in range(1, len(nums)):
        print("nums[i]:",nums[i])
        print("nums[i-1]", nums[i-1])
        print("nums[i - 1] + 1",nums[i - 1] + 1)
        if nums[i] == nums[i - 1] + 1:

            group.append(nums[i])
            print("groups",group)
        else:
            result.append(group)
            print("result", result)
            group = [nums[i]]

    result.append(group)  # Append the last group
    return result

# Example usage:
numbers = [1, 2, 3, 5, 6, 9, 10, 11, 15]
print(group_consecutive(numbers))
