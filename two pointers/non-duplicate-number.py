def remove(arr):

    l = 1

    for r in range(1, len(arr)):
        if arr[r] != arr[r -1]:
            arr[l] = arr[r]
            l += 1

    return l


print(remove([2, 3, 3, 3, 6, 9, 9]))
