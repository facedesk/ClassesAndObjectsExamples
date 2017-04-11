class Card:
    def __init__(self, rank, suit):
    	self.rank = rank.lower()
    	self.suit = suit.lower()
        self.orderRank = self.checkRank()
        self.orderSuit = self.checkSuit()
        if(self.orderRank!=0 and self.orderSuit!=0):
            self.rank = rank
            self.suit = suit
        else:
        	self.rank = "Invalid"
        	self.suit = "Invalid"

    def checkRank(self):
        return "invalid"

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
    c = Card("Ace","Clubs")
    c.displayCard()
