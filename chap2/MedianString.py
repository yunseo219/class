# Find a k-mer Pattern that minimizes d(Pattern, Dna); aka minimum hamming distance, where this function is itself computed by taking a minimum over all choices of k-mers from each string in Dna. 
#Runtime: 4^k*n*t*k => faster than bruteforce but can be better

#Input: An integer k, followed by a collection of strings Dna.
#Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all possible choices of k-mers. (If there are multiple such strings Pattern, then you may return any one.)
"""
   MedianString(Dna, k)
       distance ← ∞
       for each k-mer Pattern from AA…AA to TT…TT
           if distance > d(Pattern, Dna)
                distance ← d(Pattern, Dna)
                Median ← Pattern
       return Median
"""

k = 6
dna = ["CTAGTGTCCCACTGATAGTGAGGATTAGCCTGTCCGACACGC",
"GAGATCTGACCGACATTTGCTGAAACCCTGCTAACCACGAAG",
"CCCGCGTGAAACAATTTGTTAGAAGGCGAATGTCCGCTCGGT",
"TTGCCCTGCCCGGAGAGTCGGGGATGCCCCGAGTTCTGCGTG",
"AGTCACCTTTCGACACTGTGACCGAATGCCCTGGTGGCCGCG",
"AGACCGACGTAATCAATCGAACGCGTTCCGTTAACATGGCCG",
"TCCAGACGTAAATGGCCGACCTGGCGGCGACATCACGGCCGG",
"CCGCGTTTTAGGTGTCCGTAGGAATCTCGTACCTTCAATTTC",
"CATGAACCTGACGTCCCGCCTATTCGGTTCGGCCACTGTCCG",
"CTACCTTGGCCGCCGACTCTTTATATCTCGAACACGGCGGCG"]
#output: 

def hamming_distance(seq1,seq2):
    distance = 0
    length = len(seq1)
    for i in range(length):
        if seq1[i] != seq2[i]:
            distance += 1
    return distance

def DistanceBetweenPatternAndStrings(pattern, dna):
    distance = 0
    for seq in dna: 
        Hamdist = float('inf') #hammingdist
        for i in range(len(seq) - len(pattern) +1):
            if Hamdist > hamming_distance(pattern, seq[i:i+len(pattern)]):
                Hamdist = hamming_distance(pattern, seq[i:i+len(pattern)])
        distance += Hamdist
    return distance

def NumberToPattern(index,k):
    if k == 1:
        return NumberToSymbol(index)
    prefixid = index/4
    j = index%4
    symbol = NumberToSymbol(j)
    prefixPattern = NumberToPattern(prefixid, k-1)
    return prefixPattern + symbol
    
def NumberToSymbol(number):
    mapping = {'A':0,'C':1,'G':2,'T':3}
    invertmap = {val:key for key, val in mapping.items()} #invertback
    return invertmap[number]

def MedianString(dna, k):
    distance = float('inf')
    for i in range(4**k): #for each kmer pattern
        pattern = NumberToPattern(i, k) 
        if distance > DistanceBetweenPatternAndStrings(pattern, dna):
            distance = DistanceBetweenPatternAndStrings(pattern, dna)
            median = []
            median.append(pattern)
    return median
            
print(" ".join(MedianString(dna, k)))

#not running; check answers
