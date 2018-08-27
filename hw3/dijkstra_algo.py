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

        while True:
            node = reader.readline().replace('\n', '')
            neighbour = reader.readline().replace('\n', '')

            if not node:
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


def find_shortest_path(name_txt_file, source, destination):

    """
    :param name_txt_file: name of a txt file including a graph (str)
    :param source: staring node key value (int)
    :param destination: ending node key value (int)
    :return: [shortest path length, [nodes on path]] or the message "no path exists"
    """

    graph = readtxt(name_txt_file)

    S = []
    F = [source]
    d = {}
    bk = {}
    d[source] = 0

    for k in graph.keys():
        bk[k] = None

    while F != []:
        if len(F) == 1:
            f = F[0]
        else:
            f = F[0]
            for node in F[1:]:
                if d[node] < d[f]:
                    f = node

        F.remove(f)
        S.append(f)

        for node_weight in graph[f]:
            w = node_weight[0]
            weight = node_weight[1]

            if (w not in S) and (w not in F):
                d[w] = d[f] + weight
                F.append(w)
                bk[w] = f
            else:
                if d[f] + weight < d[w]:
                    d[w] = d[f] + weight
                    bk[w] = f

    if source == destination:
        print([d[source], [source]])
        return [d[source], [source]]

    else:
        path = []
        path.append(destination)
        current = destination

        while (True):
            if bk[current] == None:
                print("no path exists")
                return "no path exists"
            elif bk[current] == source:
                path = [source] + path
                break
            else:
                path = [bk[current]] + path
                current = bk[current]

        print([d[destination], path])
        return [d[destination], path]


if __name__ == "__main__":
    find_shortest_path(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

