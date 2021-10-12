import sys
from random import choice
from re import split

def Adjacent_lists(adjtext):
    adj_list = {}
    for adjs in adjtext:
        temp = split(' -> ', adjs)
        adj_list[temp[0]] = temp[1].split(',')
    return adj_list

def RemoveEdges(adj_list, fromNodes, endNodes):
    adj_list[fromNodes].remove(endNodes)
    if not adj_list[fromNodes]: #not empty
        del adj_list[fromNodes] #then delete it 
    return adj_list

def MaxNonBranchingPath(adj_list):
    paths = []
    degrees = {}
    for startin, targets in adj_list.items():
        if startin not in degrees:
            degrees[startin] = [0, len(targets)]
        else:
            degrees[startin][1] = degrees[startin][1] + len(targets)
        for target in targets:
            if target not in degrees:
                degrees[target] = [1, 0]
            else:
                degrees[target][0] = degrees[target][0] + 1
    for x in list(degrees): #search 
        if degrees[x] != [1, 1]:
            if degrees[x][1] > 0:
                while x in adj_list:
                    y = adj_list[x][0]
                    non_branching= [x, y]
                    adj_list = RemoveEdges(adj_list, x, y)
                    while degrees[y] == [1, 1]:
                        z = adj_list[y][0]
                        non_branching.append(z)
                        adj_list = RemoveEdges(adj_list, y, z)
                        y = z
                    paths.append(non_branching)
    true = adj_list
    while true: 
        currN = adj_list[startN][0]
        startN = list(adj_list)[0]
        cycle = [startN, currN]
        adj_list = RemoveEdges(adj_list, startN, currN)
        while currN != startN:
            targetN = adj_list[currN][0]
            cycle.append(targetN)
            adj_list = RemoveEdges(adj_list, currN, targetN)
            currN = targetN
        paths.append(cycle)
    return paths

file = 'dataset_442821_2 (1).txt'
with open(file) as f:
    lines = f.read().splitlines()
    Adj_list = Adjacent_lists(lines)
    lines = MaxNonBranchingPath(Adj_list)
    for line in lines: 
        print("->".join(line))