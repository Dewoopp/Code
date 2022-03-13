import unittest
from Cards import CardDeck
import statistics

class TestCardDeck(unittest.TestCase):

    def testDeck(self):
        testDeck = CardDeck()
        self.assertEqual(len(testDeck.cards), 52)


    def testDeckTopCard(self):
        testDeck = CardDeck()
        tempCard = testDeck.cards[0]
        testDeck.removeTop()
        self.assertFalse(tempCard in testDeck.cards)

    def testDeckRemove(self):
        testDeck = CardDeck()
        testDeck.removeTop()
        self.assertEqual(len(testDeck.cards), 51)


    def testDeckRandomness(self):
        testDeck = CardDeck()
        cardListNum = [self.cardVal(card, testDeck) for card in testDeck.cards]
        cardListDiff = [cardListNum[i + 1] - cardListNum[i] for i in range(len(cardListNum) - 1)]
        self.assertTrue(-5 < statistics.mean(cardListDiff) < 5)
        stDev = statistics.stdev(cardListDiff)
        self.assertTrue(stDev > 10)
    
    def cardVal(self, card, cardDeck):
        suitNum = cardDeck.suits.index(card.suit)
        return suitNum * 13 + card.number - 1



if __name__ == '__main__':
    unittest.main()