v = 'aeiouAEIOU'
S = input("Enter :")

count = 0
for i in range(len(S)):
    for j in range(len(S)):
        if v[i] == S[j]:
            count+=1

vowels = count
consonant = len(S) - vowels

print("Vowels are :",vowels)
print("consonant are :",consonant)