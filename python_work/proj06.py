# PROJECT 6
# 6/26/18



# Card class, Deck Class, and random module in cards
import cards

def less_than(c1,c2):
    '''Return 
           True if c1 is smaller in rank, 
           True if ranks are equal and c1 has a 'smaller' suit
           False otherwise'''
    if c1.rank() < c2.rank():
        return True
    elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
        return True
    return False
    
def min_in_list(L):
    '''Return the index of the mininmum card in L'''
    min_card = L[0]  # first card
    min_index = 0
    for i,c in enumerate(L):
        if less_than(c,min_card):  # found a smaller card, c
            min_card = c
            min_index = i
    return min_index
        
def cannonical(H):
    ''' Selection Sort: find smallest and swap with first in H,
        then find second smallest (smallest of rest) and swap with second in H,
        and so on...'''
    for i,c in enumerate(H):
        # get smallest of rest; +i to account for indexing within slice
        min_index = min_in_list(H[i:]) + i 
        H[i], H[min_index] = H[min_index], c  # swap
    return H

def flush_7(H):
    '''Return a list of 5 cards forming a flush,
       if at least 5 of 7 cards form a flush in H, a list of 7 cards, 
       False otherwise.'''
    
    suits = [[],[],[],[]]       # list of 4 lists: 1 list for each suit
    for c in H:
        suits[c.suit()-1].append(c)  # suit assigned values 0,1,2,3 in  
    for i in range(4):               # card class
        if len(suits[i]) >= 5:
            return cannonical(suits[i][:5])   # returns if there are atleast
    return False                              # 5 cards of the same suit
    
def straight_7(H):
    '''Return a list of 5 cards forming a straight,
       if at least 5 of 7 cards form a straight in H, a list of 7 cards, 
       False otherwise.'''
    
    H = cannonical(H)   # sort the 7 cards in hand by rank
    
    beginning = H[:5]   # only 5 cards need to be returned, not 7
    middle = H[1:6]     # there are 3 instances of 5 cards in H (overlap)
    end = H[2:]
    
    hand_list = [beginning,middle,end]
    
    unique_set = set()

    for i,h in enumerate(hand_list):
        # taking avg of low card rank and high card rank in list
        high_low_avg = (h[0].rank() + h[-1].rank()) / 2
        # taking difference between high card and low card in list
        high_low_diff = h[-1].rank() - h[0].rank()
        overall = 0
        for c in h:
            # taking overall sum of card ranks in list
            overall += c.rank()
            unique_set.add(c.rank())
        overall_avg = overall / len(h)  # avg of overall sum

        if high_low_avg == overall_avg and\
        high_low_diff == 4 and\
        len(hand_list[i]) == len(unique_set):
            
            #   for example [1,2,3,4,5]
            #   (1 + 5) / 2 = 3             --> high_low_avg
            #   (1 + 2 + 3 + 4 + 5) / 5 = 3 --> overall_avg 
            #   5 - 1 = 4                   --> high_low_diff
            #   all numbers are unique      --> unique set
            
            return hand_list[i]
        else:
            unique_set.clear()
            
    return False

def straight_6(H):
    '''Return a list of 5 cards forming a straight,
       if at least 5 of 6 cards form a straight in H, a list of 6 cards, 
       False otherwise.'''
       
    # CONDITIONAL FUNCTION FOR STRAIGHT_FLUSH_7   
    
    H = cannonical(H)   # sort the 6 cards in hand by rank
    
    beginning = H[:5]   # only 5 cards need to be returned, not 6
    end = H[1:]         # there are 2 instances of 5 cards in H (overlap)

    
    hand_list = [beginning,end]
    
    unique_set = set()

    for i,h in enumerate(hand_list):
        # taking avg of low card rank and high card rank in list
        high_low_avg = (h[0].rank() + h[-1].rank()) / 2
        high_low_diff = h[-1].rank() - h[0].rank()
        overall = 0
        for c in h:
            # taking overall sum of card ranks in list
            overall += c.rank()
            unique_set.add(c.rank())
        overall_avg = overall / len(h)  # avg of overall sum

        if high_low_avg == overall_avg and\
        high_low_diff == 4 and\
        len(hand_list[i]) == len(unique_set):
            
            return hand_list[i]
        
        else:
            unique_set.clear()
            
    return False

