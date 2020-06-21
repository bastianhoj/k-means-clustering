import matplotlib.pyplot as plt
import numpy as np
import math

center1 = (-50, -50)
center2 = (50, -50)
center3 = (50, 50)
center4 = (-50, 50)
standard_deviation = 40

x1 = np.random.normal(center1[0], standard_deviation, size=(100,))
y1 = np.random.normal(center1[1], standard_deviation, size=(100,))

x2 = np.random.normal(center2[0], standard_deviation, size=(100,))
y2 = np.random.normal(center2[1], standard_deviation, size=(100,))

x3 = np.random.normal(center3[0], standard_deviation, size=(100,))
y3 = np.random.normal(center3[1], standard_deviation, size=(100,))

x4 = np.random.normal(center4[0], standard_deviation, size=(100,))
y4 = np.random.normal(center4[1], standard_deviation, size=(100,))

cluster_x1, cluster_y1, cluster_x2, cluster_y2, cluster_x3, cluster_y3, cluster_x4, cluster_y4 = [], [], [], [], [], [], [], []

f1 = plt.figure(1)
plt.scatter(x1, y1, color="red")
plt.scatter(x2, y2, color="blue")
plt.scatter(x3, y3, color="orange")
plt.scatter(x4, y4, color="green")
plt.scatter(np.mean(x1), np.mean(y1), s=150, color="darkred")
plt.scatter(np.mean(x2), np.mean(y2), s=150, color="darkblue")
plt.scatter(np.mean(x3), np.mean(y3), s=150, color="darkorange")
plt.scatter(np.mean(x4), np.mean(y4), s=150, color="darkgreen")
f1.show()


def append_to_clusters(list_x, list_y):
    for i in range(0, len(list_x)):
        list_of_distance_to_means = [
            math.sqrt((list_x[i] - np.mean(x1)) ** 2 + (list_y[i] - np.mean(y1)) ** 2),
            math.sqrt((list_x[i] - np.mean(x2)) ** 2 + (list_y[i] - np.mean(y2)) ** 2),
            math.sqrt((list_x[i] - np.mean(x3)) ** 2 + (list_y[i] - np.mean(y3)) ** 2),
            math.sqrt((list_x[i] - np.mean(x4)) ** 2 + (list_y[i] - np.mean(y4)) ** 2)]
        if list_of_distance_to_means.index(min(list_of_distance_to_means)) == 0:
            cluster_x1.append(list_x[i])
            cluster_y1.append(list_y[i])
        elif list_of_distance_to_means.index(min(list_of_distance_to_means)) == 1:
            cluster_x2.append(list_x[i])
            cluster_y2.append(list_y[i])
        elif list_of_distance_to_means.index(min(list_of_distance_to_means)) == 2:
            cluster_x3.append(list_x[i])
            cluster_y3.append(list_y[i])
        elif list_of_distance_to_means.index(min(list_of_distance_to_means)) == 3:
            cluster_x4.append(list_x[i])
            cluster_y4.append(list_y[i])


j = 1

while True:
    j += 1
    append_to_clusters(x1, y1)
    append_to_clusters(x2, y2)
    append_to_clusters(x3, y3)
    append_to_clusters(x4, y4)

    if sum(x1) == sum(cluster_x1) and sum(y1) == sum(cluster_y1) and sum(x2) == sum(cluster_x2) and sum(y2) == sum(
            cluster_y2) and sum(x3) == sum(cluster_x3) and sum(y3) == sum(cluster_y3) and sum(x4) == sum(
            cluster_x4) and sum(y4) == sum(cluster_y4):
        break

    else:
        x1 = cluster_x1
        y1 = cluster_y1
        x2 = cluster_x2
        y2 = cluster_y2
        x3 = cluster_x3
        y3 = cluster_y3
        x4 = cluster_x4
        y4 = cluster_y4
        cluster_x1, cluster_y1, cluster_x2, cluster_y2, cluster_x3, cluster_y3, cluster_x4, cluster_y4 = [], [], [], [], [], [], [], []

    fx = plt.figure(j)
    plt.scatter(x1, y1, color="red")
    plt.scatter(x2, y2, color="blue")
    plt.scatter(x3, y3, color="orange")
    plt.scatter(x4, y4, color="green")
    plt.scatter(np.mean(x1), np.mean(y1), s=150, color="darkred")
    plt.scatter(np.mean(x2), np.mean(y2), s=150, color="darkblue")
    plt.scatter(np.mean(x3), np.mean(y3), s=150, color="darkorange")
    plt.scatter(np.mean(x4), np.mean(y4), s=150, color="darkgreen")
    fx.show()

plt.show()
