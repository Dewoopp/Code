import unittest
from Cards import CardDeck
import statistics

class TestCardDeck(unittest.TestCase):

    def testDeckLen(self):
        testDeck = CardDeck()
        self.assertEqual(len(testDeck.cards), 52)


    def testDeckTopCard(self):
        testDeck = CardDeck()
        tempCard = testDeck.cards[0]
        testDeck.removeTop()
        self.assertFalse(tempCard in testDeck.cards)

    def testDeckLenRemove(self):
        testDeck = CardDeck()
        testDeck.removeTop()
        self.assertEqual(len(testDeck.cards), 51)


    def testDeckRandomness(self):
        testDeck = CardDeck()
        # Creates a new array with the cards represented as values from 0 - 51
        cardListNum = [self.cardVal(card, testDeck) for card in testDeck.cards]
        # Creates a new array storing the differences between cards that are adjacent in the cards list
        cardListDiff = [abs(cardListNum[i + 1] - cardListNum[i]) for i in range(len(cardListNum) - 1)]
        # Takes the mean of these differences and asserts that it is high
        # This means that similar cards are far apart on average
        self.assertTrue(statistics.mean(cardListDiff) > 13)
        # Takes the standard deviation and asserts that it is high
        # This means that the spread of the cards is very varied
        # This is similar to true randomness
        self.assertTrue(statistics.stdev(cardListDiff) > 10)
    
    # Gives a value to the given card
    def cardVal(self, card, cardDeck):
        suitNum = cardDeck.suits.index(card.suit)
        return suitNum * 13 + card.number - 1



if __name__ == '__main__':
    unittest.main()