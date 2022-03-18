import unittest
from GameState import GameState
from CardStack import CardStack

class TestGameState(unittest.TestCase):

    def testStateStackLen(self):
        testState = GameState(None)
        for i in range(len(testState.cardStacks)):
            self.assertEqual(len(testState.cardStacks[i].cards), i + 1)

    def testStateStackBackNum(self):
        testState = GameState(None)
        for i in range(len(testState.cardStacks)):
            self.assertEqual(testState.cardStacks[i].backNum, i)

    def testStateWin(self):
        testState = GameState(None)
        testState.cardStacks = [CardStack(0) for i in range(testState.numCardStacks)]
        self.assertEqual(testState.isGameOver(), True)



if __name__ == '__main__':
    unittest.main()