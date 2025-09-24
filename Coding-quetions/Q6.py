# REMOVE DUPLICATE CHARECTER

ch = input("ENTER : ")
ch1 = ""

for i in ch:
    if i not in ch1:
        ch1 = ch1 + i

print(ch1)