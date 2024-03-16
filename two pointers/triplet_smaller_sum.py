def triplet_smaller(arr, target_sum):
    arr.sort()
    result = 0

    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1

        while left < right:
            s = arr[i] + arr[left] + arr[right]

            if target_sum >= s:
                result += right - left
                left += 1

            if s > target_sum:
                right -= 1

    return result


print(triplet_smaller([-1, 0, 2, 3], target_sum=3))
