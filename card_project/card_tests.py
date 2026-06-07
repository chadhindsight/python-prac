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
        """repr should return a string in the form of 'Value of Suit' """
        self.assertEqual(repr(self.card), "The card selected is the A of Hearts")
                         


if __name__ == "__main__":
    unittest.main()
