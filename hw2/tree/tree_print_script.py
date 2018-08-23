import numpy as np


class Tree(object):
    def __init__(self, root):
        """
        :param root: (Node)
        """
        self.root = root

    def print_tree(self):

        if self.root is None:
            return []

        else:
            node_list = []
            node_list.append(self.root)

            print_list = []
            local_list = []

            current_count = 1
            next_count = 0

            while current_count > 0:
                my_node = node_list.pop(0)

                if my_node is not None:
                    local_list.append(my_node.value)

                    if my_node.left is not None:
                        node_list.append(my_node.left)
                    else:
                        node_list.append(None)

                    if my_node.right is not None:
                        node_list.append(my_node.right)
                    else:
                        node_list.append(None)

                else:
                    local_list.append('|')
                    node_list.append(None)
                    node_list.append(None)

                current_count -= 1
                next_count += 2

                if current_count == 0:
                    print_list.append(local_list)
                    local_list = []
                    current_count = next_count
                    next_count = 0

                    if all(x is None for x in node_list):
                        break

            if len(print_list) == 1:
                return print_list[0]
            else:
                print_list_new = []

                level = len(print_list)
                base = 2 ** level - 1

                first = list(np.repeat('|', (base - 1) // 2)) + [print_list[0][0]] + list(
                    np.repeat('|', (base - 1) // 2))
                print_list_new.append(first)

                for i in range(1, level):
                    interval = 2 ** (level - i) - 1
                    temp = []

                    for j in range(len(print_list[i]) - 1):
                        temp.append(print_list[i][j])
                        temp = temp + list(np.repeat('|', interval))

                    temp.append(print_list[i][-1])

                    if len(temp) != base:
                        temp = list(np.repeat('|', (base - len(temp)) // 2)) + temp + list(
                            np.repeat('|', (base - len(temp)) // 2))

                    print_list_new.append(temp)

                # print(np.matrix(print_list_new))
                return print_list_new


class Node(object):
    def __init__(self, value, left, right):
        """
        :param value: (float)
        :param left: (Node)
        :param right: (Node)
        """
        self.value = value
        self.left = left
        self.right = right
