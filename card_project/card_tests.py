import unittest
from cards import Card, Deck 

class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", "A")
    
    def test_init(self):
        """cards should have a suit and a value"""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")
    
    def test_repr(self):
        """repr should return a string in the form of 'The card selected is the ___ of ___' """
        self.assertEqual(repr(self.card), "The card selected is the A of Hearts")
                         
class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = []
    

if __name__ == "__main__":
    unittest.main()
