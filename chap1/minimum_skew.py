#Input: A DNA string Genome.
#Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).
#Minimum Skew Problem now provides us with an approximate location of ori 

sequence = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
#output = [11, 24]

def Minimum_Skew(sequence):
	sklist = [] #list to compare and track
	index = 0 # to iterate
	genomec = 0 
	genomeg = 0
	min_skew = 0
	for i in sequence:
		if i == 'C':
			genomec += 1
		if i == 'G':
			genomeg += 1
		index += 1
		numskew = genomeg-genomec
		#if numbers of skew g-c is less than min_skew, sklist is updated to index to track and min_skew is updated to numskew
		#print (numskew); there were -1 on position 11,24th
		
		if numskew < min_skew:
			sklist = [index]
			min_skew = numskew
		# if numskew == min_skew and index is not in sklist, sklist is updated
		if numskew == min_skew and index not in sklist:
			sklist.append(index)	
	return sklist
print(Minimum_Skew(sequence))

