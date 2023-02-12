#The number of mismatches between strings p and q is called the Hamming distance 
#Input: Two strings of equal length.
#Output: The Hamming distance between these strings.

seq1 = "GGGCCGTTGGT"

seq2 = "GGACCGTTGAC"

def hamming_distance(seq1,seq2):
	distance = 0
	length = len(seq1) #length of seq1 and seq are same
	for i in range(length):
		if seq1[i] != seq2[i]:
			distance += 1
	return distance

print(hamming_distance(seq1,seq2))
