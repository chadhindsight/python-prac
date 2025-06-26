class Card:
    def __init__(self, suit, value):
       self.suit = suit
       self.value = value 
    
    # a getter
    def __repr__(self):
        return f"The card selected was the age={self.value} of {self.suit})"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = [Card(value, suit) for value in values for suit in suits]
        print(self.cards)
    
    def count(self):
        return f"You have {len(self.cards)} cards in the deck"



c1 = Card("A", "Spades")
c1 = Card("5", "Hearts")
    
Deck()