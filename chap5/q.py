v = 'PLEASANTLY'
w = 'MEASNLY'
indel_pentalty = 5

def BLOSUM62():
    file = 'BLOSUM62.txt'
    with open(file) as f:
        lines = f.read().splitlines()
    smatrix = []
    readlines = lines[0].split()
    for i in range(1,len(lines)):
        smatrix.append(list(map(int,lines[i][1:].split())))
    return smatrix,readlines

def middle_column_score(v, w, smatrix, sigma):
    '''Returns the score of the middle column for the alignment of v and w.'''
    # Initialize the score columns.
    S = [[i*j*sigma for j in range(-1, 1)] for i in range(len(v)+1)]
    S[0][1] = -sigma
    backtrack = [0]*(len(v)+1)

    # Fill in the Score and Backtrack matrices.
    for j in range(1, len(w)//2+1):
        for i in range(0, len(v)+1):
            if i == 0:
                S[i][1] = -j*sigma
            else:
                scores = [S[i-1][0] + smatrix[v[i-1], w[j-1]], S[i][0] - sigma, S[i-1][1] - sigma]
                S[i][1] = max(scores)
                backtrack[i] = scores.index(S[i][1])
        if j != len(w)//2:
            S = [[row[1]]*2 for row in S]

    return [row[1] for row in S], backtrack


def middle_edge(v, w, smatrix, sigma):
    '''Returns the middle edge in the alignment graph of v and w.'''

    # Get the score of the middle column from the source to the middle.  The backtrack matrix is unnecessary here.
    source_to_middle = middle_column_score(v, w, smatrix, sigma)[0]

    # Get the score of the middle column from the middle to sink.  Reverse the order as the computations are done in the opposite orientation.
    middle_to_sink, backtrack = map(lambda l: l[::-1], middle_column_score(v[::-1], w[::-1]+['', '$'][len(w) % 2 == 1 and len(w) > 1], smatrix, sigma))

    # Get the componentwise sum of the middle column scores.
    scores = map(sum, zip(source_to_middle, middle_to_sink))

    # Get the position of the maximum score and the next node.
    max_middle = max(range(len(scores)), key=lambda i: scores[i])

    if max_middle == len(scores) - 1:
        next_node = (max_middle, len(w)//2 + 1)
    else:
        next_node = [(max_middle + 1, len(w)//2 + 1), (max_middle, len(w)//2 + 1), (max_middle + 1, len(w)//2),][backtrack[max_middle]]

    return (max_middle, len(w)//2), next_node

    # Get the middle edge.
middle = middle_edge(v, w, BLOSUM62(), 5)

    # Print and save the answer.
print (' '.join(map(str, middle)))