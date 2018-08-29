import re
import sys
import numpy as np

def simple_multi(file1, file2):
    """
    :param file1: name of a txt file contains a matrix (str)
    :param file2: name of a txt file contains a vector (as a row) (str)
    :return: return the multiplication result (list)
    """

    matrix = sc.textFile(file1)
    vector = sc.textFile(file2)

    matrix = matrix.map(lambda r: [float(i) for i in r.split(',')]).cache()
    vector = vector.flatMap(lambda v: [float(i) for i in v.split(',')]).collect()

    result_vector = matrix.map(lambda r: np.dot(r, vector)).collect()

    return result_vector

def add_index1(l):
    """
    :param l: a list of (row index, element) (list)
    :return: a list of (row_index, (element,col_index)) (list)
    """
    for i in range(len(l[1])):
        yield tuple([l[0], tuple([l[1][i],i])])

def add_index2(l):
    """
    :param l: a list of (element) (for column) (list)
    :return: a list of (col_index, element) (list)
    """
    for i in range(len(l)):
        yield tuple([i, l[i]])


def advance_multi(file1, file2):

    """
    :param file1: name of a txt file contains a matrix (str)
    :param file2: name of a txt file contains a vector (as a row) (str)
    :return: return the multiplication result (list)
    """

    # step1: read in lines
    matrix = sc.textFile(file1)
    matrix = matrix.map(lambda r: tuple([i for i in r.split(':')]))
    matrix = matrix.map(lambda r: tuple([int(r[0]), tuple([float(i) for i in r[1].split(',')])]))
    vector = sc.textFile(file2)
    vector = vector.map(lambda v: tuple([float(i) for i in v.split(',')]))

    # step2: add column index to each matrix element: (i, (aij,j))
    matrix = matrix.flatMap(add_index1)

    # step3: add column index to each vector element: (j,vj)
    vector = vector.flatMap(add_index2).collect()

    # step4: calculate the element*element product for each row position j: (i,aij*vj)
    product = matrix.map(lambda r: tuple([r[1][1], tuple([r[0], r[1][0]])]))
    product = product.map(lambda r: tuple([r[0], tuple(list(r[1]) + [vector[r[0]][1]])]))
    product = product.map(lambda r: tuple([r[1][0], r[1][1] * r[1][2]]))

    # step5: sum the element-wise product for each row: (i,sum(aij*vj))
    product_sum = product.reduceByKey(lambda n1, n2: n1 + n2).map(lambda x: x[1]).collect()

    return product_sum

if __name__ == "__main__":
    advance_multi(sys.argv[1], sys.argv[2])
