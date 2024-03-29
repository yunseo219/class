"""
Code Challenge: Solve the Overlap Alignment Problem.

Input: Two strings v and w, each of length at most 1000.
Output: The score of an optimal overlap alignment of v and w, followed by an alignment of a suffix v' of v and a prefix w' of w achieving this maximum score. Use an alignment score in which matches count +1 and both the mismatch and indel penalties are 2.

Sample Input:
PAWHEAE
HEAGAWGHEE

Sample Output:
1
HEAE
HEAG
"""

x = 'GCTATAAGAATAAACCACTAGATCACCTCCGGCTCGCTCACTCCTGATCATGGTTCGTGCTAACATCGCGCCGCGCTGACGCCGAATCGTTCGTAGGAGACAAGTCGACGACCTCATCTACAGGCAAAAGTTAAATTAGCTCTCGGCTAGATGTGACAATCGGAACCCTGCACCCTGCGTAATAGGGTAAATAGTCGGGAGTTGATGCACACACCTAGATATTGGCTGAATGACAGACTGCCATTCCTGCACTGGAAAGTAGAGTGCATATGTTTCGTGAGATTATGCAGGCTCTACGGTTATACTGGGCTCCACGGATTCGACCGGTACTGTTGATTGAAGACTCTTCTATAGAGGCTCTAACCGCGGAGGCCGCAACCAATCGACAATGAAGCACCCGTCGTCGGTATCGTTGGGAAGGACGACACCGTAAGGGCAGACTTTATCGTGACCCGTCTGCTTGCTAGAAAAGCCCTGGCGTTTGTACAACGTCCGTGCAGAATTAGCGTTTTTCTCAGGAAAGATGAGGGGGTTGATCATCATCTCGTTTCGCACGGGTCAAGCGCATTTTCCTACTGTTTTGGACACAGTACGTCTTCCACTGATCTCATACGGACATTACCAGCACCCTTTTGTACCTGTCGTAACTTGTGCCATTCTAGGCCCGTTTTCACTTGCGCTTATGATCATGGTTCCGCTGATCTATATGGGCCGGGTAGGGCACTCCCAGATGAAGGGGAGTAATGGTAGCCGGATCCAAGTGACGCGCCCTAGCGGCTCCGGAGTTTGATAGACGTCGTGCTATGGAGCGTTGGAGCGACAACGCGCTCGTGCTCTGGAAGGTCGCTGCTGATCCGTAA'
y = 'TACTGGTCCTGACCCACCTCACTTTGATGTCCCCTTTTCTCGTTTGCGCATCAAGATCTGGCCCGCAACTATTGGCCGTGAAAGGCACTCATCAATAAAGACAGTACTCACGCGGTCGGATCCAAATGCGCGCACCGAGCGGCCCAGGAGTTGATAGCGTCGAGTAACCTATTAGGACTCGAGGCAACTCGCGCTCTCTCAGGAGGCTCGCCTGCTAGTCCGTGAACGACGGATCTTTGGTGCTGCCTTCCTATCATGACATTGCCTAATAACGAGCGGCACCTACTCCCAGGTCTTTGAAGGGATGGCTTGTTTACCCCGATTCCGAGAAATAGAGATGACTCCTAAGGAAGTAATGAAGGAAGTTCAGTGGTATGGGTATCGTTTAGTTTGCCAGGGAGATTGCCCATAACCTAAGTCCCTAATACAGCAGTAGATCTCACCATAGATGTAGGAAAGCACAGTGATTTAGACGCTTAGCCAAATACAAAGGAATGTACCCCCTCCTAACACTGAGCACCGCTTATTTACTAGTATACTCAGAGTGTGGAGCGCTGAACGTTGTGTCAACAAGAACATAAGCCGCCGTGAATGAATTTGTGAAGGGGAGTGATCATGGTTTTACTCGTGGTAGATTTGGGCAGAACCTGATTCCTCACGTGTGAATGTAATTGAAGCTGACTCCCACACATACAGGCACGATTCTTTTAGATGATGTTTTAGGAAGCGCATTTCGTATTAACACTGCCTTGCATTTGATAACCATCACTTGTTCATTACATGATCCCATAGGGCCGTGTTGTTACTTTCGTGTTAGTCGAGCAGTATGACCACCTTTTCGGCGCTTGATATGCCTCAAGACGTGCGATTCAAGGAATCAAACAAATGAACGCCGCACTGGATGACTGGG'

def OverlapAlignment(x,y,indelpenalty=2):
	mat = [[0 for toj in range(len(y)+1)] for toi in range(len(x)+1)]
	backtrack = [[0 for toj in range(len(y)+1)] for toi in range(len(x)+1)]
	for i in range(len(y)+1,len(x)+1):
		mat[i][0] = mat[i-1][0] - indelpenalty
	for j in range(1,len(y)+1):
		mat[0][j] = 0
	for i in range(1,len(x)+1):
		for j in range(1,len(y)+1):
			distH = mat[i][j-1] +1
			distV = mat[i-1][j] +1
			distD = mat[i-1][j-1] + 1 if x[i-1]==y[j-1] else mat[i-1][j-1] - indelpenalty
			scores = [distH,distV,distD]
			mat[i][j] = max(scores)
			if mat[i][j] == 0: 
				backtrack[i][j] = -1
			elif mat[i][j] == distV:
				backtrack[i][j] = "south" 
			elif mat[i][j] == distH:
				backtrack[i][j] = "east"
			else :
				backtrack[i][j] = "southeast" 

	return mat,backtrack

def Backtrack_max(mat,backtrack,x,y):
	track = [[],[]]
	maxrow = [max(row) for row in mat]
	maxcol = [max(col) for col in mat]
	maxscore = max(maxcol)
	i = maxrow.index(maxscore)
	j = maxcol.index(maxscore)
	while i != 0 and j != 0:
		if backtrack[i][j] == -1:
			break
		elif backtrack[i][j] == "south" :
			track[0].append(x[i-1])
			track[1].append('-')
			i -= 1
		elif backtrack[i][j] == "east": 
			track[0].append('-')
			track[1].append(y[j-1])
			j -=1
		else :
			track[0].append(x[i-1])
			track[1].append(y[j-1])
			i -= 1
			j -= 1

		alignment1 = ''.join(track[0][::-1])
		alignment2 = ''.join(track[1][::-1])
	return maxscore, alignment1, alignment2

if __name__ == '__main__':
	score,backtrack = OverlapAlignment(x,y,indelpenalty=2)
	maxscore,alignment1,alignment2 = Backtrack_max(score,backtrack,x,y)
	print('\n'.join([str(maxscore),alignment1, alignment2])) 
