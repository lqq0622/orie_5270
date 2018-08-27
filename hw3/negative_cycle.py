import os
import copy
import sys


def readtxt(file_name):

    """
    :param file_name: a txt file contains a graph
                      every two line will a node and list((neighbour node, weight btw)...) (str)
    :return: a graph stored in a dict
             key: node value
             value: list of [neighbour node key, weight bet]
    """

    if os.path.isfile(file_name) != True:
        return {}

    else:
        reader = open(file_name)

        graph_dict = {}

        while (True):
            node = reader.readline().replace('\n', '')
            neighbour = reader.readline().replace('\n', '')

            if (not node):
                break

            if neighbour == ['']:
                graph_dict[int(node)] = []

            else:
                new = []
                neighbour = neighbour.split(',')

                for i in range(len(neighbour) // 2):
                    new.append([int(neighbour[2 * i][1:]), float(neighbour[2 * i + 1][:-1])])

                graph_dict[int(node)] = new

        return graph_dict


def find_prev_node(graph, w):

    """
    :param graph: a graph dictionary (dict)
    :param w: a node key value (int)
    :return: a list of key values of the nodes pointed to w
    """

    # find the node before w
    prev_node = []

    for k in graph.keys():
        for node_weight in graph[k]:
            if node_weight[0] == w:
                prev_node.append([k, node_weight[1]])

    return prev_node


def BellmanFord(graph, s, t, steps='default'):

    """
    :param graph: a graph stored in a dict (dict)
    :param s: the starting node key value (int)
    :param t: the ending node key value (int)
    :param steps: the number of steps allowed to find the shortest path (default value is number of node - 1) (int)
    :return: [shortest path length, nodes in path]
            (the value will be accurate if no negative cycle)
    """

    if graph == {}:
        return []

    # shortest path dictionary (path length to t)
    M = {}

    for k in graph.keys():
        M[k] = float('Inf')
    M[t] = 0

    # shortest path dictionary (next node)
    N = {}

    for k in graph.keys():
        N[k] = None

    # previous updated or not
    update = [t]
    update_next = []

    # find the shortest path
    if steps == 'default':
        steps = len(graph.keys()) - 1

    for i in range(steps):
        for w in update:
            for prev_w in find_prev_node(graph, w):
                v = prev_w[0]
                weight = prev_w[1]

                if M[w] + weight < M[v]:
                    M[v] = M[w] + weight
                    N[v] = w
                    update_next.append(v)

        if update_next == []:
            break
        else:
            update = update_next
            update_next = []

    if s == t:
        return [M[t], [t]]

    path = []
    path.append(s)
    current = s

    while (True):
        if N[current] == None:
            return "no path exists"
        elif N[current] == t:
            path.append(t)
            break
        elif N[current] in path:
            path = path[path.index(N[current]):]
            break
        else:
            path.append(N[current])
            current = N[current]

    return [M[s], path]


def negative_cycle(name_txt_file):

    """
    :param name_txt_file: the name of a txt file including a graph (str)
    :return: [nodes in negative cycle] or the message "There is no negative cycle"
    """

    # read from txt file
    graph = readtxt(name_txt_file)

    # add a new node
    for k in graph.keys():
        graph[k].append(['add', 0])
    graph['add'] = []

    # new graph node number
    n = len(graph.keys())

    # check for cycle
    for k in graph.keys():
        if BellmanFord(graph, k, 'add', n)[0] < BellmanFord(graph, k, 'add', n - 1)[0]:
            path = BellmanFord(graph, k, 'add', n)[1]
            print(path)
            return path

    print("There is no negative cycle")
    return "There is no negative cycle"


if __name__ == "__main__":
    negative_cycle(sys.argv[1])

