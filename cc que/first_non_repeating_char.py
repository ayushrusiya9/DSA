def first_non_repeating_char(s: str):
    for char in s:
        if s.count(char) == 1:
            return char
    return None


print(first_non_repeating_char("swiss"))   
print(first_non_repeating_char("aabbcc"))  
print(first_non_repeating_char("python"))  
