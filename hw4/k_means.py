import re
import sys
import numpy as np


def find_nearest_c(dp, cen):
    """
    :param dp: a data point coordinate (a row of RDD)
    :param cen: a list of centroid coordinates (list)
    :return: (cluster index, data point coordinate)
    """
    min_dist = float(np.Inf)
    min_dist_index = 0

    for i in range(len(cen)):
        c = cen[i][0]
        dist = np.linalg.norm(dp - c)

        if dist < min_dist:
            min_dist = dist
            min_dist_index = i

    return (min_dist_index, dp)


def check_equal(check0, check1):
    """
    :param check0: one iteration before centroids RDD
    :param check1: the latest centroids RDD
    :return: return True if two RDD contains the same centroid coordinates (regardless the order); False otherwise
    """

    check0 = check0.map(lambda r: r[0]).collect()
    check1 = check1.map(lambda r: r[0]).collect()
    for i in check0:
        check = False
        for j in check1:
            if (i == j).all():
                check = True
                break
        if check == False:
            return False
    return True


def k_means(file_data, file_centroid):
    """
    :param file_data: name of a txt file including all data points coordinates
    :param file_centroid: name of a txt file including the initial centroid points coordinates
    :return: a RDD object includes the finalized centroid points information
    """

    # Load the data
    data = sc.textFile(file_data).map(lambda line: np.array([float(x) for x in line.split(' ')])).cache()

    # Load the initial centroids
    centroids = sc.textFile(file_centroid).map(lambda line: np.array([float(x) for x in line.split(' ')])).cache()
    centroids = centroids.zipWithIndex()
    centroids_list = centroids.collect()

    iteration = 0

    while (iteration < 100):

        # group the data
        data_group = data.map(lambda dp: find_nearest_c(dp, centroids_list))
        data_group = data_group.groupByKey().map(lambda g: (g[0], list(g[1])))

        # update the centroids
        previous_centroids = centroids
        centroids = data_group.map(lambda g: (np.mean(g[1], axis=0), g[0]))
        centroids_list = centroids.collect()

        # check if to stop
        if check_equal(previous_centroids, centroids):
            print(iteration)
            break

        iteration += 1

    return centroids.map(lambda r: r[0])

if __name__ == "__main__":
    k_means(sys.argv[1], sys.argv[2])



