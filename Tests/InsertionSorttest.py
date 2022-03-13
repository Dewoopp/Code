import unittest
from InsertionSort import insertionSort

class TestInsertionSort(unittest.TestCase):

    def testSort(self):
        data = [4, 19, 2, 8, 1]
        dataSorted = sorted(data)
        insertionSort(data)
        self.assertEqual(dataSorted, data)

    def testSortBackwards(self):
        data = [5, 4, 3, 2, 1]
        dataSorted = sorted(data)
        insertionSort(data)
        self.assertEqual(dataSorted, data)

    def testSortBoth(self):
        data = [5, 4, 3, 2, 1]
        dataSorted = [1, 2, 3, 4, 5]
        insertionSort(data)
        self.assertEqual(dataSorted, data)

    def testSortSorted(self):
        data = [1, 2, 3, 4, 5]
        dataSorted = sorted(data)
        insertionSort(data)
        self.assertEqual(dataSorted, data)

    def testSortDecimal(self):
        data = [7.1111, 7.11, 7.11111, 7.111, 7.1]
        dataSorted = sorted(data)
        insertionSort(data)
        self.assertEqual(dataSorted, data)

    def testSortNegative(self):
        data = [-8, -1, -19, -20, -9, -81, -2]
        dataSorted = sorted(data)
        insertionSort(data)
        self.assertEqual(dataSorted, data)

    def testSortNegativePositive(self):
        data = [34, -8, 120, -1, 5, -19, -20, 89, -9, -81, -2, 8, 32]
        dataSorted = sorted(data)
        insertionSort(data)
        self.assertEqual(dataSorted, data)

    def testSortNegativePositiveBoth(self):
        data = [34, -8, 120, -1, 5, -19, -20]
        dataSorted = [-20, -19, -8, -1, 5, 34, 120]
        insertionSort(data)
        self.assertEqual(dataSorted, data)

    def testSortAllSame(self):
        data = [1, 1, 1, 1, 1, 1]
        dataSorted = sorted(data)
        insertionSort(data)
        self.assertEqual(dataSorted, data)

    def testSortEmpty(self):
        data = []
        dataSorted = []
        insertionSort(data)
        self.assertEqual(dataSorted, data)

if __name__ == '__main__':
    unittest.main()