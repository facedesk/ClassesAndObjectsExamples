class Card:
    def __init__(self, passedInRank, passedInSuit):
    	self.rank = passedInRank.lower()
    	self.suit = passedInSuit.lower()
        self.orderRank = self.checkRank()
        self.orderSuit = self.checkSuit()
        if(self.orderRank!=0 and self.orderSuit!=0):
            self.rank = rank
            self.suit = suit
        else:
        	self.rank = "Invalid"
        	self.suit = "Invalid"

    def checkRank(self):
        if(self.rank=="2"):
            return 1
        elif(self.rank=="3"):
            return 2
        elif(self.rank=="4"):
            return 3
        elif(self.rank=="5"):
            return 4 
        elif(self.rank=="6"):
            return 5  
        elif(self.rank=="7"):
            return 6  
        elif(self.rank=="8"):
            return 7  
        elif(self.rank=="9"):
            return 8  
        elif(self.rank=="10"):
            return 9 
        elif(self.rank=="jack"):
            return 10
        elif(self.rank=="queen"):
            return 11     
        elif(self.rank=="king"):
            return 12
        elif(self.rank=="ace"):
            return 13
        else:
            return 0

    def checkSuit(self):
    	if(self.suit == "clubs"):
    		return 1
    	elif(self.suit == "diamonds"):
    		return 2
    	elif(self.suit == "hearts"):
    		return 3
    	elif(self.suit =="spades"):
    		return 4
    	else:
    		return 0

    def displayCard(self):
        print (self.rank+" of "+self.suit)


if(__name__=="__main__"):
    a = Card("Ace","Clubs")
    b = Card("5","DiaMOnds")
    c = Card("4","hearts")  
    d= Card("Blue", "5")

    a.displayCard()
    b.displayCard()
    c.displayCard()
    d.displayCard()
