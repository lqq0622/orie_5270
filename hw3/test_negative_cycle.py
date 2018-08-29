import unittest

from negative_cycle import negative_cycle


class TestNegativeCycle(unittest.TestCase):
    def setUp(self):
        self.file1 = "graph1.txt"
        self.file2 = "graph2.txt"
        self.file3 = "graph3.txt"
        self.file4 = "graph4.txt"
        self.answer1 = [5, 7, 8]
        self.answer2 = "There is no negative cycle"
        self.answer3 = [1, 2, 3]
        self.answer4 = "There is no negative cycle"

    def test_1(self):
        assert negative_cycle(self.file1) == self.answer1

    def test_2(self):
        assert negative_cycle(self.file2) == self.answer2

    def test_3(self):
        assert negative_cycle(self.file3) == self.answer3

    def test_4(self):
        assert negative_cycle(self.file4) == self.answer4


if __name__ == "__main__":
    unittest.main()
