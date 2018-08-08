#############################################################
#PROJECT_2____5-17-2018
#
#
#
#
#
#############################################################

quarters = 10
dimes = 10
nickels = 10
pennies = 10

print("\nWelcome to change-making program.")

print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))

in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

while in_str != "q":
    
    dollars_paid = input("Input dollars paid (int): ")
    
    price = float(in_str) * 100
    purchase = int(dollars_paid) * 100
    change = purchase - price
        
    if change == 0:
        pass
    
    elif (quarters * 25) + (dimes * 10) + (nickels * 5) + pennies < change:
        break
    
    else:
        
        while quarters > 0 and change >= 25:
            q_change = change // 25
            if q_change > quarters:
                q_change = q_change - quarters
            quarters -= q_change
            change = change - (q_change * 25)
            if q_change > 0:
                print("Quarters: ",int(q_change))
                
        while dimes > 0 and change >= 10:
            d_change = change // 10
            if d_change > dimes:
                d_change = d_change - dimes
            dimes -= d_change
            change = change - (d_change * 10)
            if d_change > 0:
                print("Dimes: ",int(d_change))
                
        while nickels > 0 and change >= 5:
            n_change = change // 5
            if n_change > nickels:
                n_change = n_change - nickels
            nickels -= n_change
            change = change - (n_change * 5)
            if n_change > 0:
                print("Nickels: ",int(n_change))
                
        while pennies > 0 and change >= 1:
            p_change = change // 1
            if p_change > pennies:
                p_change = p_change - pennies
            pennies -= p_change
            change = change - p_change
            if p_change > 0:
                print("Pennies: ",int(p_change))
                
    print("\nStock: {:} quarters, {:} dimes, {:} nickels, and {:} pennies".format(
            int(quarters), int(dimes), int(nickels), int(pennies)))
    
    in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
    
    
    