def straight_5(H):
    '''Return a list of 5 cards forming a straight,
       if 5 cards form a straight in H, a list of 5 cards, 
       False otherwise.'''
    
    # CONDITIONAL FUNCTION FOR STRAIGHT_FLUSH_7
    
    H = cannonical(H)   # sort the 5 cards in hand by rank
    unique_set = set()
    
    overall = 0
    for c in H:
        # taking avg of low card rank and high card rank in list
        high_low_avg = (H[0].rank() + H[-1].rank()) / 2
        high_low_diff = H[-1].rank() - H[0].rank()
        
        # taking overall sum of card ranks in list
        overall += c.rank()
        unique_set.add(c.rank())    
    overall_avg = overall / len(H)  # avg of overall sum
    
    if high_low_avg == overall_avg and\
    high_low_diff == 4 and\
    len(H) == len(unique_set):        
        return H
        
    return False
        
def straight_flush_7(H):
    '''Return a list of 5 cards forming a straight flush,
       if at least 5 of 7 cards form a straight flush in H, a list of 7 cards, 
       False otherwise.'''
    
    # combination of flush function and straight_7/straight_6/straight_5
    
    # flush_7
    suits = [[],[],[],[]]
    for c in H:
        suits[c.suit()-1].append(c)
    for i in range(4):
        if len(suits[i]) >= 5:
            # straight_5
            if len(suits[i]) == 5:
                return straight_5(suits[i])
            # straight_6
            elif len(suits[i]) == 6:
                return straight_6(suits[i])
            # straight_7
            elif len(suits[i]) == 7:
                return straight_7(suits[i])
     
    return False

def four_7(H):
    '''Return a list of 4 cards with the same rank,
       if 4 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.'''
       
    H = cannonical(H)   # sorts cards in hand(H) by rank
    H_ranked_list = []
    four_list = []
    
    for c in H:
        H_ranked_list.append(c.rank())
    
    for rank in H_ranked_list:
        if H_ranked_list.count(rank) == 4:      # counts occurences of rank
            four_rank = rank                    # in ranked list
            for c in H:
                if c.rank() == four_rank:       # returns list of four cards
                    four_list.append(c)
            return four_list
    
    return False

def three_7(H):
    '''Return a list of 3 cards with the same rank,
       if 3 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''
       
    H = cannonical(H)   # sorts cards in hand(H) by rank
    H_ranked_list = []
    three_list = []
    
    for c in H:
        H_ranked_list.append(c.rank())
    
    for rank in H_ranked_list:
        if H_ranked_list.count(rank) == 3:      # counts occurences of rank 
            three_rank = rank                   # in ranked list
            for c in H:
                if c.rank() == three_rank:      # returns list of three cards
                    three_list.append(c)
            return three_list
    
    return False
        
def two_pair_7(H):
    '''Return a list of 4 cards that form 2 pairs,
       if there exist two pairs in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H) and three_7(H) are both False.'''
    
    H = cannonical(H)   # sort the cards in hand(H) by rank
    H_ranked_list = []  # list of card ranks
    pair_1 = []
    
    for c in H:
        H_ranked_list.append(c.rank())
    
    # loops through ranked list until all pairs are found
    for rank in H_ranked_list:
        if H_ranked_list.count(rank) == 2:
            rank_1 = rank
            for c in H:
                if c.rank() == rank_1:
                    pair_1.append(c)
                    H_ranked_list.remove(c.rank())
    
    # only returns if pair 1 has 4 items
    if len(pair_1) == 4:
        return pair_1
    
    return False

def one_pair_7(H):
    '''Return a list of 2 cards that form a pair,
       if there exists exactly one pair in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H), three_7(H) and two_pair(H) are False.'''
    
    H = cannonical(H)   # sorts the cards in hand(H) by rank
    H_ranked_list = []  # list of card ranks in hand
    pair_1 = []
    
    for c in H:
        H_ranked_list.append(c.rank())
    
    for rank in H_ranked_list:
        if H_ranked_list.count(rank) == 2:
            two_rank = rank
            for c in H:
                if c.rank() == two_rank:
                    pair_1.append(c)
            # returns once one pair is found in hand
            return pair_1
    
    return False
    

def full_house_7(H):
    '''Return a list of 5 cards forming a full house,
       if 5 of the 7 cards form a full house in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''    

    H = cannonical(H)   # sorts cards in hand(H) by rank
    H_ranked_list = []  # list of card ranks in hand
    three_list = []
    two_list = []
    
    for c in H:
        H_ranked_list.append(c.rank())
    
    # attempts to find triplet in ranked list
    for rank in H_ranked_list:
        if H_ranked_list.count(rank) == 3:
            three_rank = rank
            for c in H:
                if c.rank() == three_rank:
                    three_list.append(c)
            
            # removes triplet from ranked list to not interfere
            # with finding pair
            H_ranked_list[:] = [rank for rank in H_ranked_list\
                                if rank != three_rank]
    
    #attempts to find pair in ranked list
    for rank in H_ranked_list:
        if H_ranked_list.count(rank) == 2:
            two_rank = rank
            for c in H:
                if c.rank() == two_rank:
                    two_list.append(c)
            
            #only returns if the length of three list is 5
            #   ensures that a full house is actually being returned
            three_list.extend(two_list)
            if len(three_list) == 5:
                return cannonical(three_list)
    
    return False

