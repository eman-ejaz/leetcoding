def search(arr, target_sum):
    left, right = 0, len(arr) - 1

    while left < right:
        if arr[left] + arr[right] == target_sum:
            return [left, right]
        elif arr[left] + arr[right] > target_sum:
            right -= 1
        else:
            left += 1

    return [-1, -1]


def search_hash_table(arr, target):
    nums = {}

    for i, num in enumerate(arr):
        if target - num in nums:
            return [i, nums[target - num]]

        nums[num] = i

    return [-1, -1]


print(search_hash_table([2, 5, 9, 11], 11))
