'''
Input: A string BWT(Text), followed by a collection of Patterns.
Output: A list of integers, where the i-th integer corresponds to the number of substring matches of the i-th member of Patterns in Text.
'''



def BWT_match(BWT, pattern_collection):
    diction = {}
    bwt = []
    for c in BWT:
        diction[c] =  diction.get(c,0) + 1
        tmp = c + str(diction[c])
        bwt.append(tmp)
    x = sorted(bwt, key=lambda x: x[0])
    LastToFirst = [] #y
    for last in bwt:
        for idx, first in enumerate(x,0):
            if first == last:
                LastToFirst.append(idx)
    output = []
    for pattern in pattern_collection:
        output.append(BWMatching(BWT, pattern, LastToFirst))
    return output

'''
    BWMatching(LastColumn, Pattern, LastToFirst)
        top ← 0
        bottom ← |LastColumn| − 1
        while top ≤ bottom
            if Pattern is nonempty
                symbol ← last letter in Pattern
                remove last letter from Pattern
                if positions from top to bottom in LastColumn contain an occurrence of symbol
                    topIndex ← first position of symbol among positions from top to bottom in LastColumn
                    bottomIndex ← last position of symbol among positions from top to bottom in LastColumn
                    top ← LastToFirst(topIndex)
                    bottom ← LastToFirst(bottomIndex)
                else
                    return 0
            else
                return bottom − top + 1
'''


def BWMatching(LastColumn, Pattern, LastToFirst):
    top = 0
    bottom = len(LastColumn) - 1
    while top <= bottom:
        if len(Pattern) != 0:
            symbol = Pattern[-1]
            Pattern = Pattern[:-1]
            topIndex = []
            bottomIndex = []
            for i in range(top, bottom + 1): #if positions from top to bottom in LastColumn contain an occurrence of symbol
                if LastColumn[i] == symbol: 
                    topIndex.append(i)
                    bottomIndex.append(i)
            if len(topIndex) and len(bottomIndex) != 0:
                top = LastToFirst[min(topIndex)]
                bottom = LastToFirst[max(bottomIndex)]
            else:
                return 0
        else:
            return bottom - top + 1


file = 'dataset_442938_8 (1).txt'
with open(file) as f:
    lines = f.read().splitlines()
    BWT = lines[0]
    pattern_collection = lines[1].split()
    match = BWT_match(BWT, pattern_collection)
    print(' '.join(map(str, match)))