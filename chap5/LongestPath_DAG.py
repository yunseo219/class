'''
LONGESTPATH(Graph, source, sink)
for each node b in Graph
sb = infinite
s source = 0 
topologicaly order graph
for each node b in graph - following tological 
sb = max (sa + weight of edge from a to b)
return s sink

TOPOLOGICALORDERING(Graph)
List empty list
Candidates set of all nodes in Graph with no incoming edges
while Candidates is non-empty
select an arbitrary node a from Candidates
add a to the end of List and remove it from Candidates
for each outgoing edge from a to another node b
remove edge (a, b) from Graph
if b has no incoming edges
add b to Candidates
if Graph has edges that have not been removed
return “the input graph is not a DAG”
else
return List

'''

from collections import defaultdict
import sys

def update_graph(graph):
    nodes = graph.keys()
    for node in graph.keys():
        links = graph[node]
        for link in links:
            if link[0] not in nodes:
                nodes.append(link[0])
    ''' make graph complete with only in-going nodes'''
    for node in nodes:
        if node not in graph.keys():
            graph[node] = []
    return graph,nodes

def acyclicLP(graph,s,v):
    global postorder,marked,nodes,distTo,edgeTo
    graph,nodes = update_graph(graph)
    edgeTo = {node:None for node in nodes}
    distTo = {node:float("-inf") for node in nodes}
    distTo[s] = 0
    depthFirstOrder(graph)
    topo_order = postorder[::-1]
    for node in topo_order:
        for edge in graph[node]:
            relax(node,edge[0],edge[1])
    stack = []
    w = edgeTo[v]
    stack.append(v)
    while w != s:
        stack.append(w)
        v = w
        w = edgeTo[v]
    stack.append(s)
    return distTo[v],stack[::-1]

def relax(start,end,weight):
    global distTo,edgeTo
    if distTo[end] < distTo[start] + weight:
        distTo[end] = distTo[start] + weight
        edgeTo[end] = start

def depthFirstOrder(graph):
    global postorder, marked, nodes
    ''' set up variables '''
    postorder = []
    marked = {node:False for node in nodes}
    for v in graph.keys():
        if not marked[v]:
            dfs(G,v)

def dfs(graph,v):
    global postorder, marked
    marked[v] = True
    for nodew in graph[v]:
        w = nodew[0]
        if not marked[w]:
            dfs(graph,w)
    postorder.append(v)

if __name__ == '__main__':
    if len(sys.argv)==2:
        filename = sys.argv[1]
        with open(filename) as f:
            lines = f.read().splitlines()
        s = int(lines[0])
        v = int(lines[1])
        G = defaultdict(list)
        for line in lines[2:]:
            nodei = int(line.split("->")[0])
            nodej = int(line.split("->")[1].split(':')[0])
            w = int(line.split("->")[1].split(':')[1])
            G[nodei].append((nodej,w))
    else:
        s = 0
        v = 4
        G = {0:[(1,7),(2,4)],2:[(3,2)],1:[(4,1)],3:[(4,3)]}

    longest, path = acyclicLP(G,s,v)
    print '->'.join(map(str,path))