
def pattern_input(pattern_str,string):
    pat_dict = dict()
    
    pat_lst = []
    for letter in pattern_str:
        pat_lst.append(letter)
        
    for ch in pattern_str:
        if ch not in pat_dict:
            pat_dict[ch] = []
    
    for ch in pat_dict:
        pat_dict[ch] = pat_lst.count(ch)
        
        lst_of_stuff = []
        
        for index in range(len(string)):
            sliced = string[:index]
            
            if string.count(sliced) == pat_dict[ch]:
                lst_of_stuff.append(sliced)
                
                
        pat_dict[ch] = lst_of_stuff[-1]
        new_string = string.replace(pat_dict[ch],"")
        break
    print(new_string)
    
    
    return(pat_dict)    
    

    

            
a = pattern_input("aabb","xyzabcefgxyz")
print(a)