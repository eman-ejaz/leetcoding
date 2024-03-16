def searchTriplet(arr, target_sum):
    arr.sort()
    result = float('inf')
    for i in range(len(arr)):
        left, right = i + 1, len(arr) - 1

        while left < right:
            target_diff = target_sum - arr[i] - arr[left] - arr[right]

            if target_diff == 0:
                return arr[i] + arr[left] + arr[right]

            if abs(target_diff) < abs(target_sum - result):
                result = abs(target_diff)

            if target_diff > 0:
                left += 1
            else:
                right -= 1

    return target_sum - result


print(searchTriplet([-3, -1, 1, 2], 3))
