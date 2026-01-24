s = input("Enter String:")
rev_str = ""
for i in s:
    rev_str = i + rev_str

if s == rev_str:
    print("It's Palindrome")
else:
    print("It's not palindrome")

def palindrome(s):
    rev_str = ""
    for i in s:
        rev_str = i + rev_str

    if s == rev_str:
        return True
    else:
        return False
    
print(palindrome("madam"))