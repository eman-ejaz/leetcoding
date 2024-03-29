def reverseVowels(s: str) -> str:
    char_index_map = {}
    vowels = ['a', 'e', 'i', 'o', 'u']

    result = []

    chars = []
    vowels_positions = []

    for index, char in enumerate(s):
        if char.lower() in vowels:
            chars.append(char)
            vowels_positions.append(index)

    j = len(chars) - 1

    for i in range(len(s)):
        if i in vowels_positions:
            result.append(chars[j])
            j -= 1
        else:
            result.append(s[i])

    return ''.join(result)


def reverseVowelsOpt(s: str):
    a = 0
    b = len(s) - 1

    sList = list(s)

    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    while a < b:
        if sList[a] in vowels and sList[b] in vowels:
            sList[a], sList[b] = sList[b], sList[a]

            a += 1
            b -= 1

        elif sList[a] not in vowels:
            a += 1

        elif sList[b] not in vowels:
            b -= 1

    return ''.join(sList)


def reverseVowels2(s: str) -> str:
    # Convert the string to a list to allow modification.
    chars = list(s)
    # Define a set of vowels for O(1) lookup time.
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    # Initialize two pointers.
    left, right = 0, len(s) - 1

    # Use two-pointer technique to find and swap vowels.
    while left < right:
        # Move the left pointer until a vowel is found.
        while left < right and chars[left] not in vowels:
            left += 1
        # Move the right pointer until a vowel is found.
        while right > left and chars[right] not in vowels:
            right -= 1
        # Swap the vowels.
        chars[left], chars[right] = chars[right], chars[left]
        # Move pointers towards the center.
        left, right = left + 1, right - 1

    # Convert the list back to a string and return it.
    return ''.join(chars)

# Example usage
print(reverseVowels("hello"))  # Should print "holle"
print(reverseVowels("leetcode"))  # Should print "leotcede"


print(reverseVowelsOpt('DesignGUrus'))
