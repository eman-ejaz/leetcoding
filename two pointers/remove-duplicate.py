def remove_duplicate(arr):
    l = 1

    for r in range(1, len(arr)):
        if arr[l] != arr[r - 1]:
            arr[l] = arr[r]
            l += 1

    return l


print(remove_duplicate([1, 1, 2, 3, 3, 5, 5, 6]))
