def reverse(s):
    s1 = ''
    for i in s:
        s1 = i + s1
    return s1


s = "ayush"
print(reverse(s))