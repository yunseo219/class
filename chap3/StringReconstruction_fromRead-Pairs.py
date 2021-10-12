import sys
from re import split
from random import choice
from collections import defaultdict

#NOT SUBMITTED NOT WORKING
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

'''
def StringSpelledByGappedGenome(gappedpatterns, k, d):
    firstPattern = [pattern.split('|')[0] for pattern in gappedpatterns ]
    secondPattern = [pattern.split('|')[1] for pattern in gappedpatterns ]
    preffixstr = stringSpelledByPatterns(firstPattern,k)
    suffixstr = stringSpelledByPatterns(secondPattern,k)
    combstr = k+d 
    if preffixstr[combstr:] == preffixstr[combstr:]:
        return preffixstr + suffixstr[-(combstr):]

def stringSpelledByPatterns(patterns,k):
    stringPat = [patterns[0]]
    for pattern in patterns[1:]:
        stringPat.append(pattern[-1])
    return ''.join(stringPat)

'''
def StringSpelledByGappedPatterns(GappedPatterns, k, d):
    prefix_string = ''
    suffix_string = ''
    for i, pattern_pair in enumerate(GappedPatterns):
        if i != len(GappedPatterns) - 1:
            prefix_string += pattern_pair[0][0]
            suffix_string += pattern_pair[1][0]
        else:
            prefix_string += pattern_pair[0]
            suffix_string += pattern_pair[1]
    for i in range(k + d + 1, len(prefix_string)):
        if prefix_string[i] != suffix_string[i - k - d - 1]:
            return -1
    return prefix_string + suffix_string[len(suffix_string) - k - d - 1:]

def DeBruijnwithreadpairs(paired_reads):
    adj_list = defaultdict(list)
    for pair in paired_reads:
        adj_list[(pair[0][:-1], pair[1][:-1])].append((pair[0][1:], pair[1][1:]))
    return adj_list

def StringReconstructionwithReadpairs(k, d, paired_reads):
    adj_list = DeBruijnwithreadpairs(paired_reads)
    path = EulerianPath(adj_list)
    return StringSpelledByGappedPatterns(path, k - 1, d)

filename = 'dataset_442816_16.txt'
with open(filename) as f:
    lines = f.read().splitlines()
    k = int(lines[0].split()[0])
    d = int(lines[0].split()[1])
    pairedKmers = lines[1:]
        
    adjlist,nodes = build_deGruijnGraphFromPairedKmers(pairedKmers)
    numedge = 0
    for v in adjlist.keys():
        numedge += len(adjlist[v])

    path = eupath.eulerian_path(adjlist)
    patterns = [nodes[p] for p in path]
    string = gappedString.stringSpelledByGappedPatterns(patterns,k,d)
    print string