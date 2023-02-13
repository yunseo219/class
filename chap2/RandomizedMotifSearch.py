#we can begin from a collection of randomly chosen k-mers Motifs in Dna, construct Profile(Motifs), and use this profile to generate a new collection of k-mers: Motifs(Profile(Motifs), Dna). 
# and hope that Motifs(Profile(Motifs), Dna) has a better score than the original collection of k-mers Motifs.

#Input: Integers k and t, followed by a collection of strings Dna.
#Output: A collection BestMotifs resulting from running RandomizedMotifSearch(Dna, k, t) 1,000 times. Remember to use pseudocounts!

"""
    RandomizedMotifSearch(Dna, k, t)
        randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
        BestMotifs ← Motifs
        while forever
            Profile ← Profile(Motifs)
            Motifs ← Motifs(Profile, Dna)
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
            else
                return BestMotifs
"""

k = 8
t = 5
N = 1000 
dnas = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT', 'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']

from random import randint

def randomizedMotifSearch(dnas,k,t):
    motifs = []
    for dna in dnas:
        istart = randint(0,len(dna)-k)
        motifs.append(dna[istart:istart+k])
    bestMotifs = motifs
    while True:
        profile = profileMatrixPesudocounts(motifs)
        motifs = [profile_most_probable_kmer(dna,k,profile) for dna in dnas]
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs
        else:
            return bestMotifs

def profileMatrixPesudocounts(motifs):
    columns = [''.join(seq) for seq in zip(*motifs)]
    profile = [ [float(col.count(nuc)+1) / float(len(col)+4) for nuc in 'ACGT'] for col in columns]
    return profile

def profile_most_probable_kmer(text,k,profile):
    xaxis = {'A':0,'C':1,'G':2,'T':3}
    maxprob = float('-inf')
    maxkmer = None
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        prob = 1
        for ki in range(len(kmer)):
            prob = prob * profile[ki][xaxis[kmer[ki]]]
        if prob > maxprob:
            maxkmer = kmer
            maxprob = prob
    return maxkmer

def hamming_distance(seq1,seq2):
    distance = 0
    length = len(seq1)
    for i in range(length):
        if seq1[i] != seq2[i]:
            distance += 1
    return distance

def score(motifs):
    columns = [''.join(seq) for seq in zip(*motifs)]
    max_count = sum([ max([col.count(nuc) for nuc in 'ACGT']) for col in columns ])
    return len(motifs[0])*len(motifs) - max_count
    
    bestScore = k*t
    bestMotif = None
    for repeat in xrange(1000):
        motifs = randomizedMotifSearch(dnas,k,t)
        if score(motifs) < bestScore:
            bestMotif = motifs
            bestScore = score(bestMotif)
            
print("\n".join(randomizedMotifSearch(dnas,k,t)))
