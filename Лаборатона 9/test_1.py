def user_input():
    str=input('input your string: ')
    return str

def output():
    print (str)

def search_min(number_words, words ):
    min=int(words[0])
    minIndex = 0
    for i in range (1, number_words):
        if min>int(words[i]):
           min=int(words[i])
           minIndex = i
    return minIndex

def search_max(number_words, words ):
    max=int(words[0])
    maxIndex = 0
    for i in range (1, number_words):
        if max<int(words[i]):
           max=int(words[i])
           maxIndex = i
    return maxIndex