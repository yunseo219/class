import math


def Euclidean_distance(v, w):
    distance = 0
    for i in range(len(v)):
        distance += ((v[i] - w[i])*(v[i] - w[i]))
    distance = math.sqrt(distance)
    return distance


def Closet_Center(Datapoint, Centers):
    closest = float("Inf")
    for i in Centers:
        current = Euclidean_distance(i, Datapoint)
        if  closest > current:
            closest = current
            dist = i
    return dist



'''
We define the center of gravity of Data as the point 
whose i-th coordinate is the average of the i-th coordinates of all points from Data. 

'''

def CenterOfGravity(Datapoint):
	center = [0]*len(Datapoint[0])
	for i in range(len(Datapoint)):
		for j in range(len(Datapoint[0])):
			center[j] += float(Datapoint[i][j])/len(Datapoint)
	return center


'''
Centers to Clusters: After centers have been selected, 
assign each data point to the cluster corresponding to its nearest center; 
ties are broken arbitrarily.
Clusters to Centers: After data points have been assigned to clusters, 
assign each cluster’s center of gravity to be the cluster’s new center.
'''

def Lloyd_kmeans(Data, k):
    Centers = Data[:k]
    while True:
    	clusters = ClustersTonearest(Data, Centers)
    	newCenter = NewCenter(Data, Datapoint, k)
    	if newCenter == Centers:
    		break
    	Centers = newCenter
    	return Centers

def ClustersTonearest(Data, Centers):
    Cluster_dict = defaultdict(list)
    for Datapoint in Data:
    	center = Closet_Center(Datapoint, Centers)
    	Cluster_dict[center].append(Datapoint)
    return Centers

def NewCenter(Data, Datapoint, k): 
	Cluster_dict = ClustersTonearest(Data, Centers)
	new = [[],] * k
	for i in range(k):
		new[i] = cluster_mean(Cluster_dict[(Centers[i])])
	return new

if __name__ == '__main__':
    filename = 'dataset_442915_3.txt'
    with open(filename) as f:
        lines = f.read().splitlines()
    k = int(lines[0].split(' ')[0])
    Data = [[float(x) for x in line.split()] for line in lines[1:]]
    for i in Lloyd_kmeans(Data, k):
    	print(' '.join([str(x) for x in i]))