x ='GTAGGCTTAAGGTTA'
y = 'TAGATA'

def FittingAlignment(x,y,indelpenalty=1):
	s = [[0 for toj in range(len(y)+1)] for toi in range(len(x)+1)]
	backtrack = [[0 for toj in range(len(y)+1)] for toi in range(len(x)+1)]
	s[0][0] =0
	for i in range(1,len(x)+1): #first column
		s[i][0] = i
	for j in range(1,len(y)+1):
		s[0][j] = j
	for i in range(1,len(x)+1):
		for j in range(1,len(y)+1):
			deletion = s[i-1][j] 
			insertion = s[i][j-1] 
			match = s[i-1][j-1] +1 if x[i-1]==y[j-1] else s[i-1][j-1]
			s[i][j] = max(s[i-1][j], s[i][j-1],  s[i-1][j-1]+ 1 if x[i-1]==y[j-1] else s[i-1][j-1])
			if s[i][j] == deletion:
				backtrack[i][j] = "south" 
			elif s[i][j] == insertion :
				backtrack[i][j] = "east"
			else : #mis/match
				backtrack[i][j] = "southeast" 
	return s[len(x)][len(y)]

def Backtrack_max(s,backtrack,x,y):
	track = [[],[]]
	lastDCol = zip(*s)[-1]
	lastPointCol = zip(*backtrack)[-1]
	indexdiag = [k for k in range(len(lastDCol)) if lastPointCol[k]==3 and k > len(y)]
	lastCol = [lastDCol[ind] for ind in indexdiag]
	i = indexdiag[lastCol.index(max(lastCol))]
	j = len(y)
	score = mat[i][j]
	while i != 0 and j!=0:
		if backtrack[i][j] == "southeast" :
			track[0].append(x[i-1])
			track[1].append(y[j-1])
			i -= 1
			j -= 1
		elif backtrack[i][j]== "east":
			track[0].append(x[i-1])
			track[1].append('-')
			i -= 1
		else:
			track[0].append('-')
			track[1].append(y[j-1])
			j -=1
	alignment1 = ''.join(track[0][::-1])
	alignment2 = ''.join(track[1][::-1])

	return score,alignment1,alignment2


if __name__ == '__main__':
	score,backtrack = FittingAlignment(x,y,indelpenalty=1)
	score,alignment1,alignment2 = Backtrack_max(score,backtrack,x,y)
	print('\n'.join([str(score),alignment1, alignment2]))

