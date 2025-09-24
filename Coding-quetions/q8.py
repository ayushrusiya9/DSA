#COUNT HOW many words in a sentance

def countWord(sentance):
    words_list = sentance.split()
    words_count = len(words_list)
    print(words_count, 'is total word\' in a sentance.')
    return 

countWord(input("Enter sentance: "))