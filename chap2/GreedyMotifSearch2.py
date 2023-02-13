# Using GreedyModifysearch with profile would still be calculated to 0.somethign so bioinformaticians often substitute zeroes with small numbers called pseudocounts. i.e Laplace’s Rule of Succession. 
#In the case of motifs, pseudocounts often amount to adding 1 (or some other small number) to each element of Count(Motifs).

"""
    GreedyMotifSearch(Dna, k, t)
        form a set of k-mers BestMotifs by selecting 1st k-mers in each string from Dna
        for each k-mer Motif in the first string from Dna
            Motif1 ← Motif
            for i = 2 to t
                ****apply Laplace's Rule of Succession to form Profile from motifs Motif1, …, Motifi-1
                Motifi ← Profile-most probable k-mer in the i-th string in Dna
            Motifs ← (Motif1, …, Motift)
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
        output BestMotifs
"""
#Input: Integers k and t, followed by a collection of strings Dna.
#Output: A collection of strings BestMotifs resulting from applying GreedyMotifSearch(Dna, k, t) with pseudocounts. If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.
#output: TTC ATC TTC ATC TTC

k = 3
t = 5
Dna = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']

def hamming_distance(seq1,seq2):
	distance = 0
	length = len(seq1)
	for i in range(length):
		if seq1[i] != seq2[i]:
			distance += 1
	return distance

def probability_nucleo(Pattern, Profile):
    probability = 1
    for i,nuc in enumerate(Pattern): 
        for j, listofprof in sorted(Profile.items()): 
            if nuc == j:
                probability *= listofprof[i]
    return probability

def ProfileMostProbable(text, k, profile):
    maxp = -1
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        prob = probability_nucleo(kmer, profile)
        if prob > maxp:
            maxp = prob
            maxk = kmer
    return maxk

def TextProfile(Text, pseudocounts=1):
    t = len(Text[0])
    if type(Text) != list:
        Text = [Text]
    profile = {'A': [pseudocounts] * t, 'C': [pseudocounts] * t, 'G': [pseudocounts] * t, 'T': [pseudocounts] * t}
    for i in range(t):
        for j in range(len(Text)):
            profile[Text[j][i]][i] += 1
    return profile

def Calculate(Motifs):
    k = len(Motifs[0])
    profile = TextProfile(Motifs)
    Score= 0
    consensus = ''
    for i in range(k):
        freqent = 0
        for nucleotide in ['A', 'C', 'G', 'T']:
            if profile[nucleotide][i] > freqent:
                freqent = profile[nucleotide][i]
                addon = nucleotide
        consensus += addon
    for motif in Motifs:
        Score += hamming_distance(consensus, motif)
    return Score

def GreedyMotifSearch(Dna, k, t):
    BestMotifs = [dna[0:k] for dna in Dna]
    Optimize = Calculate(BestMotifs)
    DNA = Dna[0]
    for i in range(len(DNA) - k + 1):
        Motifs = [DNA[i:i + k]]
        for j in range(1, t):
            profile = TextProfile(Motifs)
            Motifs.append(ProfileMostProbable(Dna[j], k, profile))
        Curr = Calculate(Motifs)
        if Curr < Optimize:
            BestMotifs = Motifs
            Optimize = Curr
    return BestMotifs
    
print("\n".join(GreedyMotifSearch(Dna, k, t))) 
