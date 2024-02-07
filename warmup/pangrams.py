def checkIfPangram(sentence: str):
    unique_chars = set()

    for char in sentence.lower():
        if char.isalpha():
            unique_chars.add(char)

    return len(unique_chars) == 26




print(checkIfPangram("TheQuickBrownFoxJumpsOverTheLazyDog"))

# Test case 2: "This is not a pangram"
# Expected output: False
print(checkIfPangram("This is not a pangram"))
