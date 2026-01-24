# REMOVE DUPLICATE CHARECTER

ch = input("ENTER : ")
ch1 = ""

for i in ch:
    if i not in ch1:
        ch1 = ch1 + i

print(ch1)

def remove_duplicate_characters(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result   

print(remove_duplicate_characters("programming")) 