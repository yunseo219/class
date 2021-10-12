k = 12
t = 25
Dna = ['ATTTACAATTTCTTAAGATAACCGCAGTGGCTCGGCCTGGGTTATCGCCTCGAGCATGCAGCAGTAGCACTTCCACCGCTTAATGACCTGAAGCTTAATCGACCGGCGTAGTCCGGGGAACACTGTGGCTGGGCGTAAAAATATTCCCTCTCACAC',
'CTATGGCGTCCCGGGTCGAGTAGACTTCGTGTGGGTTCTTGGCGAGCGGTACGTCAACCGTGTGTAGGAGATAACCAGGTCTACCACTGGGTCCAGCAGCAGAACCAGTGCAGTTGCTTAGGAGGGCTGCCAGCGCGGGCCGCAGGCCCCGTTCCG',
'AGGTCCAGGTTACTCTAGCCCAGTTATGGACCCGGCCCAATGCTCCACCCTTCGTGTCAACGATACCCACCGTCCTGACGAGTAGGGTGTGAAGGTGTTTCTCGCCTTATAAACGAGTCAGTTGAAACAGATTTAAGTTAACCGTTTGTTTTAGAG',
'CAATGTCCTATAGAAGATCCTAAGGCTTCCAGGAACACGCTACTAAAGTTACTTATTCTCTGAGGAGCTTCCGTAAACAGTCACTGACAACTTTCTACCAATCTGGTGCTGGTTTCCGTCCTGCCTCAAAATGTAAGCTAACCGAATCGACGCCCG',
'TACCAAGGTATTATAAGCCAACCGACTGTGGTTCAGCGTCAAAGGGTGACGTTGTAGTGCAATCCCTGCAGTATCGTGGCATTGACGCAACAAGACGTTGGGATGCTCCCCTGCGGTCTACCGCTATGCCGGAGTTGCACACGAGGACGAGATGAA',
'ACTGGCGTGGATCTTGACTGCAACATCTCGCGGCAAAGAAAGTCACAAGGCGTTATTAATGCACAGGTGTAACAAAGTGGACAGGCTCTGTGAAATCGCATTGTTATAAGGTATGTTGCGCCATAGACGTGGATAGATAGGCGGATATGCAAACCG',
'ACCCCGACTAAACGCAATGCTAAGGTATGTAAACCGCTTCGTACCGCATAGCTCAAATTTTAATTTAGGCGCATCCGTATCGGGAACAACACTGGGAGAGAAGAGTAGCATATAGACTGCCCTATTAGGCCCCCCACTTTGAGTTTTGGACTCGGG',
'GCTTGCTAGTGCATTCGCGGTGCGAAGAACAACACCACGATTTATTCTAACCCACGAACTTATCTGTGCAAACTTGTCTGGTCCCAAGTGACTTCTTTTCGACTTGTCTTATGTGAACCGACCTCTATATCATCCCAAGAACAACCACTAGACTCC',
'GGGGAAAACGTGGGATTCCACCTGGCGCATACCCAGTCGCCGGCACTGGGAGCGATCTCGCGTACTCTCCTACCCGGAAATGGTACACCCGTGAAAGGTAAACTAGCGCGTCACTTCCCCGGTGGCCTCGAGCGCACAGCGGAGGTACGCGAACCG',
'TGTCCGGCCTGCCGTGCATTCTTTTCTAAAGGATATTGGTTACTACTATCTCTGGAGCGCCATACTTGAGTTTATAGAATCAATTCCTCCCCGTGCGAAAGCGCATTTTTAGGGGTCTGAGAGAGGGGCAGGAAGTGATATTCAGTAGGTAAACCG',
'TAGTGGTTATCCCTTAGTTAAATTAGCACAGTGGTATCACTCGCAACACGGGAGATGCCATTAAGGCAACCGGGATAGGGGTGACGACACTCTGGTTAACTCTCAACCTTGGTGGACAGCCAGATAGGCGAACCCCCTTGCATAGCAGTATAGTCT',
'TGTATACCGCCCTTATGGTAACCGGCCCACTAACTGCGAACTAGGTACAGTCGGTCATGCCTACAATCCGGAGGAACACTCTGAATAGGTCGAACACCCCTCGCCTTAAAGGTAGGTTGGGTGCGGGGAGTTCGCTCGTAGATTGGGCTTGTTGCC',
'CTGCTGGTTTACTCATTAAGTTCCTCTGACCGCTCAGCGCTTCTATAACCTTTTGTTTTCATATGTTAACCGGGTTGTTCAACACGCGCTTGAATACTATTCACTTTCTACCTTCGATTATTTTGAACCCGAATCGGCAAAAATCAAATTGTGCAT',
'TTCTCCCCTACCAGCAGGGATCAACAAAAACAGACGCGTAATGAACCTATGTAAGGCAATGTTACATTGGGCCTCGGAATAATAGCCTAACCCAGACTAAGGTAACCGCGGGAGTGTCTCATCTCCCGCTTTCTCAATATCATCGATGCGCGACTT',
'AACCTATGACACTTAAGTCCTACCGCGAAGGCCTGATGGTAACCGGAACTAAGCGAACCGGGGCCATGACGGTGGTACGGTGGGCGTAGAAAGCCTGTCTGCCCTCAGAATGCGAAGGACTACCAACCGCCATAGCCCCTGAGGTGCCAGTGAGCA',
'CAATCACGATCTCTCAGCCGTACTTCGTATCGGGATTCTTCGAATCAGATTAGAGGTTTGGCAACCTACTGAATACGCCAACCGCTCGTGTGCGTTCAGCTCTAAAACTACCTCTCCCGTTACGAGCCTTCAGATGAGGAGGCATAAGGTGGATCG',
'CTCGATGAAAAAGCGTGTACCTTTACGCAACTCTTTTTAAGCGAACCGCGTTGCAGAACCTGGACATTCTTTCGAAGAGCTCGACGCAACACAACCACAGAACTCGGAATGAGATAGCATATATCCTCAAAGACTCGAGCGTCGCCCCTCTGGACC',
'GCGTCGTCGATACTACGCGAACCGTCCGCATGCGTCCTAAGCCGAATCGGCATCGACCGAGGCCATCCCTCAGCGGGCTTACGCGCAGTCGTAAGTGCATTACCCAGAGGTCCGGTCGGGCGCAAAGTGATTACGCAATGGACAACACATAAAAAT',
'GTATGAAAACCGTCACACTTGGTTGATGATTCCAGCATCCTATAGGCCTCTGGACTCTGTGCACCGTGGCCCAAGTGGAAACAAGAGATAACTTCTGACGGACCAGGGATCCCGAGCAAGCTCGATGTGTTTAGGATTATTGAACTATCCGTAGTT',
'ATGGCACGAGCGTGTTCGAGGGAATAGTGATCTAGCCAACTACATGGACACACATTATTAACGATAATTTACTCGTGTAAGGATAAGTAACTTCTTTTTTTAGCTTACCTCGTGACGTCATTACGGTAACCGCAAAATCGCTCCATAATCCCAGTG',
'CCTAGAATCGAATCAACAGAAAGGGAACCCGTACTGTACCCTTGACTCTTATGCGAACCGGCTGGGAGAAGCATTACCGTGCAATCGTTGATACGCTTCGGCCGCAGTCTTTGTCGTTCAGATCGCCCATTGATGTAGCCGTAGAACATAACTAGA',
'CTGGATAAAGGCTACCATTTGACGAGCCCGTAAGGAATCCCAAACCGTTTATGGGAACCGCGAATAATTTAGTTAGCTGACATTTGGTCAGGTCAGATGAGGAAGGGGGGGGTGCAGTTGCCCAGTCCTAGTATTTGTATTCTACAACTACCTAGA',
'GTTACAGGGTACAAGGAGTTGATTGCCATAAGCGTCAATATTCTTTCCGGCCCAGTTCGTGAACAACACGTTTGAGTGATAGATTAATGTTTATTGTAATATTTTGAGGTACGTAAACCGTTTAAGAGACAGGAGCAAACCCGCCCCCTTGTGAGG',
'TAGTCAGGCATACTATAACTAGAATGCATTGGTGACGTACGTAAACCGGATGCCTCGTTACTAGTGTACAAACCTTATTCCTCTCACGTGTGACCGGAATTAAGTTTGGGTCGCATGCAACTTAGATTCGACGTTCAAAGCACGTCGGCCCATGGC',
'TCTCGCACTACCACCACGTGGAGATCAGTATCTCCAACTTCACGCTGGTTGACTAGGCTTGTGAGCGGAAGAAATACGTCTTATATAGGACAACCGGCGAAGAACTTCGTACGTTTAGTCACCCTAATCCCCCCCATGGACCGTTGCTTAGGTCCC']

