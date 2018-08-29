import unittest

from dijkstra_algo import find_shortest_path


class TestDijkstraAlgo(unittest.TestCase):
    def setUp(self):
        self.filename = "graph4.txt"
        self.answer1 = [0, [1]]
        self.answer2 = [1.0, [1, 2]]
        self.answer3 = [1.0, [1, 3]]
        self.answer4 = [2.0, [1, 2, 4]]

    def test_1(self):
        assert find_shortest_path(self.filename, 1, 1) == self.answer1

    def test_2(self):
        assert find_shortest_path(self.filename, 1, 2) == self.answer2

    def test_3(self):
        assert find_shortest_path(self.filename, 1, 3) == self.answer3

    def test_4(self):
        assert find_shortest_path(self.filename, 1, 4) == self.answer4


if __name__ == "__main__":
    unittest.main()
