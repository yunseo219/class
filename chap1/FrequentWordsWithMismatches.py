#Most frequent k-mer with up to d mismatches in Text is simply a string Pattern maximizing Countd(Text, Pattern) among all k-mers.
#**The number of mismatches between strings p and q is called the Hamming distance
#Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
#Output: All most frequent k-mers with up to d mismatches in Text.

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4 # k-mer length     
d = 1 # num of mismatch
#output: ATGT GATG ATGC OR ATGC ATGT GATG

def hamming_distance(seq1,seq2):
	distance = 0
	length = len(seq1)
	for i in range(length):
		if seq1[i] != seq2[i]:
			distance += 1
	return distance
	
# For a given k-mer substring Pattern of Text, we need to increase 1 to the count of every k-mer that has Hamming distance at most d from Pattern = d-neighborhood of Pattern, i.e Neighbors(Pattern, d).
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
