def makeSquares(arr):
    l, r = 0, len(arr) - 1

    result = [0] * len(arr)

    for i in range(len(result) - 1, -1, -1):
        if arr[l] ** 2 > arr[r] ** 2:
            result[i] = arr[l] ** 2
            l += 1
        else:
            result[i] = arr[r] ** 2
            r -= 1

    return result


print(makeSquares([-3, -1, 0, 1, 2]))
