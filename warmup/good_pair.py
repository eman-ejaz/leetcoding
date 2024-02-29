def numGoodPairs(nums):
    pairCount = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                pairCount += 1
    return pairCount



print(numGoodPairs([1, 1, 1, 1]))
