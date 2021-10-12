import math

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
        if closest > current:
            closest = current
    return closest
'''
Distortion(Data,Centers) = (1/n) ∑all points DataPoint in Datad(DataPoint, Centers)^2 .
Note that whereas MaxDistance(Data, Centers) only accounts for the length of the single red segment in the figure below, the squared error distortion accounts for the length of all segments in this figure.

'''

def SquaredError_Distortion(Data, Centers):
    distortion = 0
    n = len(Data)
    for Datapoint in Data:
        distortion += (Closet_Center(Datapoint, Centers) * Closet_Center(Datapoint, Centers))/n
    return distortion


if __name__ == '__main__':
    filename = 'dataset_442914_3.txt'
    with open(filename) as f:
        lines = f.read().splitlines()
    k = int(lines[0].split(' ')[0])
    Centers = [[float(x) for x in line.split()] for line in lines[1:k + 1]]
    Data = [[float(x) for x in line.split()] for line in lines[k + 2:]]
    print(SquaredError_Distortion(Data, Centers))

    #22.46506675567425