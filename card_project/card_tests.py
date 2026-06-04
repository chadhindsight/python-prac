import unittest
from cards import Card, Deck 

class CardTests(unittest.TestCase):
    def set_up(self):
        self.card = Card("Hearts", "A")
    
    def test_init(self):
        """cards should have asuit and a value"""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")
    
    def test_repr(self):
        self.assertEqual( repr(self.card),"The card selected is the A of Hearts"
)
