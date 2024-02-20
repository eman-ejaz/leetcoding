def shortestDistance(words, word1, word2):
    min_dist = float('inf')
    p1, p2 = -1, -1

    for index, word in enumerate(words):
        if word == word1:
            p1 = index
        elif word == word2:
            p2 = index

        if (p1 != -1 and p2 != -1):
            min_dist = min(min_dist, abs(p1 - p2))

    return min_dist


print(shortestDistance(["cat", "dog", "mouse", "elephant", "lion", "tiger", "bear", "cat"], 'cat', 'tiger'))
