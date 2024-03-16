def find_non_dups(arr):
    next_unique = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[next_unique] = arr[i]
            next_unique += 1

    return arr


print(find_non_dups([2, 3, 3, 3, 6, 9, 9]))
