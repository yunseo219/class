k = 12
Text = "TACTGATCCGTCTGGACCGCATAGCATCCATAGGGTCTGGACCGCATAGCTATAGTAGTTATCCATAGGTACTGATCCTATAGTAGTTCGCATAGCGTCTGGACATCCATAGGTACTGATCCCGCATAGCTACTGATCCATCCATAGGGTCTGGACTACTGATCCCGCATAGCTACTGATCCGTCTGGACGTCTGGACGTCTGGACATCCATAGGGTCTGGACTACTGATCCCGCATAGCCGCATAGCTATAGTAGTTCGCATAGCATCCATAGGATCCATAGGATCCATAGGTACTGATCCATCCATAGGATCCATAGGTATAGTAGTTTACTGATCCTACTGATCCCGCATAGCTACTGATCCTACTGATCCCGCATAGCTACTGATCCATCCATAGGCGCATAGCGTCTGGACCGCATAGCTATAGTAGTTCGCATAGCCGCATAGCCGCATAGCTATAGTAGTTATCCATAGGTACTGATCCTACTGATCCATCCATAGGTACTGATCCATCCATAGGTATAGTAGTTTACTGATCCATCCATAGGTATAGTAGTTCGCATAGCTACTGATCCTATAGTAGTTATCCATAGGGTCTGGACCGCATAGCTATAGTAGTTCGCATAGCTACTGATCCTATAGTAGTTTATAGTAGTTTATAGTAGTTGTCTGGACTATAGTAGTTTATAGTAGTTGTCTGGACTACTGATCCTACTGATCCTATAGTAGTTTATAGTAGTTTACTGATCCTACTGATCCTATAGTAGTTGTCTGGACTATAGTAGTTTACTGATCCCGCATAGCTATAGTAGTTATCCATAGGATCCATAGGGTCTGGACGTCTGGACGTCTGGACATCCATAGGGTCTGGACCGCATAGCTACTGATCCATCCATAGG"

def PatternCount(Pattern, Text):
    count = 0 #start with 0 
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

# k-mer Pattern appears in position 0 of Text, position 1 of Text, and so on. so k-mer pattern is |Text| − k + 1 

def FrequentWordsProblem(Text, k):
    FrequentPatterns = [] #empty set 
    Count = {}
    for i in range(len(Text)-k+1): 
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    maxC = max(Count.values())
    for i in Count:
        if Count[i] == maxC:
            FrequentPatterns.append(Text[i:i+k])
    FPNoDup = remove_duplicates(FrequentPatterns) #add nondups
    return FPNoDup 

def remove_duplicates(Text):
    NoDuplicates = [] #empty = no item dup
    for item in Text: 
        if item not in NoDuplicates:
            NoDuplicates.append(item) #add
    return NoDuplicates

print (" ".join(FrequentWordsProblem(Text, k)))

#in chap 1 we are looking for dna boxes so clump finding matters
