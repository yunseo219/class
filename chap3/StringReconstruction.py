
def StringReconstruction(pattern):
    string = pattern[0]
    for i in range(1, len(pattern)):
        string += pattern[i][-1]
    return string

file = 'dataset_442810_3 (7).txt'
with open(file) as f:
	pattern = f.read().splitlines()
	
print(StringReconstruction(pattern))