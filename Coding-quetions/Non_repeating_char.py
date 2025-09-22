s = input("Enter str: ")

# for i in range(len(s)):
#     count = 0
#     for j in range(len(s)):
#         if s[i] == s[j]:
#             count+= 1
#     if count == 1:
#         print(s[i])
#         break;
# else:
#     print("String have no repeating charcter")

for ch in range(len(s)):
    if  s.count(s[ch]) == 1:
        print(s[ch])
        break;
else:
    print("string have no repeating character.")
