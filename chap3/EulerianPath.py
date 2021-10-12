import sys
from random import choice
from re import split

def Adjacent_lists(adjtext):
    adj_list = {}
    for adjs in adjtext:
        temp = split(' -> ', adjs)
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
        adj_list = RemoveEdges(adj_list, currN, targetN)
        currN = targetN
        Cycle.append(currN)
    true = adj_list
    while true:
        beginwith = [(idx, node) for idx, node in enumerate(Cycle) if node in adj_list]
        idx, new_start = choice(beginwith)
        TraverseCycle = Cycle[idx:] + Cycle[1:idx + 1]
        targetN = choice(adj_list[new_start])
        adj_list = RemoveEdges(adj_list, new_start, targetN)
        currN = targetN
        TraverseCycle.append(currN)
        while currN != new_start:
            edges = adj_list[currN]
            targetN = choice(edges)
            adj_list = RemoveEdges(adj_list, currN, targetN)
            currN = targetN
            TraverseCycle.append(currN)
        Cycle = TraverseCycle
    return Cycle

def RemoveEdges(adj_list, fromNodes, endNodes):
    adj_list[fromNodes].remove(endNodes)
    if not adj_list[fromNodes]: #not empty
        del adj_list[fromNodes] #then delete it 
    return adj_list

def EulerianPath(adj_list):
    diff = {}
    for froms, ends in adj_list.items():
        if froms in diff:
            diff[froms] += len(ends)
        else:
            diff[froms] = len(ends)
        for end in ends:
            if end in diff:
                diff[end] -= 1
            else:
                diff[end] = -1
    addi = [node for node, diffin in diff.items() if diffin == -1][0]
    addj = [node for node, diffin in diff.items() if diffin == 1][0]
    if addi in adj_list:
        adj_list[addi].append(addj)
    cycle = EulerianCycle(adj_list)
    idex = 0
    while True:
        if cycle[idex] == addi and cycle[idex + 1] == addj:
             break
        idex = idex + 1
    return cycle[idex + 1:] + cycle[1:idex + 1]

file = 'dataset_442815_6.txt'
with open(file) as f:
	lines = f.read().splitlines()
	Adj_list = Adjacent_lists(lines)

print("->".join(EulerianPath(Adj_list)))