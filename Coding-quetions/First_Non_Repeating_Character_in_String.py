def first_non_repeating_char(s: str) -> str:
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch

    return "None"


print(first_non_repeating_char("swiss"))   
print(first_non_repeating_char("aabb"))    
print(first_non_repeating_char("teeter"))  