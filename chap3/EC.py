import sys,random
from re import split
'''
def Adjacent_lists(adjs):
    adj_list = []
    for adj in adjs:
        temp = split(' -> ', adj)
        adj_list[temp[0]] = temp[1].split(',')
    return adj_list

def EulerianCycle(adjlist):
    nodes = list(adjlist.keys())
    eulerianCycle = []

    marked = {} # we need to mark the EDGE
    edges = 0
    for key,val in adjlist.items():
        marked[key] = [False] * len(val)
        edges += len(val)
    # choose any vertex v and push it onto stack
    v = random.choice(nodes)
    # greedily add to cycle, depth-first search style
    stack = []
    stack.append(v)
    # while the stack is not empty
    while len(stack):
        u = stack[-1]
        unmarkedEdges = [i for i,mark in enumerate(marked[u]) if mark == False]
        if len(unmarkedEdges):
            w = adjlist[u][unmarkedEdges[0]]
            marked[u][unmarkedEdges[0]] = True
            stack.append(w)
        else:
            del stack[-1]
            eulerianCycle.append(u)
    return eulerianCycle[::-1]

file = 'dataset_442815_2.txt'
with open(file) as f:
    lines = f.read().splitlines()
    adj_list = Adjacent_lists(lines)
    print("->".join(EulerianCycle(adj_list)))


    adjlist = {}
    for line in lines:
        node = int(line.split(' -> ')[0])
        edge = list(map(int,line.split(' -> ')[1].split(',')))
        adjlist[node] = edge
    print("->".join(EulerianCycle(adjlist)))
    #cycle = EulerianCycle(adjlist)
    #printcycle = ''.join([str(c) + '->' for c in cycle])
    #print(printcycle[:-2])
'''

edges = {0:[3],1:[0],2:[1,6],3:[2],4:[2],5:[4],6:[5,8],7:[9],8:[7],9:[6]}

def eulerian_cycle(edge_dict):
    '''Generates an Eulerian cycle from the given edges.'''
    current_node = edge_dict.keys()[0]
    path = [current_node]

    # Get the initial cycle.
    while True:
        path.append(edge_dict[current_node][0])

        if len(edge_dict[current_node]) == 1:
            del edge_dict[current_node]
        else:
            edge_dict[current_node] = edge_dict[current_node][1:]

        if path[-1] in edge_dict:
            current_node = path[-1]
        else:
            break

    # Continually expand the initial cycle until we're out of edge_dict.
    while len(edge_dict) > 0:
        for i in xrange(len(path)):
            if path[i] in edge_dict:
                current_node = path[i]
                cycle = [current_node]
                while True:
                    cycle.append(edge_dict[current_node][0])

                    if len(edge_dict[current_node]) == 1:
                        del edge_dict[current_node]
                    else:
                        edge_dict[current_node] = edge_dict[current_node][1:]

                    if cycle[-1] in edge_dict:
                        current_node = cycle[-1]
                    else:
                        break

                path = path[:i] + cycle + path[i+1:]
                break
    return path


if __name__ == '__main__':

    # Get the Eulerian cycle.
    path = eulerian_cycle(edges)

    # Print and save the answer.
    print('->'.join(map(str,path)))
