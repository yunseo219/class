#String Composition Problem: Generate the k-mer composition of a string.

#Input: An integer k and a string Text.
#Output: Compositionk(Text), where the k-mers are arranged in lexicographic order.

#k = 5
#Text = CAATCCAAC
#output = CAATC AATCC ATCCA TCCAA CCAAC

def StringReconstruction(k, text):
    kmers = []
    for i in range(len(text) - k + 1):
        kmers.append(text[i:i+k])
    return (kmers)
print(' '.join(StringReconstruction(k, text)))
