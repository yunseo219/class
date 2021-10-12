text = "TCGGTCGGATGACGACGATGCTCGGTGCATGATGCTCGGCGACGACGACGATGCATGAATGATGCTGCTCGGATTTGCATTTCGGTGCATGACGAATTTGCTCGGATGACGATGCTCGGATGATCGGTCGGATTTCGGATGAATTATTCGACGAATTATGACGATGCATTTGCTCGGCGATCGGTCGGATGAATGACGATGCCGAATGAATTCGATCGGCGATCGGTCGGATTCGAATTATGAATGATCGGATGACGATGCCGAATGAATTTCGGTGCATGACGAATGAATTATGAATTTCGGATTTGCTGCCGAATGACGACGACGAATGAATTCGAATGAATTATGACGAATGACGAATTCGACGATGC"
k = 6
d = 2


def hamming_distance(seq1,seq2):
	distance = 0
	length = len(seq1)
	for i in range(length):
		if seq1[i] != seq2[i]:
			distance += 1
	return distance

def neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for suffix in suffix_neighbors:
        if hamming_distance(pattern[1:], suffix) < d:
            for nuc in ['A', 'C', 'G', 'T']:
                neighborhood.add(nuc + suffix)
        else:
            neighborhood.add(pattern[0] + suffix)
    return neighborhood


def frequentWordsWithMismatches(text,k,d):
    count_dict = {}
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        neighborhood = neighbors(kmer, d)
        for approx_pattern in neighborhood:
            if approx_pattern in count_dict:
                count_dict[approx_pattern] += 1
            else:
                count_dict[approx_pattern] = 1
    max_freq = max(count_dict.values())
    return [kmer for kmer, count in count_dict.items() if count == max_freq]

print(' '.join(frequentWordsWithMismatches(text,k,d)))

#runs online