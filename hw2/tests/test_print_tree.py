import unittest
# import numpy as np
# import numpy.testing as npt

from tree.tree_print_script import Tree, Node


class TestPrintTree(unittest.TestCase):

    def setUp(self):
        self.tree1 = Tree(None)
        self.tree2 = Tree(Node(1, None, None))
        self.tree3 = Tree(Node(1, Node(2, Node(4, None, None), Node(5, None, None)),
                               Node(3, Node(6, None, None), Node(7, None, None))))
        self.tree4 = Tree(Node(1, Node(2, Node(3, Node(4, None, None), None), None), None))
        self.tree5 = Tree(Node(1, Node(2, None, Node(4, Node(6, None, None), None)),
                               Node(3, Node(5, Node(7, None, None), None), None)))

        self.answer1 = []
        self.answer2 = [1]
        self.answer3 = [['|', '|', '|', 1, '|', '|', '|'],
                        ['|', 2, '|', '|', '|', 3, '|'],
                        [4, '|', 5, '|', 6, '|', 7]]
        self.answer4 = [['|', '|', '|', '|', '|', '|', '|', 1, '|', '|', '|', '|', '|', '|', '|'],
                        ['|', '|', '|', 2, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                        ['|', 3, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                        [4, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]
        self.answer5 = [['|', '|', '|', '|', '|', '|', '|', 1, '|', '|', '|', '|', '|', '|', '|'],
                        ['|', '|', '|', 2, '|', '|', '|', '|', '|', '|', '|', 3, '|', '|', '|'],
                        ['|', '|', '|', '|', '|', 4, '|', '|', '|', 5, '|', '|', '|', '|', '|'],
                        ['|', '|', '|', '|', 6, '|', '|', '|', 7, '|', '|', '|', '|', '|', '|']]

    def test_none_tree(self):
        assert self.tree1.print_tree() == self.answer1

    def test_one_node_tree(self):
        assert self.tree2.print_tree() == self.answer2

    def test_balance_tree(self):
        assert self.tree3.print_tree() == self.answer3

    def test_unbalance_tree(self):
        assert self.tree4.print_tree() == self.answer4

    def test_mix_tree(self):
        assert self.tree5.print_tree() == self.answer5

