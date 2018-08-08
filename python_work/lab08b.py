
def open_file():
    '''Opens files and returns file names'''
    in_file1 = open("data1.txt", "r")
    in_file2 = open("data2.txt", "r")
    return(in_file1,in_file2)


def make_dict(file_name,a_dict):
    '''Makes a dictionary from file name with format {name: score} '''
    file_name.readline() # first line of file is header
    
    name_list = []    # holds names
    number_list = []  # holds scores
    
    for line in file_name:
        line = line.strip().split()
        for item in line:
            if item.isalpha():
                name_list.append(item)
            else:
                number_list.append(int(item))
                
    a_dict = dict(zip(name_list,number_list)) # use zip() to combine two lists
                                              # into one dictionary
    return a_dict

def add_recurring(dict1,dict2):
    '''If key already exists in other dict, adds value for key
       If key doesn't exist in other dict, adds key and value to dict'''
       
    for key in dict1:
        if key in dict2:               # if name already in other dictionary
                                       # as key, sum values from both. 
            dict2[key] += dict1[key]
        else:                          # if key not already in other dictionary
                                       # adds key to the new dictionary 
            dict2[key] = dict1[key]
    return dict2

def output_format(dict2):
    '''formats dictionary for output'''
    
    output_list = []
    for key,val in dict2.items():
        output_list.append((key,val))
    output_list = sorted(output_list)  # creates list, alphabetically sorted
    
    print("{:10s}{:<10s}".format("Name","Total"))
    for pair in output_list:
        print("{:10s}{:<10d}".format(pair[0],pair[1]))    

def main():
    
    # initialize dictionaries to be empty so make_dict can add key:values
    dict1 = {}
    dict2 = {}
    
    # two files are being compared data1.txt and data2.txt    
    file_name1,file_name2 = open_file()
    
    dict1 = make_dict(file_name1,dict1)
    dict2 = make_dict(file_name2,dict2)
    
    # combines dictionaries, adds to value if key already in second dictionary
    dict2 = add_recurring(dict1,dict2)
    output_format(dict2)

main()

