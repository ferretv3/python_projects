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


while in_str != "q":
    
    if float(in_str) < 0:
        print("Error: purchase price must be non-negative.")
    else:
        
        dollars_paid = float(input("Input dollars paid (int): "))
        
        while float(dollars_paid) < float(in_str):
            print("Error: insufficient payment.")
            dollars_paid = float(input("Input dollars paid (int): "))
            
        price = float(in_str) * 100
        purchase = float(dollars_paid) * 100
        change = int(purchase) - int(price)
        
        if change == 0:
            print("No change.")
    
        elif (quarters * 25) + (dimes * 10) + (nickels * 5) + pennies < change:
            print("Error: ran out of coins.")
            break
        
        elif purchase < 0:
            print("Error: insufficient payment.")
    
        else:        
            print("\nCollect change below: ")
            
            #greedy algorithm for calculating the amount of change
            #Hierarchy of quarters --> dimes --> nickels --> pennies
        
            while quarters > 0 and change >= 25: #number of quarters in change
                q_change = change // 25
                if q_change >= quarters:
                    q_change = quarters
                quarters = quarters - q_change
                change = change - (q_change * 25)
                if q_change > 0:
                    print("Quarters:",int(q_change))
                
            while dimes > 0 and change >= 10: # number of dimes in change
                d_change = change // 10
                if d_change >= dimes:
                    d_change = dimes
                dimes = dimes - d_change
                change = change - (d_change * 10)
                if d_change > 0:
                    print("Dimes:",int(d_change))
                
            while nickels > 0 and change >= 5: #number of nickels in change
                n_change = change // 5
                if n_change > nickels:
                        n_change = nickels
                nickels = nickels - n_change
                change = change - (n_change * 5)
                if n_change > 0:
                    print("Nickels:",int(n_change))
                
            while pennies > 0 and change >= 1: #number of pennies in change
                p_change = change // 1
                if p_change > pennies:
                    p_change = pennies
                pennies = pennies - p_change
                change = change - p_change
                if p_change > 0:
                    print("Pennies:",int(p_change))
            
    print("\nStock: {:} quarters, {:} dimes, {:} nickels, and {:} pennies".format(
        int(quarters), int(dimes), int(nickels), int(pennies)))
    
    in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
    
    
