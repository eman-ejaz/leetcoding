def triplets(arr):
    result = []
    arr.sort()

    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        num_to_find = -arr[i]

        left, right = i + 1, len(arr) - 1

        while left < right:
            if arr[left] + arr[right] == num_to_find:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while right > left and arr[right] == arr[right + 1]:
                    right -= 1

            elif arr[left] + arr[right] > num_to_find:
                right -= 1

            else:
                left += 1

    return result


print(triplets([-1,0,1,2,-1,-4]))
