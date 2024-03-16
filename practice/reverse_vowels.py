def reverse_vowels(s: str):
    s = list(s)
    left, right = 0, len(s) - 1
    vowels = ['a', 'e', 'i', 'o', 'u']
    while left < right:
        if s[left].isalpha() and s[left].lower() not in vowels:
            left += 1

        if s[right].isalpha() and s[right].lower() not in vowels:
            right -= 1

        if (s[left].isalpha() and s[left].lower() in vowels) and (s[right].isalpha() and s[right].lower() in vowels):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return ''.join(s)


print(reverse_vowels('DesignGurus'))
