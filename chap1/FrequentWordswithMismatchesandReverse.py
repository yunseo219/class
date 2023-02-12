#Frequent Words with Mismatches and Reverse Complements Problem: Find the most frequent k-mers (with mismatches and reverse complements) in a string.

#Input: A DNA string Text as well as integers k and d.
#Output: All k-mers Pattern maximizing the sum Countd(Text, Pattern)+ Countd(Text, Patternrc) over all possible k-mers.

Text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4 # k-mer length     
d = 1 # num of mismatch
#output: ATGT ACAT OR VARIES

def hamming_distance(seq1,seq2):
    distance = 0
    length = len(seq1)
    for i in range(length):
        if seq1[i] != seq2[i]:
            distance += 1
    return distance

# Flip the sequences 
def ReverseComplement(Pattern):
    revComp = map(complement, Pattern)
    return ('').join(revComp)[::-1]

# Complement of nucleotide
def complement(Nucleotide):
    complements = { 'A': 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}
    comp = complements[Nucleotide.upper()] 
    return comp

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

def frequentWordsWithMismatchesandReverse(text, k, d):
    count_dict = {}
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        neighborhood = neighbors(kmer, d)
        for Pattern in neighborhood:
            if Pattern in count_dict:
                count_dict[Pattern] += 1
            else:
                count_dict[Pattern] = 1
            r_pattern = ReverseComplement(Pattern)
            if r_pattern in count_dict:
                count_dict[r_pattern] += 1
            else:
                count_dict[r_pattern] = 1
    max_freq = max(count_dict.values())
    return [kmer for kmer, count in count_dict.items() if count == max_freq]

print(" ".join(frequentWordsWithMismatchesandReverse(Text, k, d)))
