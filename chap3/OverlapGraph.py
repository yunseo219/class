#Input: A collection Patterns of k-mers.
#Output: The overlap graph Overlap(Patterns), in the form of an adjacency list. 

def OverlapGraph(patterns):
    adj = [] #using adjacent list
    for i in range(len(patterns) - 1):
        for j in range(i, len(patterns)):
            if patterns[i][1:] == patterns[j][:-1]:
                adj.append((patterns[i], patterns[j]))
            if patterns[j][1:] == patterns[i][:-1]:
                adj.append((patterns[j], patterns[i]))
    return adj

file = 'dataset_442810_3.txt'   
with open(file) as f:
	Patterns = f.read().splitlines()
	adj = OverlapGraph(Patterns)	
	for lines in adj:
		print(" -> ".join(lines))