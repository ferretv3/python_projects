# Project 5
# 
#reads csv file with crop information for each state
#prints the max and min percentage for each state, for the respective crop
#


#importing modules
import csv
import string
import collections

def open_file():
    '''prompts for file name until file is successfully opened and returned'''
    
    file_name_str = input("Enter a file: ")
    
    while True:
        try:
            file_name = open(file_name_str,"r")
            return file_name
        except FileNotFoundError: #repeatedly prompts until correct file 
                                  #entered
            print("Invalid file name.")
            file_name_str = input("Enter a file: ")

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
    
    #row[0] = State
    #row[1] = Crop
    #row[3] = Variety
    #row[4] = Year
    #row[6] = Percentage of Crops 
    
    crop_dict = {} #initially empty so data can be entered
    
    readcsv = csv.reader(file_name) #reads csv file
    
    for row in readcsv:
        
        row[0] = row[0].strip(string.punctuation).strip(string.digits)
        row[0] = row[0].strip()
        
        if row[0] in STATES:
            if row[1] not in crop_dict:
                crop_dict[row[1]] = {}
                #only include data for values that are numbers and
                #of the variety type = All GE varieties
                if row[6].isdigit() and row[3] == "All GE varieties":
                    
                    year_data_tuple = (int(row[6]),row[4])
                    
                    crop_dict[row[1]].setdefault(row[0],[]).\
                    append(year_data_tuple)
                        #sets initial value to be a list so tuples can
                        #be appended to value
                    crop_dict[row[1]][row[0]].sort()
            elif row[3] == "All GE varieties":
  
                if row[6].isdigit():
                    
                    year_data_tuple = (int(row[6]),row[4])
                   
                    crop_dict[row[1]].setdefault(row[0],[]).\
                    append(year_data_tuple)
                    #sorts state names alphabetically
                    crop_dict[row[1]] = collections.OrderedDict(sorted(\
                             crop_dict[row[1]].items()))
                    #sorts tuple values in list from least to greatest
                    crop_dict[row[1]][row[0]] = sorted(crop_dict[row[1]][row[0]])
                    
    #alphabetically sorts key in crop_dict
    crop_dict = collections.OrderedDict(sorted(crop_dict.items())) 
    
    
                                        
    return crop_dict

def print_data(a_dict):
    '''finds min and max values and formats data for printing'''
    for crop,state in a_dict.items():
        print("Crop:",crop)
        print("{:<20s}{:<8s}{:<6s}{:<8s}{:<6s}".format(\
              "State","Max Yr","Max","Min Yr","Min"))
        for key,values in state.items():
            
            max_tuple = max(values,key=lambda item:item[0]) #gets max value
            min_tuple = min(values,key=lambda item:item[0]) #gets min value
            
            min_yr = min_tuple[1]
            min_value = min_tuple[0]
            max_yr = max_tuple[1]
            max_value = max_tuple[0]
            print("{:<20s}{:<8s}{:<6d}{:<8s}{:<6d}".format(\
                  key,max_yr,max_value,min_yr,min_value))
        print(" ")
        
def main():
    file_name = open_file()
    data_dict = read_file(file_name)
    print_data(data_dict)   

if __name__ == "__main__":
    main()
        
        
        
        