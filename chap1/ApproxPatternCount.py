#Approx_patterncount: Countd(Text, Pattern) simply requires us to compute the Hamming distance between Pattern and every k-mer substring of Text

#The number of mismatches between strings p and q is called the Hamming distance
#Input: Strings Pattern and Text as well as an integer d.
#Output: 4


pattern = "TTTAGAGCCTTCAGAGG"
text = "GAGG"
d = 2

def hamming_distance(seq1,seq2):
	distance = 0
	length = len(seq1)
	for i in range(length):
		if seq1[i] != seq2[i]:
			distance += 1
	return distance

def approx_patterncount(text,pattern,d):
	count = 0
	for i in range(len(text)-len(pattern)+1):
		if hamming_distance(text[i:i+len(pattern)],pattern) <= d:
			count += 1
	return count

print (approx_patterncount(pattern,text,d))
