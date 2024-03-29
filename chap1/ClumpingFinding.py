genome = "TTAATTCCTCATGGGTCTCGGCATCAGATGCTGGGGTAATAGGAGACACTCGTACTCGTTCGTGATAAATGCACGATAAATGTCCGAAGAGGGAGTGGACCAGCAATGGTATCCTCGCAGTAATTAAATTCCCTATGTGTCGATGAACGGCGCAGACGCAGATAACACAACATAACGGTAACAAGCAAGTCCGTTAATACGTCCGAGGTATGACAAAAATGCTGCAACGAAGTCGTCGTCAATTTCGTCAATTGTCAATTATACCCATCGACGTCTGAGCCGAGCCTCACGGTCGAGACCGAGCCACGTAGGAGAGGCGCTTGACGCGCCAACGCGGCGCCATCACCCGACGTAATTCGTGAGTTGGCCTCCCGGATTGTTCTCAGTGTCGCACGATATGGTTGTGGTCCAGCCGTTAGAGCATGTTGTTCACAAGTGACTGGCAATCGACGTGGTTGCAATCGCGGGATCGCCCGATGCTTGGAATACTTCTGATCGGTTCATACCAGAACGGCTAGATTCGGATACCAGATGTGCACTGTGGAAGAACTAATTCGTAAGGTGCCTCGTTTGTCTTTCCTAGATAATATATGTCGAATCTAATGTTTGTCCTTTACGAGTGTCTAGAATGCCCGTGAGGCAGCCACCAAGGATACCAAGGATATTACATAAACACGCTACGACAATCCTCTTCGATCACCCTGATTACCTACTTGTCGTAGACCTGGTACTTGCGCCGCCAACCTGGTTAGCGACAGATTCGTGCTCTAATCAACGCAAACGCAGCACGCAGGCCGTCATCTTATGCGTACGCAGAAGGGCTTGCATACCAAAGCATACACGTTTCGCAGGCACGCTATCACAGTTTGTGGATGCCGCTGGGCAACGGTGAACAACGCATTAGTAGTTCCCAGTACCAAAAAATCGACCATAGCCTGGCTCCACTAAAGTCTCTCGGCTAGATAATCAGAATCTCAGAATCAGAAATCTCTATACTTCCGGCTACCGTGGGTACCAAGTCTGATAGGTACGAATCATTCTAAGACCGAGTTCCTTCGGCGGGCCGGAAGCGAGGCGATATCTCCGTTCTTTTCGCGCAGAACGCAGATTCGGACGGCGGGTGGATCCTTAGTACACCATTTGATCTAAATACCGTTCATGGTGCGGATATTTTGCCTTATCGTGTCGTGTCGTGTCCCTGTGTCCCTCAGTTATTACGTCTAAGTCGTTGGTAGAGAACACTGTAACGGACCTCGACTGTTGCGGCCTCAGTGATATATGTTCCTGACCGATAGGTGCGCCCTTGGAATATATATGAATATTATTTATTGGCGGACTATCCCCGTACATAAGGATGTCTGAGCACATTTATCACTGCACTATTAGGTTATTGCTTTATGCCAGGTATCTTGGTTCCCCGCAGCTCCAGCAACATGTGTACCCTATATTGCCTTCGATTGTTAGAGTGAGCCACCAGGAGCCACATACGAAGTATCCCCCACGATAGAGTCATGCTCCTAAGAATACCCCACATGACGCATAGCCTTTGAGAGTGTTGGGCGTTAGGCGGCCTTACGAATTCAGAGCCAACTTACGAGCACTCTCCGCTAAGTGACACAATGCCTTCGAGAACACGTCCTTTGACCCGTGTCGGCTACCAGGGTAGGGAAAATTCATCTCAAGCGCGATTATTACAACCCAACGCCCCAGAGTCATAGACCAGGCGGAGGAGTCATAGAGGAACAAGTACCATTAACCAATGGCTGTCGGCTGGTGGAGGCCCTGTGCGACTTACGATGAGGTCACCAATGCTACAGAGATTCTGTACCTTCTCTTCCAAGACTACATCGGCTCGTGTTCACTCACTATATTCACTATATTT"
k = 10
L = 29
t = 3

"""
Background knowledge
k-mer as a "clump" if it appears many times within a short interval of the genome; 
if there is an interval of Genome of length L in which this k-mer appears at least t times.
given integers L and t, a k-mer Pattern forms an (L, t)-clump

Sample Input:
CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA
5 50 4

Sample Output:
CGACA GAAGA
"""

#Input: A string Genome, and integers k, L, and t.
#Output: All distinct k-mers forming (L, t)-clumps in Genome.


def clumpfinding(genome,k,t,L):
    frequentPatterns = [] #empty set
    for i in range(len(genome) - L + 1):
        clump = [0] * (4**k)
        text = genome[i:i+L]
        frequencyArray = freqArray.computeFreq(text,k)
        for i in range(4**k):
            if frequencyArray[i] >= t:
                clump[i] = 1
    for i in range(4**k):
        if clump[i] == 1:
            freqPatterns.append(freqArray.NumberToPattern(i,k))
    return freqPatterns
    
def computeFreq(text,k):
    frequencyArray = [0] * (4**k)
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        j = PatternToNumber(pattern)
        frequencyArray[j] += 1
    return frequencyArray

def PatternToNumber(pattern):
    if len(pattern) == 0 :
        return 0
    symbol = pattern[-1]
    prefix = pattern[:-1]
    return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)
    
def NumberToPattern(index,k):
    if k == 1:
        return NumberToSymbol(index)
    prefixid = index/4
    j = index%4
    symbol = NumberToSymbol(j)
    prefixPattern = NumberToPattern(prefixid, k-1)
    return prefixPattern + symbol

def SymbolToNumber(symbol):
    mapping = {'A':0,'C':1,'G':2,'T':3}
    return mapping[symbol]

def NumberToSymbol(number):
    mapping = {'A':0,'C':1,'G':2,'T':3}
    invertmap = {val:key for key, val in mapping.items()} #invertback
    return invertmap[number]

    Fpatterns = clumpfinding(genome,k,t,L)
    print ' '.join(Fpatterns)
    
    
sequence = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"

k = 5 # k-mer length
L = 50 # genome length
t = 4 #k-mer appearance


"""
Background knowledge
k-mer as a "clump" if it appears many times within a short interval of the genome; 
if there is an interval of Genome of length L in which this k-mer appears at least t times.
given integers L and t, a k-mer Pattern forms an (L, t)-clump

Sample Input:
CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA
5 50 4

Sample Output:
CGACA GAAGA
"""

DNA = str(sequence.upper())

# Create new dic called counts to counts all the kmer
counts = {}
for i in range(0, len(DNA) - k + 1):
	kmer = DNA[i:i + k]
	if kmer in counts:
		counts[kmer] += 1
	else:
		counts[kmer] = 1
		
# Eliminate all pairs that appear less than t times; new dict called frequent
frequent = {}
for k in counts:
	if counts[k] >= t:
		frequent[k] = counts[k]
output = ' '.join(frequent.keys())
print(output)

