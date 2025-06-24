class Card:
    def __init__(self, suit, value):
       self.suit = suit
       self.value = value 
    
    # a getter
    def __repr__(self):
        return f"The card selected was the age={self.value} of {self.suit})"

class Deck:
    def __init__(self, cards):
        self.cards = []
    
    def count(self):
        return f"You have {len(self.cards)} cards in the deck"
    

    
