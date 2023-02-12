#For example, to generate Neighbors(CAA,1), first form Neighbors(AA,1) = {AA, CA, GA, TA, AC, AG, AT}. 
pattern = "ACG"
d = 1
#Input: A string Pattern and an integer d.
#Output: The collection of strings Neighbors(Pattern, d).
#output: TCG CCG ACG GCG ATG AAG ACA AGG ACC ACT

def hamming_distance(seq1,seq2):
	distance = 0
	length = len(seq1)
	for i in range(length):
		if seq1[i] != seq2[i]:
			distance += 1
	return distance

def neighbors(pattern,d):
	if d == 0:
		return pattern
	if len(pattern) == 1:
		return ['A','C','G','T'] #nucleotide pattern
	neighborhood = [] #empty set
	suffixneigh = neighbors(pattern[1:],d)
	for text in suffixneigh:
		if hamming_distance(pattern[1:],text) < d:
			for nucleotide in ['A','C','G','T']:
				neighborhood.append(nucleotide+text)
		else: #add first symbol
			neighborhood.append(pattern[:1]+text)
	neighborhood = list(set(neighborhood))
	return neighborhood
print (' '.join (neighbors(pattern,d)))
