######################################################################
#   Project 4:
#   Opens file with income data and returns avg/median income
#   for a specific year. Optionally plots income vs cumulative percent, 
#   calculates the percentage of population that makes less than
#   income value, and calculates top percentage given income 
######################################################################
import pylab

def do_plot(x_vals,y_vals,year):
    '''Plot x_vals vs. y_vals where each
       is a list of numbers of the same length.'''
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    pylab.title("Cumulative Percent for Income in "+str(year))
    pylab.plot(x_vals,y_vals)
    pylab.show()
    
def open_file():
    '''Prompts user for input year between 1990 and 2015
       and attempts to open file until valid file is listed'''

    #Only executes if year_str is in valid range, 1990-2015
    while True:
        year_str = input("Enter a year where 1990 <= year <= 2015: ")
        try:
            if int(year_str) in list(range(1990,2016)):
                file_name = "year" + year_str + ".txt"
                while True:
                    try:
                        fp = open(file_name,"r")
                        return (fp,int(year_str))
                    except FileNotFoundError:
                        print("Error in file name:",file_name,\
                              " Please try again.")
                        year_str = input("Enter a year where\
                                         1990 <= year <= 2015: ")
                        break
            else:
                print("Error in year. Please try again.")
                year_str = input("Enter a year where 1990 <= year <= 2015: ")
        except ValueError:
            print("Error in year. Please try again.")
            year_str = input("Enter a year where 1990 <= year <= 2015: ")
                                    
        
def read_file(fp):
    '''reads line of text and returns list of data'''
    
    data_list = []
    for index, line in enumerate(fp):
        if index >= 2: #first two lines are headers
            data = list(line.replace("\n","").replace(",","").split())
            data_list.append(data) #makes a list of lists
    return data_list

#Line index values:
#   Column 0 is bottom of this income range 
#   Column 1 is the hyphen separating the bottom of the range from the top
#   Column 2 is the top of this income range
#   Column 3 is the number of individuals in the income range
#   Column 4 is the cumulative number of individuals in
#      this income range and all lower ranges
#   Column 5 is the Column 4 value represented as a
#      cumulative percentage of all individuals
#   Column 6 is the combined income of all the individuals
#      in this range of income
#   Column 7 is the average income of individuals in this range of income.

            
def find_average(data_lst):
    '''Returns the average income for given year'''
    
    aggregate_flt = 0
    for index, line in enumerate(data_lst):
        aggregate_flt += float(line[6])
        if index == 58: #final line of text file
            total_population = int(line[4])
    average_flt = aggregate_flt / total_population
    return(average_flt)
    
def find_median(data_lst):
    '''Finds median income: percent of population closest to 50%'''
    
    min_percent = 100
    for index, line in enumerate(data_lst):
        if abs(50.00 - float(line[5])) < min_percent:
            min_percent = abs(50.00 - float(line[5]))
            median_income = line[7]
    return(float(median_income))

        
def get_range(data_lst, percent):
    '''Returns salary range, given list of data and percentage'''
    
    min_percent = 100
    for line in data_lst:
        if float(line[5]) > percent and\
           abs(percent - float(line[5])) < min_percent:
               
            min_percent = abs(percent - float(line[5]))
            salary_range = line[0],line[2]
            percentage = float(line[5])
            income = float(line[7])
            
    return(salary_range,percentage,income)
    

def get_percent(data_lst,salary):
    '''Returns percentage of population given salary'''
    
    for line in data_lst:
        if salary >= float(line[0]) and salary <= float(line[2]):
            salary_range = line[0],line[2]
            percentage = float(line[5])
            return(salary_range,percentage)

def main():
    
    fp,year = open_file()
    data_lst = read_file(fp)
    avg = find_average(data_lst)
    median = find_median(data_lst)
    print("{:<6s}{:<14s}{:<14s}".format("Year","Mean","Median"))
    print("{:<6d}${:<14,.2f}${:<14,.2f}".format(year,avg,median))

        
    response = input("Do you want to plot values (yes/no)? ")
    if response.lower() == 'yes':
        x_vals = []
        y_vals = []
        for index, line in enumerate(data_lst):
            if index <= 39:
                x_vals.append(float(line[0]))
                y_vals.append(float(line[5]))
        do_plot(x_vals,y_vals,year)

    
    choice = input("Enter a choice to get (r)ange,\
                   (p)ercent, or nothing to stop: ")
    
    while choice:
        if choice == "r": #r returns get_range function
            
            percent = float(input("Enter a percent: "))
            if percent > 100 or percent < 0:
                print("Error in percent. Please try again.")
                choice = input("Enter a choice to get (r)ange,\
                               (p)ercent, or nothing to stop: ")
            elif percent <= 100 and percent >= 0:
                salary_range,percentage,income = get_range(data_lst,percent)
                print("{:4.2f}% of incomes are below ${:<13,.2f}."\
                      .format(percent,float(salary_range[0])))
                choice = input("Enter a choice to get (r)ange,\
                               (p)ercent, or nothing to stop: ")
            else:
                choice = input("Enter a choice to get (r)ange,\
                               (p)ercent, or nothing to stop: ")

        elif choice == "p": #p returns get_percent function
            income = float(input("Enter an income: "))
            if income < 0:
                print("Error: income must be positive")
                choice = input("Enter a choice to get (r)ange,\
                               (p)ercent, or nothing to stop: ")
            elif income >= 0:
                salary_range,percentage = get_percent(data_lst,income)
                print("An income of ${:<13,.2f} is in\
                      the top {:4.2f}% of incomes."\
                      .format(income,float(percentage)))
                choice = input("Enter a choice to get (r)ange,\
                               (p)ercent, or nothing to stop: ")
            else:
                choice = input("Enter a choice to get (r)ange,\
                               (p)ercent, or nothing to stop: ")
            
        elif choice == " ": #carriage return exits loop
            break
        else:
            print("Error in selection.")
            choice = input("Enter a choice to get (r)ange,\
                           (p)ercent, or nothing to stop: ")

if __name__ == "__main__":
    main()

    
