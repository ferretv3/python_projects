########################################################################
#
# PROJECT_3____6-1-2018(m-d-y)
#   Opens GDP.txt and returns:
#   Maximum and minimum percent GDP change (with respective years),
#   And maximum and minimum GDP values in trillions
#
#   1.) Auxiliary Functions
#   2.) Main Function
#
########################################################################

# 1.A)
def open_file(file_name_str):
    '''Repeatedly prompt until a valid file name for file to be opened.'''
    
    while True: 
        try:
            GDP_file = open(file_name_str,"r")
            return GDP_file
        except FileNotFoundError:
            print("Error. Please try again", end=" ")
            file_name_str = input("Enter a file name: ")
            
# 1.B)    
def find_min_percent(line):
    '''Find the min percent change in the line; return value and index.'''
    
    start = 76    #Data values start on index 76 of line
    x = 12        #Values separated by increments of 12
    count = 0
    min_value = 1000000
    while count != 47:     #47 data values to examine
        num = line[start:start+x]
        num.replace(" ","")         #Remove whitespace from string slice
        if float(num) < min_value:
            min_value = float(num)
            index = start
        start += x
        count += 1
        
    return(min_value,index)
    
# 1.C)
def find_max_percent(line):
    '''Find the max percent change in the line; return value and index.'''
    
    start = 76    #Data values start on index 76 of line
    x = 12        #Values separated by increments of 12
    count = 0
    max_value = -1000000
    
    while count != 47:     #47 data values to examine
        num = line[start:start+x]
        num.replace(" ","")         #Remove whitespace from string slice
        if float(num) > max_value:
            max_value = float(num)
            index = start
        start += x
        count += 1
        
    return(max_value,index)
    
# 1.D)
def find_gdp(line, index):
    '''Use the index fo find the gdp value in the line; return the value'''
    
    gdp_str = line[index:index+12]
    gdp_str.replace(" ","")         #Remove whitespace from string slice
    gdp_float = float(gdp_str)
    
    return(gdp_float)
    
# 1.E)
def find_year(line,index):
    '''Use the index to find the year, given index; return the value'''
    
    year_str = line[index:index+12]
    year_str.replace(" ","")        #Remove whitespace from string slice
    year_int = int(year_str)
    
    return(year_int)
    
# 1.F)
def trillions_converter(gdp_value):
    '''Converts value in billions to trillions'''
    
    gdp_trillions = gdp_value / 1000
    
    return gdp_trillions

# 1.G)        
def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):
    '''Display values; convert billions to trillions first.'''
    
    min_gdp = trillions_converter(min_val_gdp)
    max_gdp = trillions_converter(max_val_gdp)
    
    print("\nGross Domestic Product")
    print("{:<10s}{:>8s}{:>6s}{:>18s}".format(\
          "min/max","change","year","GDP (trillions)"))
    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format(\
          "min",min_val,min_year,min_gdp))
    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format(\
          "max",max_val,max_year,max_gdp))
    
    
    
# 2.)
def main():  
                  
    file_name = input("Enter a file name: ")
    GDP_file = open_file(file_name)

    for index, line in enumerate(GDP_file):
        if index == 8:
                #line containing percent changes in gdp
            min_percent,min_index = find_min_percent(line)
            max_percent,max_index = find_max_percent(line)
        elif index == 42:
                #line containing a catalog of years
            min_year = find_year(line,min_index)
            max_year = find_year(line,max_index)
        elif index == 43:
                #line containing total gdp values in billions
            min_gdp = find_gdp(line,min_index)
            max_gdp = find_gdp(line,max_index)

    display(min_percent,min_year,min_gdp,max_percent,max_year,max_gdp)

if __name__ == "__main__":
    main()            
          #Calls main function        
