def StringSpelledByGappedGenome(gappedpatterns, k, d):
	firstPattern = [pattern.split('|')[0] for pattern in gappedpatterns ]
	secondPattern = [pattern.split('|')[1] for pattern in gappedpatterns ]
	preffixstr = stringSpelledByPatterns(firstPattern,k)
	suffixstr = stringSpelledByPatterns(secondPattern,k)
	combstr = k+d 
	if preffixstr[combstr:] == preffixstr[combstr:]:
		return preffixstr + suffixstr[-(combstr):]

def stringSpelledByPatterns(patterns,k):
	stringPat = [patterns[0]]
	for pattern in patterns[1:]:
		stringPat.append(pattern[-1])
	return ''.join(stringPat)

file = 'dataset_442820_4.txt'
with open(file) as f:
	lines = f.read().splitlines()
	k = int(lines[0].split()[0])
	d = int(lines[0].split()[1])
	gappedpatterns = lines[1:]

print(StringSpelledByGappedGenome(gappedpatterns, k, d))