def Count(Motifs):
    count = {}
    for nucleo in "ACGT": # each key in the dictionary ("A", "C", "G", "T") 
        count[nucleo] = []
        for j in range(len(Motifs[0])):
            count[nucleo].append(0)
    for i in range(len(Motifs)):
        for j in range(len(Motifs[0])):
            nucleo = Motifs[i][j]
            count[nucleo][j] += 1
    return count

def Profile(Motifs):
    profile = {}
    count = Count(Motifs)
    for key, mlists in sorted(count.items()):
        profile[key] = mlists
        for mlist, number in enumerate(mlists):
            mlists[mlist] = number/len(Motifs)
    return profile

def Consensus(Motifs):
    profile = Profile(Motifs)
    consensus = ""
    for j in range(len(Motifs[0])):
        maximum = 0
        frequent = ""
        for nucleo in "ACGT":
            if profile[nucleo][j] > maximum:
                maximum = profile[nucleo][j]
                frequent = nucleo
        consensus += frequent
    return consensus

def Score(Motifs):
    count = 0
    consensus = Consensus(Motifs)
    for motif in Motifs:
        for index, letter in enumerate(motif):
            if letter != consensus[index]:
                count += 1
    return count

def probability_nucleo(Pattern, Profile):
    probability = 1
    for i,nuc in enumerate(Pattern): 
        for j, listofprof in sorted(Profile.items()): 
            if nuc == j:
                probability *= listofprof[i]
    return probability
    
def ProfileMostProbable(Text, k, Profile):
    maxi = -1
for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        prob = probability_nucleo(kmer, profile)
        if prob > maxp:
            maxp = prob
            maxk = kmer
    return maxk

def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    for i in range(len(Dna[0])-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbable(Dna[j], k, P))
        if  Score(BestMotifs) > Score(Motifs):
            BestMotifs = Motifs
    return BestMotifs
    
print("\n".join(GreedyMotifSearch(Dna, k, t))) 