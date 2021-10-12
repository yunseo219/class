import math

'''
First, we define the Euclidean distance between points v = (v1, ... , vm) and w = (w1, ... , wm) in m-dimensional space, 
denoted d(v, w), as the length of the line segment connecting these points,

'''
def Euclidean_distance(v, w):
    distance = 0
    for i in range(len(v)):
        distance += ((v[i] - w[i])*(v[i] - w[i]))
    distance = math.sqrt(distance)
    return distance
'''
Next, given a point DataPoint in multi-dimensional space and a set of k points Centers, 
we define the distance from DataPoint to Centers, denoted d(DataPoint, Centers), 
as the Euclidean distance from DataPoint to its closest center,

'''
def Closet_Center(Datapoint, Centers):
    closest = float('inf')
    for i in Centers:
        current = Euclidean_distance(i, Datapoint)
        if closest > current :
            closest = current
    return closest

'''
This distance, denoted MaxDistance(Data, Centers), 
is the maximum of d(DataPoint, Centers) among all data points DataPoint,
MaxDistance(Data, Centers) = max all points DataPoint from Data d(DataPoints,Centers).
'''
def MaxDistance(Data, Centers): 
    Maxdist = 0.0
    for Datapoint in Data:
        current = Closet_Center(Datapoint, Centers)
        if  Maxdist < current:
            Maxdist = current
            point = Datapoint #update max all datapoints
    return point

'''
﻿FarthestFirstTraversal(Data, k) 
    Centers ← the set consisting of a single randomly chosen point from Data
    while |Centers| < k 
        DataPoint ← the point in Data maximizing d(DataPoint, Centers) 
        add DataPoint to Centers 
    return Centers
'''

def FarthestFirstTraversal(Data, k):
    Centers = [Data[0]]
    while len(Centers) < k:
        Datapoint = MaxDistance(Data, Centers)
        Centers.append(Datapoint)
    return Centers


if __name__ == '__main__':
    filename = 'dataset_442913_2.txt'
    with open(filename) as f:
        lines = f.read().splitlines()
    k = int(lines[0].split(' ')[0])
    Data = [[float(x) for x in line.split()] for line in lines[1:]]
    for i in FarthestFirstTraversal(Data, k):
        print(' '.join([str(x) for x in i ]))



'''
0.4 10.5 12.5
37.2 4.1 16.2
31.4 26.1 0.1
8.8 36.1 11.8
9.5 7.9 35.8
18.4 0.4 0.2
'''