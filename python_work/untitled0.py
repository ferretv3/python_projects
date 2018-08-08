#Viginere Cipher

number_lst = []

pear = True

while pear == True:   
    
        key = input("Enter a number: ")
        
        if key.isalpha():
            pear = False
        else:
            number_lst.append(int(key))

def shift_alphabet(num_int):
    
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
    ALPHABET = ALPHABET[num_int:] + ALPHABET[:num_int]
        
    for letter in ALPHABET:
        print(letter,end=" ")
    
    print(end="\n")
    print("This alphabet has been shifted by {} spaces".format(num_int))

for number in number_lst:
    shift_alphabet(number)


