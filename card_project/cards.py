class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value 
    
    def __repr__(self):
        return f"The card selected was the {self.value} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = [Card(suit, value) for value in values for suit in suits] 
    
    def __repr__(self):
        return f"Deck of {self.count()} cards"  
    
    def count(self):
        return len(self.cards)  
    
    def _deal(self, num):
        numOfCards = self.count()  
        actual = min(numOfCards, num) 
        if numOfCards == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:] 
        self.cards = self.cards[:-actual]
        return cards 

    def deal_card(self):
        return self._deal(1)[0]
     
    # def deal_hand(self):

d = Deck()
print(d._deal(3))
print(d.count())