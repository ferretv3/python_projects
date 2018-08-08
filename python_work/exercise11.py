
class Olympics:
    
    def __init__(self, athlete = "", country = "", event = "", medal = ""):
        self.athlete = athlete
        self.country = country
        self.event = event
        self.medal = medal
    

ath_1 = Olympics("Stephen Brown", "USA", "Shotput", "Silver")


print(ath_1.athlete)