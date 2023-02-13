#Construct the de Bruijn graph from a set of k-mers.
#Eulerian Cycle one node has path in and out to create circle in the graph
# in = out for each node -> balanced graph

#Input: A collection of k-mers Patterns.
#Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).

"""
Sample Input:
GAGG
CAGG
GGGG
GGGA
CAGG
AGGG
GGAG

Sample Output:
AGG -> GGG
CAG -> AGG,AGG
GAG -> AGG
GGA -> GAG
GGG -> GGA,GGG
"""

import sys,random
from re import split
from random import choice

def Adjacent_lists(adj_list_text):
    adj_list = {}
    for elem in adj_list_text:
        temp = split(' -> ', elem)
        adj_list[temp[0]] = temp[1].split(',')
    return adj_list


def EulerianCycle(adj_list):
    startN, edges = choice(list(adj_list.items())) #form with random 
    targetN = choice(edges)
    Cycle = [startN, targetN]
    currN = targetN
    adj_list = RemoveEdges(adj_list, startN, targetN) 
    while currN != startN:
        edges = adj_list[currN]
        targetN = choice(edges)
        #adj_list = RemoveEdges(adj_list, currN, targetN)
        #adj_list[currN].remove(targetN)
        if not adj_list[currN]: #not empty
        	del adj_list[currN] #then delete it 
        currN = targetN
        Cycle.append(currN)
    true = adj_list
    while true:
        beginwith = [(idx, node) for idx, node in enumerate(Cycle) if node in adj_list]
        idx, new_start = choice(beginwith)
        TraverseCycle = Cycle[idx:] + Cycle[1:idx + 1]
        targetN = choice(adj_list[new_start])
        #adj_list = RemoveEdges(adj_list, new_start, targetN)
        #adj_list[currN].remove(targetN)
        if not adj_list[currN]: #not empty
        	del adj_list[currN] #then delete it 
        currN = targetN
        TraverseCycle.append(currN)
        while currN != new_start:
            edges = adj_list[currN]
            targetN = choice(edges)
            #adj_list = RemoveEdges(adj_list, currN, targetN)
        	#adj_list[currN].remove(targetN)
        	if not adj_list[currN]: #not empty
        		del adj_list[currN] #then delete it 
            currN = targetN
            TraverseCycle.append(currN)
        Cycle = TraverseCycle
    return Cycle

'''
def RemoveEdges(adj_list, fromNodes, endNodes):
    adj_list[fromNodes].remove(endNodes)
    if not adj_list[fromNodes]: #not empty
        del adj_list[fromNodes] #then delete it 
    return adj_list
'''


file = 'dataset_442815_2.txt'
with open(file) as f:
	lines = f.read().splitlines()
    adj_list = Adjacent_lists(lines)
	print("->".join(EulerianCycle(adj_list)))


