"""
Implement LinearSpaceAlignment to solve the Global Alignment Problem for a large dataset.

Input: Two long (10000 amino acid) protein strings written in the single-letter amino acid alphabet.
Output: The maximum alignment score of these strings, followed by an alignment achieving this maximum score. Use the BLOSUM62 scoring matrix and indel penalty σ = 5.

Sample Input:
PLEASANTLY
MEANLY

Sample Output:
8
PLEASANTLY
-MEA--N-LY
"""

str1 = 'PLEASANTLY'
str2 = 'MEANLY'
indelpenalty = 5

import sys,math

def BLOSUM62():
    file = 'BLOSUM62.txt'
    with open(file) as f:
        lines = f.read().splitlines()
    matrix = []
    readlines = lines[0].split()
    for i in range(1,len(lines)):
        matrix.append(list(map(int,lines[i][1:].split())))
    return matrix,readlines

def middle_node(v,w,indelpenalty =5):
    '''FromSource(i)'''
    #from column 0 to collumn middle
    (midNode_i,midNode_j,fromSource) = from_source(v,w,indel)
    ''' ToSink(i) '''
    v_rev = v[::-1]
    w_rev = w[::-1]
    (toSink,toSinkMax,) = to_sink(v_rev,w_rev,indel,midNode_j,midNode_i)
    length = fromSource + toSink

def middle_edge(v,w,indelpenalty =5):
    n = len(v)+1
    matrix,readlines = BLOSUM62()
    middle_col = int(math.floor(len(w)/2.0))
    firstCol = range(0,-indelpenalty*n,-indelpenalty)
    colCount = 1
    while colCount <= middle_col+1:
        nextCol = [None] * n
        nextCol[0] = -indel * colCount
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

def middle_edge(top,bottom,left,right):
    matrix,readlines = BLOSUM62()
    middle_col = int(math.floor((left+right)/2.0))

    firstCol = range(0,-indel*n,-indelpenalty)
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
            middle_row = max([i for i in range(len(nextCol)) if nextCol[i] == max(nextCol)])
        colCount += 1
    for middle_row in middle_rows:
        if nextCol[middle_row+1] >= nextCol[middle_row]:
            middle_edge = 1
        else:
            middle_edge = 2
    return middle_row,middle_edge

def to_sink(v,w, indelpenalty,middle,i):
    n = len(v)
    m = len(w)
    matrix,readlines = BLOSUM62()
    middle_rev = m - middle
    i_rev = n - i
    firstCol = range(0,-indelpenalty*n,-indel)
    colCount = 1
    while colCount <= middle_rev:
        nextCol = [None] * n
        nextCol[0] = -indelpenalty * colCount
        for i in range(1,n):
            distDiag = firstCol[i-1] + matrix[readlines.index(v[i-1])][readlines.index(w[colCount-1])]
            distHor = firstCol[i] - indelpenalty
            distVer = nextCol[i-1] - indelpenalty
            candi = [distVer,distHor,distDiag]
            nextCol[i] = max(candi)
            direction = candi.index(nextCol[i])
        firstCol = nextCol
        colCount += 1
    middle_row = nextCol.index(max(nextCol))
    return (nextCol[i_rev],max(nextCol))

def from_source(v,w,indelpenalty):
    n = len(v)+1
    matrix,readlines = BLOSUM62()
    middle = int(math.floor(len(w)/2.0))
    firstCol = range(0,-indelpenalty*n,-indel)
    colCount = 1
    while colCount <= middle:
        nextCol = [None] * n
        nextCol[0] = -indel * colCount
        for i in range(1,n):
            distDiag = firstCol[i-1] + matrix[readlines.index(v[i-1])][readlines.index(w[colCount-1])]
            distHor = firstCol[i] - indelpenalty
            distVer = nextCol[i-1] - indelpenalty
            candi = [distVer,distHor,distDiag]
            nextCol[i] = max(candi)
        firstCol = nextCol
        colCount += 1
    middle_row = max([i for i in range(len(nextCol)) if nextCol[i] == max(nextCol)])
    return (middle_row,middle,max(nextCol))

def linear_space_alignment(top,bottom,left,right):
    if left == right:
        return ['-']*len(top-bottom)
    if top == bottom:
        return ['-']*len(right-left)
    middle_node_j = int(math.floor((left+right)/2.0))
    middle_node_i,middle_edge = middle_edge(top,bottom,left,right)
    linear_space_alignment(v,w,top,middle_node_i,left,middle_node_j)
    middle_node_j += 1
    if middle_edge == 1:
        middle_node_i += 1
    linear_space_alignment(middle_node_i,bottom,middle_node_j,right)


    score,backtrack = LinearSpaceAlignment(v,w,top,middle_node_i,left,middle_node_j)
    alignment1,alignment2 = Backtrack_edge(backtrack,str1,str2)
    print('\n'.join([str(score),alignment1,alignment2]))
