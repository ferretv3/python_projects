#####################################################################
#PROJECT_2____5-17-2018
#
#   Takes a price input (float) and payment amount (int) 
#   Returns amount of change in quarters, dimes, nickels, and pennies.
#   
#   Stops program when 'q' entered for price or if the amount of
#   change is larger than the amount of change in the register
#
#####################################################################

quarters = 10
dimes = 10
nickels = 10
pennies = 10
#   Initial amount of coins

print("Welcome to change-making program.")

print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))

in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

def quarter_change(quarters,change): #number of quarters in change
    while quarters > 0 and change >= 25: 
        q_change = change // 25
        if q_change >= quarters:
            q_change = quarters
        change -= q_change * 25
        if q_change > 0:
            print("Quarters:",int(q_change))
            return (change)
        


def dime_change(dimes,change): # number of dimes in change
    while dimes > 0 and change >= 10: 
        d_change = change // 10
        if d_change >= dimes:
            d_change = dimes
        change -= d_change * 10
        if d_change > 0:
            return(d_change,change)
            
def nickel_change(nickels,change): #number of nickels in change
     while nickels > 0 and change >= 5: 
         n_change = change // 5
         if n_change > nickels:
             n_change = nickels
         change -= n_change * 5
         if n_change > 0:
             return(n_change,change)
            
def penny_change(pennies,change): #number of pennies in change
    while pennies > 0 and change >= 1: 
        p_change = change // 1
        if p_change > pennies:
            p_change = pennies
        change -= p_change
        if p_change > 0:
            return(p_change,change)


                  
while in_str != "q":
    
    if float(in_str) < 0:
        print("Error: purchase price must be non-negative")
    else:
        
        dollars_paid = input("Input dollars paid (int): ")
        
        if float(dollars_paid) < float(in_str):
            print("Error: insufficient payment.")
            
        else:
            
            dollars_paid = input("Input dollars paid (int): ")
            
            price = float(in_str) * 100
            purchase = float(dollars_paid) * 100
            change = purchase - price
        
            if change == 0:
                print("No change.")
    
            elif (quarters * 25) + (dimes * 10) + (nickels * 5) + pennies < change:
                print("Error: ran out of coins.")
                break
        
            elif purchase < 0:
                print("Error: insufficient payment.")
    
            else:        
                print("\nCollect change below:")
        
                

            
    print("\nStock: {:} quarters, {:} dimes, {:} nickels, and {:} pennies".format(
        int(quarters), int(dimes), int(nickels), int(pennies)))
    
    in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
