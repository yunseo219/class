P = '(+1 +2 +3 +4 +5 +6)'
Q = '(+1 -3 -6 -5)(+2 -4)'


def two_break_distance(P, Q):
    p = colored_edges(P)
    q = colored_edges(Q)
    comb = p + q
    n_cycle = 0
    while len(comb) != 0:
        n_cycle = n_cycle + 1
        current_cycle = comb[0]
        comb.pop(0)
        for number in current_cycle:
            for edge in comb:
                if number in edge:
                    edge.remove(number)
                    current_cycle.extend(edge)
                    comb.remove(edge)
    return(len(q) - n_cycle)

def ChromosomeToCycle(Chromosome):
    Nodes = []
    for i in Chromosome:
        if i > 0:
            Nodes.append(2 * i- 1)
            Nodes.append(2 * i)
        else:
            Nodes.append(-2 * i)
            Nodes.append(-2 * i - 1)
    return Nodes

def colored_edges(P):
    Edges = list()
    for chromosome in P:
        Nodes = ChromosomeToCycle(chromosome)
        for j in range(1, abs(len(Nodes)), 2):
            if j != len(Nodes) - 1:
                Edges.append([Nodes[j], Nodes[j + 1]])
            else:
                Edges.append([Nodes[j], Nodes[0]])
    return Edges


if __name__ == '__main__':
    #P, Q = [line.strip().lstrip('(').rstrip(')').split(')(') for line in input_data.readlines()]
    P = [list(map(int, block.split())) for block in P]
    Q = [list(map(int, block.split())) for block in Q]

    # Get the 2-Break Distance.
    dist = two_break_distance(P, Q)

    # Print and save the answer.
    print(str(dist))