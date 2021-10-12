import sys 
from random import choice
from re import split


def DeBruijnwithkmers(patterns):
    adj_list = {}
    for pattern in patterns:
        if pattern[:-1] not in adj_list:
            adj_list[pattern[:-1]] = [pattern[1:]]
        else:
            adj_list[pattern[:-1]].append(pattern[1:])
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

def k_UniversalCirString(k):
    kmers = []
    for i in range(2 ** k):
        kmer = str(bin(i))[2:]
        if len(kmer) != k:
            kmer = '0' * (k - len(kmer))+ kmer
        kmers.append(kmer)
    adj_list = DeBruijnwithkmers(kmers)
    circularstr = EulerianCycle(adj_list)
    circularstr = circularstr[:len(circularstr) - k + 1]
    string = circularstr[0][:-1]
    for r in circularstr:
        string += r[-1]
    return string

file = 'dataset_442815_11.txt'
with open(file) as f:
	lines = f.read().splitlines()
	k = int(lines[0])

print(k_UniversalCirString(k))