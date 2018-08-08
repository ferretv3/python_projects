
import string
from operator import itemgetter


def add_word( word_map, word ):
    '''Adds word to map if word is not already in map, counts how many
       times the word occurs'''
    # adds word to word_map if not already in it
    # and assigns the initial value of zero
    word = word.lower()
    if word not in word_map:
        word_map[ word ] = 0

    # adds one to the word value in word_map
    word_map[ word ] += 1


def build_map( in_file, word_map ):
    '''Builds map from text file with unique word frequency'''
    for line in in_file:

        # splits line on spaces to make list of words
        word_list = line.split()

        for word in word_list:

            # strips word of spaces and any punctuation symbols
            word = word.strip().strip(string.punctuation)
            if word.isalpha():
                add_word( word_map, word )
        

def display_map( word_map ):
    '''prints sorted, word frequency list'''
    word_list = list()

    # items returns key,values for word_map
    # (key,values) pair assigned to list as tuple
    for word, count in word_map.items():
        word_list.append( (word, count) )

    # creates sorted list of tuples with values from greatest to least
    word_list = sorted(word_list)
    freq_list = sorted( word_list, key=itemgetter(1), reverse=True )
    

    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file(file_name_str):
    '''Attempts to open input file. If file doesn't exist, none is returned'''
    try:
        in_file = open( file_name_str, "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file


word_map = dict()
file_name_str = input("Enter file name: ")
in_file = open_file(file_name_str)

if in_file != None:

    build_map( in_file, word_map )
    display_map( word_map )
    in_file.close()


