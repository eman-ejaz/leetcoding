def contains_duplicate_brute_force(nums):
    nums_freq = {}

    for i in range(len(nums)):
        if nums[i] not in nums_freq:
            nums_freq[nums[i]] = 0

        nums_freq[nums[i]] = nums_freq[nums[i]] + 1

        if nums_freq[nums[i]] > 1:
            return True

    return False


def contains_duplicate_brute_force2(nums):
    s = set()

    for num in nums:
        s.add(num)

    return len(s) != len(nums)


print(contains_duplicate_brute_force2([1, 2, 3, 4]))
