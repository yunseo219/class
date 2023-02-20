'''
2-Break Sorting Problem: Find a shortest transformation of one genome into another by 2-breaks.

Input: Two genomes with circular chromosomes on the same set of synteny blocks.
Output: The sequence of genomes resulting from applying a shortest sequence of 2-breaks transforming one genome into the other.

The Breakpoint Theorem guarantees that there must always be a 2-break reducing the number of red-blue cycles in the breakpoint graph by 1. However, it does not tell us how to find such a 2-break. How can this be done? Check out Charging Station: Solving the 2-Break Sorting Problem if you are curious.

Sample Input:
(+1 -2 -3 +4)
(+1 +2 -4 -3)

Sample Output:
(+1 -2 -3 +4)
(+1 -2 -3)(+4)
(+1 -2 -4 -3)
(-3 +1 +2 -4)

Breakpointgraph(P,Q) -> ... -> Breakpointgraph(Q,Q)
Cycle(P,Q) -> ... -> Cycle(Q,Q)=blocks(Q,Q)
#of red-blue cycles increases by blocks(P,Q) - cycle(P,Q)
"""

"""
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




def read_genome(genome_str):
    """
    Parses a genome string and returns a list of blocks.
    """
    return [int(x) for x in genome_str[1:-1].split()]

def write_genome(genome):
    """
    Formats a genome as a string of blocks.
    """
    return '(' + ' '.join(str(x) for x in genome) + ')'

def two_break_on_genome(genome, i, j, k, l):
    """
    Applies a 2-break operation on the given genome by removing the edges (i, i+1) and (j, j+1)
    and adding the edges (i, k) and (j, l) to create two new cycles.
    """
    new_genome = genome[:]
    new_genome[i:i+1] = []
    new_genome[j-1:j] = []
    new_genome[i:i] = [k]
    new_genome[j:j] = [l]
    return new_genome

def two_break_distance(genome1, genome2):
    """
    Computes the 2-break distance between two genomes.
    """
    blocks = set()
    for genome in [genome1, genome2]:
        for block in genome:
            blocks.add(abs(block))
    edges = {i: [] for i in blocks}
    for genome in [genome1, genome2]:
        for i in range(len(genome)):
            block1 = genome[i]
            block2 = genome[(i+1) % len(genome)]
            edges[abs(block1)].append((block1, block2))
    cycles = []
    unexplored_blocks = set(blocks)
    while unexplored_blocks:
        block = unexplored_blocks.pop()
        cycle = [block]
        while True:
            for edge in edges[cycle[-1]]:
                if abs(edge[1]) not in cycle:
                    cycle.append(abs(edge[1]))
                    if edge[1] > 0:
                        cycle[-1] *= -1
                    break
            else:
                break
        cycles.append(cycle)
        unexplored_blocks -= set(map(abs, cycle))
    n = len(blocks)
    adj = [[] for _ in range(2*n)]
    for i in range(2*n):
        adj[i].append((i+n) % (2*n))
        adj[(i+n) % (2*n)].append(i)
    for cycle in cycles:
        for i in range(len(cycle)):
            j = (i+1) % len(cycle)
            adj[cycle[i]+n].append(cycle[j])
            adj[cycle[j]+n].append(cycle[i])
    dist = {i: -1 for i in range(2*n)}
    dist[0] = 0
    q = [0]
    while q:
        u = q.pop(0)
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return (n - dist[n]) // 2

def genome_2_break_distance(genome1_str, genome2_str):
    """
    Computes the sequence of 2-breaks required to transform the first genome into the second.
    """
    genome1 = read_genome(genome1_str)
    genome2 = read_genome(genome2_str)
    blocks = set()
    for genome in [genome1, genome2]:
        for block in genome:
            blocks.add(abs(block))
    edges
    
    
    """
def chromosome_to_cycle(p):
    '''
    CODE CHALLENGE: Implement ChromosomeToCycle.
    Input: A chromosome Chromosome containing n synteny blocks.
    Output: The sequence Nodes of integers between 1 and 2n resulting 
    from applying ChromosomeToCycle to Chromosome.
    '''
    nodes = []
    
    for i in p:
        if (i>0):
            nodes.append(2*i-1)
            nodes.append(2*i)
        else:
            nodes.append(-2*i)
            nodes.append(-2*i-1)
    return nodes

def cycle_to_chromosome(nodes):
    '''
    CODE CHALLENGE: Implement CycleToChromosome.
    Input: A sequence Nodes of integers between 1 and 2n.
    Output: The chromosome Chromosome containing n synteny blocks resulting 
    from applying CycleToChromosome to Nodes.
    '''
    p = []
    for j in range(0,len(nodes)/2):
        if nodes[2*j] < nodes[2*j+1]:
            s = j+1
        else:
            s = -(j+1)
        p.append(s)
    return p


def genome_str_to_list(genome):
    lp = []
    for p in genome.split('(')[1:]:
        p = permutation_str_to_list( '(' + p )
        lp.append(p)
    return lp

def colored_edges(genome):
    '''
    CODE CHALLENGE: Implement ColoredEdges.
    Input: A genome P.
    Output: The collection of colored edges in the genome graph of P 
    in the form (x, y).
    '''
    g = []
    for p in genome:
        s = chromosome_to_cycle(p)
        for j in range(len(s)/2):
            head = 1+2*j
            tail = (2+2*j) % len(s)
            e = (s[head],s[tail])
            g.append(e)
    return g
    
def graph_to_genome(g):
    '''
    CODE CHALLENGE: Implement GraphToGenome.
    Input: The colored edges ColoredEdges of a genome graph.
    Output: The genome P corresponding to this genome graph.
    '''
    
    genome = []
    visit = []
    adj = np.zeros(len(g)*2, dtype = np.int)
    for t in g:
        adj[t[0]-1] = t[1]-1
        adj[t[1]-1] = t[0]-1
    
    for t in g:
        orig = t[0]
        if orig in visit:
            continue
        visit.append(orig)
        if (orig%2 == 0):
            closing = orig-1
        else:
            closing = orig+1
        p = []
        i = 0
        while(True):
            if (orig%2 == 0):
                p.append(orig/2)
            else:
                p.append(-(orig+1)/2)
            dest = adj[orig-1]+1
            i = i + 1
            if (i>100):
                assert False
                return
            visit.append(dest)
            if (dest == closing):
                genome.append(p)
                break
            if (dest%2 == 0):
                orig = dest -1
            else:
                orig = dest + 1
            assert orig > 0
            visit.append(orig)
    return genome
  
def colored_edges_cycles(blue, red):
    '''    
    returns all alternating red-blue-edge cycles
    '''
    cycles = []
    size = len(blue)+len(red) 
    adj = np.zeros(shape = (size,2), dtype = np.int)
    visited = np.zeros(shape = size, dtype = np.bool)
    for e in blue:
        adj[e[0]-1,0] = e[1]-1
        adj[e[1]-1,0] = e[0]-1
    for e in red:
        adj[e[0]-1,1] = e[1]-1
        adj[e[1]-1,1] = e[0]-1
    
    for node in range(size):
        if not visited[node]:
            visited[node] = True
            head = node
            cycle = [head+1]
            # arbitrary we start with a blue edge
            color = 0
            while (True):
                node = adj[node,color]
                if (node == head):
                    # cycle found, we got back to the visited head node, 
                    # just break
                    cycles.append(cycle)
                    break
                cycle.append(node+1)
                visited[node] = True
                color = (color+1) % 2
    return cycles

def two_break_distance(P, Q):
    '''
    CODE CHALLENGE: Solve the 2-Break Distance Problem.
    Input: Genomes P and Q.
    Output: The 2-break distance d(P, Q).
    '''
    blue = colored_edges(P)
    red = colored_edges(Q)

    assert len(blue) == len(red)
    assert len(blue)+len(red) == max([element for tupl in blue+red for element in tupl])
    
    size = len(blue)+len(red) 
    
    l = colored_edges_cycles(blue,red)
    return size/2 - len(l)

def two_break_on_genome_graph(g,i,j,k,l):
    '''
    CODE CHALLENGE: Implement 2-BreakOnGenomeGraph.
    Input: The colored edges of a genome graph GenomeGraph, 
    followed by indices i, j, k, and l.
    Output: The colored edges of the genome graph resulting from applying 
    the 2-break operation 2-BreakOnGenomeGraph(GenomeGraph, i, j, k, l).
    '''
    bg = []
    
    # so do it this way
    rem = ((i,j), (j,i), (k,l), (l,k))
    bg = [ t for t in g if t not in rem]
    bg.append((i,k))
    bg.append((j,l))
    
    return bg

def two_break_on_genome(genome,i,j,k,l):
    '''
    CODE CHALLENGE: Implement 2-BreakOnGenome.
    Input: A genome P, followed by indices i, i', j, and j'.
    Output: The genome P' resulting from applying the 2-break operation
    2-BreakOnGenomeGraph(GenomeGraph, i, i′, j, j′).
    '''
    g = colored_edges(genome)
    g = two_break_on_genome_graph(g,i,j,k,l)
    genome = graph_to_genome(g)
    return genome


def two_break_sorting(P,Q):
    '''
    CODE CHALLENGE: Solve the 2-Break Sorting Problem.     
    2-Break Sorting Problem: Find a shortest transformation 
    of one genome into another via 2-breaks.
    Input: Two genomes with circular chromosomes on the same 
    set of synteny blocks.
    Output: The collection of genomes resulting from applying 
    a shortest sequence of 2-breaks transforming one genome into the other.
    '''
    red = colored_edges(Q)
    path = [P]
    while two_break_distance(P,Q) > 0:
        cycles = colored_edges_cycles(colored_edges(P),red)
        for c in cycles:
            if len(c) >= 4:
                P = two_break_on_genome(P,c[0],c[1],c[3],c[2])
                path.append(P)
                break          
    return path

print([two_break_distance(p,[[1, 2, -4, -3]]) for p in two_break_sorting([[1, -2, -3, 4]],[[1, 2, -4, -3]])] == range(4)[::-1])
    """
