# Project 5
# 

import csv
import string

def open_file():
    '''prompts for file name until file is successfully opened and returned'''
    
    file_name_str = input("Enter a file name: ")
    
    while True:
        try:
            file_name = open(file_name_str,"r")
            return file_name
        except FileNotFoundError:
            print("Invalid file name.")
            file_name_str = input("Enter a file name: ")

def read_file(file_name):
    '''reads csv file and returns sorted dict'''
    
    STATES = ['Alaska', 'Alabama', 'Arizona', 'Arkansas', 'California',\
          'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',\
          'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas',\
          'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts',\
          'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',\
          'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',\
          'New Mexico', 'New York', 'North Carolina', 'North Dakota',\
          'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',\
          'South Carolina', 'South Dakota', 'Tennessee', 'Texas',\
          'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',\
          'Wisconsin', 'Wyoming']
    
    
    crop_dict = {}
    file_name.readline()
    
    for line in file_name:
        line = line.strip().split(",")
        
        state = line[0].strip(string.punctuation)
        crop = line[1]
        variety = line[3]
        year = line[4]
        percentage = line[6]
        
        if state in STATES and variety == "All GE varieties":
            if crop not in crop_dict and percentage.isdigit():
                crop_dict.setdefault(crop,[]).append((percentage,year))
        
                                            
    return state_dict

def find_min_max(a_dict):
    
    print(a_dict)
    for key in a_dict.values():
        for item in key:
            print(item)

a = "Missouri 2\;"
a = a.strip(string.punctuation).strip(string.digits)
print(a)
        
        
        
        