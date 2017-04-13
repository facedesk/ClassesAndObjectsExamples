from card import Card

class Deck:
    def __init__(self):
		self.value =[]
		self.validSuits=["Clubs","Spades","Hearts","Diamonds"]
		self.validRanks=["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
		for suit in self.validSuits:
			for rank in self.validRanks:
			    self.value.append(Card(rank,suit))
    def displayDeck(self):
        for c in self.value:
    	    c.displayCard()
    def Shuffle(self):
    	pass
    def TakeFromTop(self):
    	c = self.value[-1]
    	self.value.remove(c)
    	return c
    def TakeFromBottom(self):
    	#bottom is 0, top is 52
    	c = self.value[0]
    	self.value.remove(c)
    	return c

    def AddToBottom(self,cardToAdd):
    	self.value.insert(0,cardToAdd)
    def AddToTop(self,cardToAdd):
    	self.value.append(cardToAdd)

    def Cut(self):
        pass

startingDeck = Deck()
startingDeck.displayDeck()