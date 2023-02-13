#String Composition Problem: Generate the k-mer composition of a string.

#Input: An integer k and a string Text.
#Output: Compositionk(Text), where the k-mers are arranged in lexicographic order.

#k = 5
#Text = CAATCCAAC
#output = CAATC AATCC ATCCA TCCAA CCAAC

def StringReconstruction(pattern):
    string = pattern[0]
    for i in range(1, len(pattern)):
        string += pattern[i][-1]
    return string

file = 'dataset_442810_3 (7).txt'
with open(file) as f:
	pattern = f.read().splitlines()
	
print(StringReconstruction(pattern))
