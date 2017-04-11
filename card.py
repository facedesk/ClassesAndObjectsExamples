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

    def checkRank(rank):
        pass
    def checkSuit(suit):
    	if(suit == "clubs"):
    		return 1
    	elif(suit == "diamonds"):
    		return 2
    	elif(suit == "hearts"):
    		return 3
    	elif(suit =="spades"):
    		return 4
    	else
    		return 0




    def displayCard(self):
        print (self.rank+" of "+self.card)
if(__init__=="main"):
	c = Card("Ace")
