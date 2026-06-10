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
        self.deck = Deck()
    
    def test_init(self):
        """ deck should have a card attribute, which is a list of 52 cards"""
        # Checks if self.deck.cards is a list or not
        self.assertTrue(isinstance(self.deck.cards, list))
        # Checks if the length of self.deck.cards is 52
        self.assertEqual(len(self.deck.cards), 52)
    
    def test_repr(self):
        """ repr should return a string in the form of 'Deck of __ cards' """
        self.assertEqual(self.deck, "Deck of 52 cards")
    
    def test_count(self):
        """The count method should return the number of cards"""
        self.assertEqual(self.deck.cards.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.cards.count(), 51)
    
    def test_deal_sufficient_cards(self):
        """_deal should deal the number of cards specified"""
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)
    
    def test_deal_insufficient_cards(self):
        """ deal should not deal cards if there is a deficit"""
        cards = self.deck._deal(80)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

if __name__ == "__main__":
    unittest.main()
