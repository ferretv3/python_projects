#################################################################
#   lab07
#       Tests Benford's Law. Prompts user for input file,
#       reads contents of file, counts the leading digits,
#       displays results.
#################################################################

BENFORD_PERCENT = ["(30.1%)","(17.6%)","(12.5%)","( 9.7%)",\
                   "( 7.9%)","( 6.7%)","( 5.8%)","( 5.1%)","( 4.6%)"]

def open_file(file_name_str):
    
    '''Repeatedly prompts for file to open until valid file is input'''
    try:
        new_file = open(file_name_str,"r")
        return new_file
    except FileNotFoundError:
        file_name_str = input("Enter a file name: ")
        
def file_to_data(file):
    
    '''Creates list with the first digit of each number in file'''
    data_list = []
    count_list = []
    for line in file:
        data_list.append(line.strip())
    for item in data_list:
        if item[0] != "0":
            count_list.append(item[0])
    return(count_list,len(count_list))
    
def count_first_digit(count_list):
    
    '''Counts frequency of first digits 1-9 and returns counted list'''
    first_digits = []
    
    count1 = count_list.count("1")
    first_digits.append(count1)
    count2 = count_list.count("2")
    first_digits.append(count2)
    count3 = count_list.count("3")
    first_digits.append(count3)
    count4 = count_list.count("4")
    first_digits.append(count4)
    count5 = count_list.count("5")
    first_digits.append(count5)
    count6 = count_list.count("6")
    first_digits.append(count6)
    count7 = count_list.count("7")
    first_digits.append(count7)
    count8 = count_list.count("8")
    first_digits.append(count8)
    count9 = count_list.count("9")
    first_digits.append(count9)
    return(first_digits)    


def format_output(digit_list,number_of_items,percentage):
    '''Formats data for printing'''
    
    print("\nDigit Percent Benford ")
    for index,value in enumerate(digit_list):
        print("{:>5d}{}{:7.1%}{:>8s}".format(index+1,":",\
              value/number_of_items,percentage[index]))
        
def main():
    data_file_name = input("Enter a file name: ")
    new_file = open_file(data_file_name)
    data_list,number_items = file_to_data(new_file)
    first_digit_list = count_first_digit(data_list)
    format_output(first_digit_list,number_items,BENFORD_PERCENT)
    
main()
    
    
        
