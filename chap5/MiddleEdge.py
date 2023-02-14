import sys,math

v = 'PLEASANTLY'
w = 'MEASNLY'
'''
Solve the Middle Edge in Linear Space Problem (for protein strings).

Input: Two amino acid strings.
Output: A middle edge in the alignment graph in the form "(i, j) (k, l)", where (i, j) connects to (k, l). To compute scores, use the BLOSUM62 scoring matrix and a (linear) indel penalty equal to 5.

MIDDLENODE(top, bottom, left, right), which returns the coordinate i of the middle node
(i, j) defined by the substrings vtop+1 . . . vbottom and wleft+1 . . . wright. The algorithm also
calls MIDDLEEDGE(top, bottom, left, right), which returns "!" , "#", or "&" depending
on whether the middle edge is horizontal, vertical, or diagonal.

Sample Input:
PLEASANTLY
MEASNLY

Sample Output:
(4, 3) (5, 4)
'''
indelpenalty = 5

def BLOSUM62():
	file = 'BLOSUM62.txt'
	with open(file) as f:
		lines = f.read().splitlines()
	scoring_matrix = []
	readlines = lines[0].split()
	for i in range(1,len(lines)):
		scoring_matrix.append(list(map(int,lines[i][1:].split())))
	return scoring_matrix,readlines
'''
def middle_edge(v,w,indelpenalty =5):
    n = len(v)+1
    matrix,readlines = BLOSUM62()
    middle_col = int(math.floor(len(w)/2.0))
    firstCol = range(0,-indelpenalty*n,-indelpenalty)
    colCount = 1
    while colCount <= middle_col+1:
        nextCol = [None] * n
        nextCol[0] = -indelpenalty * colCount
        for i in range(1,n):
            distDiag = firstCol[i-1] + matrix[readlines.index(v[i-1])][readlines.index(w[colCount-1])]
            distHor = firstCol[i] - indelpenalty
            distVer = nextCol[i-1] - indelpenalty
            candi = [distVer,distHor,distDiag]
            nextCol[i] = max(candi)
        firstCol = nextCol
        if colCount == middle_col:
            middle_rows = [i for i in range(len(nextCol)) if nextCol[i] == max(nextCol)]
            middle_value = max(nextCol)
        colCount += 1
    middle_next = []
    for middle_row in middle_rows:
        if nextCol[middle_row+1] >= nextCol[middle_row]:
            end_i = middle_row+1
            end_j = middle_col+1
        else:
            end_i = middle_row
            end_j = middle_col
        middle_next.append((end_i,end_j))
    return (middle_rows,middle_col,middle_value,middle_next)

'''

def middle_column_score(v, w, scoring_matrix, sigma):
    '''Returns the score of the middle column for the alignment of v and w.'''

    # Initialize the score columns.
    S = [[i*j*sigma for j in range(-1, 1)] for i in range(len(v)+1)]
    S[0][1] = -sigma
    backtrack = [0]*(len(v)+1)

    # Fill in the Score and Backtrack matrices.
    for j in range(1, int(math.floor(len(w)/2.0))+1):
        for i in range(0, len(v)+1):
            if i == 0:
                S[i][1] = -j*sigma
            else:
                scores = [S[i-1][0] + scoring_matrix[v[i-1], w[j-1]], S[i][0] - sigma, S[i-1][1] - sigma]
                S[i][1] = max(scores)
                backtrack[i] = scores.index(S[i][1])

        if j != len(w)/2:
            S = [[row[1]]*2 for row in S]

    return [row[1] for row in S], backtrack


def middle_edge(v, w, scoring_matrix, sigma):
    '''Returns the middle edge in the alignment graph of v and w.'''

    # Get the score of the middle column from the source to the middle.  The backtrack matrix is unnecessary here.
    source_to_middle = middle_column_score(v, w, scoring_matrix, sigma)[0]

    # Get the score of the middle column from the middle to sink.  Reverse the order as the computations are done in the opposite orientation.
    middle_to_sink, backtrack = map(lambda l: l[::-1], middle_column_score(v[::-1], w[::-1]+['', '$'][len(w) % 2 == 1 and len(w) > 1], scoring_matrix, sigma))

    # Get the componentwise sum of the middle column scores.
    scores = map(sum, zip(source_to_middle, middle_to_sink))

    # Get the position of the maximum score and the next node.
    max_middle = max(range(len(scores)), key=lambda i: scores[i])

    if max_middle == len(scores) - 1:
        next_node = (max_middle, len(w)/2 + 1)
    else:
        next_node = [(max_middle + 1, len(w)/2 + 1), (max_middle, len(w)/2 + 1), (max_middle + 1, len(w)/2),][backtrack[max_middle]]

    return (max_middle, len(w)/2), next_node

print(middle_edge(v,w,BLOSUM62(), 5))

