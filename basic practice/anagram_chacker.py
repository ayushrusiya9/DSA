def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Compare sorted strings
    return sorted(str1) == sorted(str2)


# Example usage
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if is_anagram(word1, word2):
    print(" Yes, they are anagrams!")
else:
    print(" No, they are not anagrams.")
