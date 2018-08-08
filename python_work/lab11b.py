class Time( object ):
    
    def __init__(self, hour = 0, minutes = 0, seconds = 0):
        '''initializes values for instance variables'''
        self.__hour = hour
        self.__mins = minutes
        self.__secs = seconds
    
    def __repr__(self):
        '''returns formal represenation of Time in hh:mm:ss format'''
        return("Class Time: {:02d}:{:02d}:{:02d}"\
               .format(self.__hour,self.__mins,self.__secs))
    
    def from_str(self, col_str):
        '''updates instance variables for string with format hh:mm:ss'''
        hour, minutes, seconds = [ int(n) for n in col_str.split(":")]
        
        self.__hour = hour
        self.__mins = minutes
        self.__secs = seconds
    
    def __str__(self):
        '''returns time in format hh:mm:ss'''
        return("{:02d}:{:02d}:{:02d}"\
               .format(self.__hour,self.__mins,self.__secs))
        


A = Time( 12, 25, 30 )

print( A )
print( repr( A ) )
print( str( A ) )
print()

B = Time( 2, 25, 3 )

print( B )
print( repr( B ) )
print( str( B ) )
print()

C = Time( 2, 25 )

print( C )
print( repr( C ) )
print( str( C ) )
print()

D = Time()

print( D )
print( repr( D ) )
print( str( D ) )
print()

D.from_str( "03:09:19" )

print( D )
print( repr( D ) )
print( str( D ) )

