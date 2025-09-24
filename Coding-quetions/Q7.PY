# find most frequent character

ch = input("Enter Value: ")

count = 1
most_freq = ''

for i in ch:
    freq = ch.count(i)
    if freq > count:
        count = freq
        most_freq = i
    
print(most_freq)