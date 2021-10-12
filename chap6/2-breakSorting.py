'''
2-BREAKONGENOMEGRAPH(GenomeGraph, i, i’, j, j’)
remove colored edges (i, i’) and (j, j’) from GenomeGraph
add colored edges (i, j) and (i’, j’) to GenomeGraph
return GenomeGraph

2-BREAKONGENOME(P, i, i’, j, j’)
GenomeGraph BLACKEDGES(P) and COLOREDEDGES(P)
GenomeGraph 2-BREAKONGENOMEGRAPH(GenomeGraph, i, i’, j, j’)
P GRAPHTOGENOME(GenomeGraph)
return P

SHORTESTREARRANGEMENTSCENARIO(P, Q)
output P
RedEdges COLOREDEDGES(P)
BlueEdges COLOREDEDGES(Q)
BreakpointGraph the graph formed by RedEdges and BlueEdges
while BreakpointGraph has a non-trivial cycle Cycle
(j, i’) an arbitrary edge from BlueEdges in a nontrivial red-blue cycle
(i, j) an edge from RedEdges originating at node j
(i’, j’) an edge from RedEdges originating at node i’
RedEdges RedEdges with edges (i, j) and (i’, j’) removed
RedEdges RedEdges with edges (j, i’) and (j’, i) added
BreakpointGraph the graph formed by RedEdges and BlueEdges
P 2-BREAKONGENOME(P, i, i’, j, j’)
output P


'''




def 2-breakSorting():
