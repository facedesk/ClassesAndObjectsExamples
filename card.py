class Card:
    def __init__(self, rank, suit):
    	rank = rank.lower()
    	suit = suit.lower()
        self.orderRank = checkRank(rank)
        self.orderSuit = checkSuit(suit)
        if(orderRank!=0 and orderSuit!=0):
            self.rank = rank
            self.suit = suit
        else:
        	self.rank = "Invalid"
        	self.suit = "Invalid"

    def checkRank(self,rank):
        return "Invalid"

    def checkSuit(self,suit):
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
        print("hi")
        print (self.rank+" of "+self.card)




if __name__=="main":
    c = Card("Ace","Clubs")
    c.displayCard()
