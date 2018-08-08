import sys

def unique_char(string):
    unique = set()
    for ch in string:
        unique.add(ch)
    if len(unique) != len(string):
        return False
    else:
        return True

def unique_char2(string):
    for ch in string:
        if string.count(ch) > 1:
            return False
        else:
            return True

def permutation(str1,str2):
    
    lst_1 = []
    lst_2 = []
    
    if len(str1) >= len(str2):
        for ch in str1:
            lst_1.append(ch)
        for ch in str2:
            if ch in lst_1:
                lst_2.append(ch)
                
        if len(lst_2) == len(str2):         
            return True
        else:
            return False
        
    else:
        for ch in str2:
            lst_1.append(ch)
        for ch in str1:
            if ch in lst_1:
                lst_2.append(ch)
                
        if len(lst_2) == len(str1):         
            return True
        else:
            return False        
        
def permutation2(str1,str2):
    
    if len(str1) == len(str2):
        
        for ch in str1:
            if str1.count(ch) == str2.count(ch):
                pass
            else:
                return False
    else:
        return False
    
    return True
        
def palindrome_perm(palindrome,str1):
    
    if palindrome[::-1] == palindrome:
        
        tst1 = sorted(palindrome)
        tst2 = sorted(str1)
        
        if tst1 == tst2:
            return True
        else:
            return False
    else:
        return True
    
def compression(string):
    
    set1 = set()
    lst1 = []
    
    for ch in string:
        set1.add(ch)
    for ch in set1:
        lst1.append(ch)
        lst1.append(string.count(ch))
    
    if len(lst1) > len(string):
        print(string)
    else:
        for ch in lst1:
            print(ch,end='')                

#compression("aaabbcccc")

def diff_array(array1,array2):
    
    array1.sort()
    array2.sort()
    
    max_diff = sys.maxsize
    
    for num_1 in array1:
        for num_2 in array2:
            if num_1 - num_2 < max_diff and num_1 - num_2 > 0:
                max_diff = num_1 - num_2
                number_1 = num_1
                number_2 = num_2

    return(number_1,number_2)
    
#print(diff_array([1,5,10,900],[10,6,8,4]))



def adding_bullshit(num1,num2):
    
    lst_1 = []
    lst_2 = []
    
    for i in range(num1):
        lst_1.append(0)
    for i in range(num2):
        lst_2.append(0)
    
    lst_1.extend(lst_2)    
    print(len(lst_1))

#adding_bullshit(4,5)


def staircase(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"#"*(i))

#staircase(7) 
    
def miniMaxSum(arr):
    
    arr.sort()
    min_sum = sum(arr) - arr[-1]
    max_sum = sum(arr) - arr[0]
    
    print(min_sum,max_sum)
    
#arr = [1,2,3,4,5]
#miniMaxSum(arr)
    
def birthday(ar):
    tallest = max(ar)
    print(ar.count(tallest))

#ar = [3,2,1,3]
#birthday(ar)



#sample_string = "aabaa"
#for i in range(len(sample_string)):
#    print(sample_string[0:i])
#

#def gradingStudents(grades):
#    
#    BENCHMARKS = [45,50,55,60,65,70,75,80,85,90,95,100]
#    update = []
#    for grade in grades:
#        if grade < 40:
#            update.append(grade)
#        else:
#            for benchmark in BENCHMARKS:
#                diff = benchmark - grade 
#                if 5 >= diff > 3:
#                    update.append(grade)
#                    continue
#                
#
#    for num in update:
#        print(num)
#
#gradingStudents([43,39,67,78,64])


def climbingLeaderboard(scores, alice):
    for i in range(len(alice)):
        score_set = set()
        score_dict = {}
        [score_set.add(score) for score in scores]
        score_set.add(alice[i])
        for index,value in enumerate(sorted(score_set,reverse=True)):
            score_dict[index+1] = value
    
        for key,val in score_dict.items():
            if val == alice[i]:
                print(key)
                score_set.clear()
                score_dict.clear()
                break
    
climbingLeaderboard([100,100,50,40,40,20,10],[5,25,50,120])