def hierarchy(H):
    '''returns hierarchy of hands in poker:
            1.) straight flush
            2.) four of a kind
            3.) full house
            4.) flush
            5.) straight
            6.) three of a kind
            7.) two pair
            8.) one pair
            9.) high card'''
    
    H = cannonical(H)
    
    if straight_flush_7(H) != False:
        value = 8
        return straight_flush_7(H), value, "a straight flush:"
    elif four_7(H) != False:
        value = 7
        return four_7(H), value, "four of a kind:"
    elif full_house_7(H) != False:
        value = 6
        return full_house_7(H), value, "a full house:"
    elif flush_7(H) != False:
        value = 5
        return flush_7(H), value, "a flush:"
    elif straight_7(H) != False:
        value = 4
        return straight_7(H), value, "a straight:"
    elif three_7(H) != False:
        value = 3
        return three_7(H), value, "three of a kind:"
    elif two_pair_7(H) != False:
        value = 2
        return two_pair_7(H), value, "two pairs:"
    elif one_pair_7(H) != False:
        value = 1
        return one_pair_7(H), value, "a pair:"
    else:
        value = 0
        return H, value, "high card:"



def main():
    D = cards.Deck()
    D.shuffle()

       
    while True:
        
        #creates community card list of 5 cards
        community_list = []
        for i in range(5):
            community_list.append(D.deal())
        
        #creates hand 1 and hand 2, both have two cards
        hand_1_list = []
        hand_2_list = []
        for i in range(2):
            hand_1_list.append(D.deal())
        for i in range(2):
            hand_2_list.append(D.deal())
        
        #printing outline
        print("-"*40)
        print("Let's play poker!\n")
        print("Community cards:",community_list)
        print("Player 1:",hand_1_list)
        print("Player 2:",hand_2_list)
        
        
        player1 = hand_1_list + community_list
        cards1, rank1, message1 = hierarchy(player1)
        
        player2 = hand_2_list + community_list
        cards2, rank2, message2 = hierarchy(player2)
        
        # player 1 win scenario
        if rank1 > rank2:
            print("\nPlayer 1 wins with",message1,cards1)
        
        # high card scenario
        elif rank1 == 0 and rank2 == 0:
            rank1 = hand_1_list[1].rank()
            rank2 = hand_1_list[1].rank()
            if rank1 > rank2:
                print("\nPlayer 1 wins with!",message1,cards1)
            elif rank1 == rank2:
                print("\nTIE with",message1,cards1)
            elif rank1 < rank2:
                print("\nPlayer 2 wins with",message2,cards2)
        
        # Tie scenario        
        elif rank1 == rank2:
            print("\nTIE with",message1,cards1)
        
        # Player 2 win scenario
        elif rank1 < rank2:
            print("\nPlayer 2 wins with",message2,cards2)
        
        # continues running program until less than
        # 9 cards are left in the deck
        if len(D) < 9:
            print("Deck has too few cards so game is done.")
            return False
        
        # continues running program if input is 'y', quits if input is 'n'
        yesno = input("Do you wish to play another hand?(Y or N) ")
        if yesno.lower() == "y":
            continue
        elif yesno.lower() == "n":
            return False
    


if __name__ == "__main__":
    main()