import string

def count_unique(sentence):
    for p in string.punctuation:
        sentence = sentence.replace(p, "")
    
    words = sentence.lower().split()
    return len(set(words))

print(count_unique("Hello, hello! World... world?"))
