import random
import numpy
import pandas

listening_time = [3,5,6,7,14,17,18,23,29,31]
print("Listening Times:", listening_time)
print("-------------------------------------------------")
k = 3
array_size = len(listening_time)-1

centroid_one = listening_time[random.randint(0, array_size)]
centroid_two = listening_time[random.randint(0, array_size)]
centroid_three = listening_time[random.randint(0, array_size)]

if centroid_two == centroid_one:
    while centroid_two == centroid_one:
        centroid_two = listening_time[random.randint(0, array_size)]

if centroid_three == centroid_one:
    while centroid_three == centroid_one:
        centroid_three = listening_time[random.randint(0, array_size)]

if centroid_three == centroid_two:
    while centroid_three == centroid_two:
        centroid_two = listening_time[random.randint(0, array_size)]

centroids = [centroid_one, centroid_two, centroid_three]
centroids = sorted(centroids)

def calculate_distance(centroids):
    cluster_one = []
    cluster_two = []
    cluster_three = []
    for i in range(0, len(listening_time)):
        distances = []
        for j in range(0, len(centroids)):
            distance = centroids[j] - listening_time[i]
            distance = abs(distance)
            distances.append(distance)
        if distances[0] <= distances[1]:
            if distances[0] <= distances[2]:
                cluster_one.append(listening_time[i])
            else:
                cluster_three.append(listening_time[i])
        else:
            if distances[1] <= distances[2]:
                cluster_two.append(listening_time[i])
            else:
                cluster_three.append(listening_time[i])
    return cluster_one, cluster_two, cluster_three


cluster_one, cluster_two, cluster_three = calculate_distance(centroids)
mean_c1 = numpy.mean(cluster_one)
mean_c2 = numpy.mean(cluster_two)
mean_c3 = numpy.mean(cluster_three)
old_centroids = centroids
centroids = []
centroids.append(mean_c1)
centroids.append(mean_c2)
centroids.append(mean_c3)
print("Previous Centroids:", old_centroids)
print("Cluster One:", cluster_one, "Mean:", mean_c1)
print("Cluster Two:", cluster_two,"Mean:", mean_c2)
print("Cluster Three:", cluster_three, "Mean:", mean_c3)
print("New Centroids:", centroids)
print("-------------------------------------------------")

if centroids[0] != old_centroids[0] or centroids[1] != old_centroids[1] or centroids[2] != old_centroids[2]:
    while centroids[0] != old_centroids[0] or centroids[1] != old_centroids[1] or centroids[2] != old_centroids[2]:
        cluster_one, cluster_two, cluster_three = calculate_distance(centroids)
        mean_c1 = numpy.mean(cluster_one)
        mean_c2 = numpy.mean(cluster_two)
        mean_c3 = numpy.mean(cluster_three)
        old_centroids = centroids
        centroids = []
        centroids.append(mean_c1)
        centroids.append(mean_c2)
        centroids.append(mean_c3)
        print("Previous Centroids:", old_centroids)
        print("Cluster One:", cluster_one, "Mean:", mean_c1)
        print("Cluster Two:", cluster_two,"Mean:", mean_c2)
        print("Cluster Three:", cluster_three, "Mean:", mean_c3)
        print("New Centroids:", centroids)
        print("-------------------------------------------------")

print("Final Centroids", centroids)
        



