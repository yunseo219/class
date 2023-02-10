pattern = "ATAT"
sequence = "GATATATGCATATACTT"
#expected output 1,3,9

DNAseq = str(sequence.upper())
patternseq = str(pattern.upper())
k = len(patternseq)
output = list()
#Output: A collection of space-separated integers specifying all starting positions where Pattern appears as a substring of Genome.
for i in range(0, len(DNAseq) - k + 1): 
	psubstr = DNAseq[i:i + k] 
	if psubstr == patternseq:#compare
		output.append(str(i)) 
print(' '.join(output))
