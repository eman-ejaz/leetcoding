def contains_duplicate_brute_force(nums):
    nums_freq = {}

    for i in range(len(nums)):
        if nums[i] not in nums_freq:
            nums_freq[nums[i]] = 0

        nums_freq[nums[i]] = nums_freq[nums[i]] + 1

        if nums_freq[nums[i]] > 1:
            return True

    return False


print(contains_duplicate_brute_force([1, 2, 3, 1]))
