class Time( object ):
    
    def __init__(self, hour = 0, minutes = 0, seconds = 0):
        '''initializes values for instance variables'''
        self.__hour = hour
        self.__mins = minutes
        self.__secs = seconds
    
    def __repr__(self):
        '''returns formal represenation of Time in HH:MM:SS format'''
        return("Class Time: {:02d}:{:02d}:{:02d}"\
               .format(self.__hour,self.__mins,self.__secs))
    
    def from_str(self, col_str):
        '''updates instance variables for string with format hh:mm:ss'''
        hour, minutes, seconds = [ int(n) for n in col_str.split(":")]
        
        self.__hour = hour
        self.__mins = minutes
        self.__secs = seconds
        
        
    