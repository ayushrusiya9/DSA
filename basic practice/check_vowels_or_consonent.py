char = input("Enter charecter: ")

def check_vowel(c):
    if c == 'a' or c == 'A' or c == 'e' or c == 'E' or c == 'i' or c == 'I' or c == 'o' or c == 'O' or c == 'u' or c == 'U':
        print(f'Given charecter {c} is vowel.')
    else:
        print(f'Given charecter {c} is consonent.')


check_vowel(char)