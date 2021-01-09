import numpy as np
from sklearn.cluster import KMeans
from random import randint
import stddraw

stddraw.setXscale(0, 200)
stddraw.setYscale(0, 200)

def dataset():
    a1, a2, a3 = [], [], []
    xx1, yy1, rr1, xx2, yy2, rr2 = randint(50, 150), randint(50, 150), randint(10, 70), randint(50, 150), randint(50, 150), randint(10, 70)
    for i in range(10000):
        x = randint(0, 200)
        y = randint(0, 200)
        a1.append([x, y])
        if 25**2 <= (x-50)**2+(y-50)**2 <= 50**2 or (x-50)**2+(y-50)**2 <= 10**2:
            a2.append([x, y])
        if (x - xx1)**2 + (y - yy1)**2 <= rr1**2 or (x - xx2)**2 + (y - yy2)**2 <= rr2**2:
            a3.append([x, y])
    a1 = np.array(a1)
    a2 = np.array(a2)
    a3 = np.array(a3)
    return a1, a2, a3


def paint(labels,arr):
    for i in range(len(labels)):
        if labels[i]==0:
            stddraw.setPenColor(stddraw.BLUE)
        if labels[i]==1:
            stddraw.setPenColor(stddraw.YELLOW)
        stddraw.point(arr[i][0], arr[i][1])


a, b, c = dataset()
data = c
kmeans = KMeans(n_clusters=2, random_state=0).fit(data)
paint(kmeans.labels_, data)
for i in range(len(kmeans.cluster_centers_)):
    stddraw.setPenColor(stddraw.RED)
    stddraw.point(kmeans.cluster_centers_[i][0], kmeans.cluster_centers_[i][1])
stddraw.show()

