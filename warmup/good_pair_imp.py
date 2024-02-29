def numGoodPairs(nums):
    numOfPairs = 0
    map = {}

    for num in nums:
        if num in map:
            numOfPairs += map[num]
        map[num] = map.get(num, 0) + 1

    return numOfPairs


print(numGoodPairs([1, 1, 1, 1]))
