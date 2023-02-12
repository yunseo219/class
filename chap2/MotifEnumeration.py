#A brute force approach for solving the Implanted Motif Problem is based on the observation that any (k, d)-motif must be at most d mismatches apart from some k-mer appearing in the first string in Dna. Therefore, we can generate all such k-mers and then check which of them are (k, d)-motifs. -> very slow and inefficient
#Runtime: n^t *k *t = very slow

"""
   MotifEnumeration(Dna, k, d)
        Patterns ← an empty set
        for each k-mer Pattern in the first string in Dna
            for each k-mer Pattern’ differing from Pattern by at most d mismatches
                if Pattern' appears in each string from Dna with at most d mismatches
                    add Pattern' to Patterns
        remove duplicates from Patterns
        return Patterns
"""

k = 3
d = 1
Dna = ["ATTTGGC","TGCCTTA", "CGGTATC", "GAAAATT"]
#output: ATT TTT GTT ATA

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

def motifEnumeration(Dna,k,d):
	patterns = []
	motifs = [] #to remove later
	neighborhood = []
	patterns = list(set(patterns))
	for dna in Dna: 
		t = []
		n = []
		for i in range(len(dna)-k+1):
			t.append(dna[i:i+k])
			n += neighbors(dna[i:i+k],d)
		neighborhood.append(t + n)
		patterns = patterns + t
	for pattern in patterns:
		kmers = neighbors(pattern,d)
		for kmer in kmers:
			match = [i for i,dna_kmer in enumerate(neighborhood) if kmer in dna_kmer]
			if len(match) == len(Dna):
				motifs.append(kmer)
	motifs = list(set(motifs)) #remove duplicates
	return motifs
            
print(' '.join(motifEnumeration(Dna,k,d)))
