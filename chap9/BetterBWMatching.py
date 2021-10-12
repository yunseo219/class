
def BWT_match(BWT, pattern_list):
    FirstOccurrence = {}
    bwt = []
    for bwt, symbol in enumerate(sorted(BWT),0):
        if symbol not in FirstOccurrence:
            FirstOccurrence[symbol] = bwt  
    output = []
    for pattern in pattern_collection:
        output.append(BetterBWMatching(FirstOccurrence, BWT, pattern))
    return output


def Countsymbol(bwt, LastColumn,symbol):
    LastColumn = LastColumn[:bwt]
    count = LastColumn.count(symbol)
    return count


def BetterBWMatching(FirstOccurrence, LastColumn, pattern):
	Countsymbol = {}
	top = 0
	bottom = len(LastColumn) - 1
	while top <= bottom:
		if len(pattern) != 0:
			symbol = pattern[-1]
			pattern = pattern[:-1]
            #topIndex = []
            #bottomIndex = []
			if symbol in LastColumn[top:bottom + 1]:
				top = FirstOccurrence[symbol] + Countsymbol(top, LastColumn,symbol)
				bottom = FirstOccurrence[symbol] + Countsymbol(bottom + 1, LastColumn,symbol) - 1
			else:	
				return 0
		else:
			return bottom - top + 1


file = 'dataset_442939_7 (2).txt'
with open(file) as f:
    lines = f.read().splitlines()
    BWT = lines[0]
    pattern_list = lines[1].split()
    print(' '.join(str(x) for x in BWT_match(BWT, pattern_collection)))
