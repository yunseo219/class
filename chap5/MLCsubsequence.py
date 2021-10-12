
v = 'AACAGAAG'
w = 'GTTGAATG'
u = 'GCTACAGGGA'

def MultiLC_Subsequence(v, w, u):
    a = len(v)
    b = len(w)
    c = len(u)
    inputv, inputw, inputu = v, w, u
    abc = [[[0 for toc in range(c+1)] for tob in range(b+1)] for toa in range(a+1)]
    backtrack = [[[0 for toc in range(c+1)] for tob in range(b+1)] for toa in range(a+1)]
    for i in range(1, a+1):
        for j in range(1, b+1):
            for k in range(1, c+1):
                scores = [abc[i-1][j][k], abc[i][j-1][k], abc[i][j][k-1], abc[i-1][j][k-1], abc[i-1][j-1][k], abc[i][j-1][k-1], abc[i-1][j-1][k-1] + int(v[i-1] == w[j-1] == u[k-1])]
                backtrack[i][j][k], abc[i][j][k] = max(enumerate(scores), key=lambda l: l[1])
    while i*j*k != 0:
        if backtrack[a][b][c] == 1:
            i -= 1
            inputw = (lambda x, i: x[:i] + '-' + x[i:])(inputw, j) #arg
            inputu = (lambda x, i: x[:i] + '-' + x[i:])(inputu, k)
        elif backtrack[a][b][c] == 2:
            j -= 1
            inputv = (lambda x, i: x[:i] + '-' + x[i:])(inputv, i)
            inputu = (lambda x, i: x[:i] + '-' + x[i:])(inputu, k)
        elif backtrack[a][b][c] == 3:
            k -= 1
            inputv = (lambda x, i: x[:i] + '-' + x[i:])(inputv, i)
            inputw = (lambda x, i: x[:i] + '-' + x[i:])(inputw, j)
        elif backtrack[a][b][c] == 4:
            i -= 1
            j -= 1
            inputu = (lambda x, i: x[:i] + '-' + x[i:])(inputu, k)
        elif backtrack[a][b][c] == 5:
            i -= 1
            k -= 1
            inputw = (lambda x, i: x[:i] + '-' + x[i:])(inputw, j)
        elif backtrack[a][b][c] == 6:
            j -= 1
            k -= 1
            inputv = (lambda x, i: x[:i] + '-' + x[i:])(inputv, i)
        else: #'ijk'
            i -= 1
            j -= 1
            k -= 1
    maxmatch = max(len(inputv),len(inputw),len(inputu))
    while len(inputv) !=  maxmatch:
        inputv = (lambda x, i: x[:i] + '-' + x[i:])(inputv, 0)
    while len(inputw) !=  maxmatch:
        inputw = (lambda x, i: x[:i] + '-' + x[i:])(inputw, 0)
    while len(inputu) !=  maxmatch:
        inputu = (lambda x, i: x[:i] + '-' + x[i:])(inputu, 0)
    return str(abc[a][b][c]), inputv, inputw, inputu

print('\n'.join(MultiLC_Subsequence(v, w, u))) 