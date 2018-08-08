def leap_year(year):
    if int(year) % 400 == 0 or int(year) % 4 == 0 and int(year) % 100 != 0:
        return True
    else:
        return False

def rotate(s,n):
    a = s[-n:]
    new = a + s[:-n]
    return new

def digit_count(number):
    
    even_count = 0
    odd_count = 0
    zero_count = 0
    number_str = str(number)
    
    if number > 1:
        for num in number_str:
            if int(num) % 2 == 0:
                if int(num) == 0:
                    zero_count += 1
                else:
                    even_count += 1
            else:
                odd_count += 1
    
    return(even_count, odd_count, zero_count)
    
print(digit_count(17982062589))    
    
def float_check(string):
    
    if "e" not in string and string.count(".") <= 1  and type(float(string)) == float: 
        return True
    else:
        return False


    
    
    
    
    
    
    