#k-mer Pattern appears as a substring of Text with at most d mismatches if there is some k-mer substring Pattern' of Text having d or fewer mismatches with Pattern, i.e., HammingDistance(Pattern, Pattern') ≤ d. 
#**The number of mismatches between strings p and q is called the Hamming distance
#Input: Strings Pattern and Text along with an integer d.
#Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

pattern = "ATTCTGGA"
text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
d = 3

def hamming_distance(seq1,seq2):
	distance = 0
	length = len(seq1)
	for i in range(length):
		if seq1[i] != seq2[i]:
			distance += 1
	return distance

def approx_patternmatch(pattern,text,d):
	count = []
	for i in range(len(text)-len(pattern)+1): 
		if hamming_distance(text[i:i+len(pattern)],pattern) <= d:
			count.append(i)
	return count

count = approx_patternmatch(pattern,text,d)
print (' '.join(map(str,count)))
# 6 7 26 27
# [6, 7, 26, 27] without print (' '.join(map(str,count)))
