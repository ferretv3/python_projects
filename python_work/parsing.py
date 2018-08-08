import operator

def parsing_bullshit(word):
    d = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for index,letter in enumerate(alphabet):
        counter =  word.count(letter)
        d[letter] = counter
        
    most = max(d.items(), key=operator.itemgetter(1))[0]
    print(most)
    print(d)
parsing_bullshit('wordssss')