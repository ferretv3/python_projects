VOWELS = "aeiou"
word = input("Enter a word ('quit' to quit): ")

while word.lower() != "quit":
    first_letter = word[0]
    new_word = word.lower()
    ending_vowel = "way"
    ending_consonant = "ay"

    if first_letter.lower() in VOWELS:
        print(word.lower() + ending_vowel)
        word = input("Enter a word ('quit' to quit): ")
    else:
        for index, letter in enumerate(word.lower()):
            if letter in VOWELS:
                value = index
                break
        print(new_word[value:] + new_word[:value] + ending_consonant)
        word = input("Enter a word ('quit' to quit): ")