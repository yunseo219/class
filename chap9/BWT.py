"""
Burrows-Wheeler Transform Construction Problem: Construct the Burrows-Wheeler transform of a string.

Input: A string Text.
Output: BWT(Text).

Note: Although it is possible to construct the Burrows-Wheeler transform in O(|Text|) time and space, we do not expect you to implement such a fast algorithm. In other words, it is perfectly fine to produce BWT(Text) by first producing the complete Burrows-Wheeler matrix M(Text).

Sample Input:
GCGTGCCTGGTCA$

Sample Output:
ACTGGCT$TGCGGC
"""
#cyclic rotation is defined by chopping off a suffix from the end of Text and appending 
#this suffix to the beginning of Text. Next — similarly to suffix arrays 
#— order all the cyclic rotations of Text lexicographically to form a |Text| × |Text| matrix of symbols

Text = 'TAAGATCTACCGTGTATCCCCATGTCCCCTGCGGTTTCAAAGTCATAATCAGTATTGCTTGTCCAATACATGTCTTTAAATCCGGAACCTTCACTCCACCTCTATAATTCATACGGGTCGTCCCTACCTCCCTGAGATTTAATGTACTTCTGCCCGTAAAACAGCCCAAAGGACTATCAAGGACAACAAAATATACGACACCCAAAATCTGACAGACTACCATTACAATCGCACTAGAGTGGATAGGCTGCTAGGAAGAACGCCTCCGTGCAGACGAAGGAAATTTGAGGGAACTTTGCGCTAGATCAACAAACCTCTCCGTTTTAGATCACAAGCTTGCACTCTTAAATTTGCTAACCTTGTCAAGAGGACGGTGTAAAAGCGCAGGATTAACGCCTGTGAATCCTCCAATTGCGTACGGGGACTGGGTTTTGTCCATCGTGGGGCCGATAAATGTCCTCAAGGTTTATTCTTATTTAGGGGATGGGGGTGCGTCCATGTAATTCATACAAGGTGGTTGCAGAACCGGGTAAATAGCGGGAAATGAGTTAGCCGCGTTGTAGAGACGAAAAGCTTGCGCTTTTAGTAGCAAGAGTCCCCTATACAGATGGGGACTGGCCCTAAGGAAGCTGAGCCAAAGAGAGCTGTGCCCGAGAGCGTCGTGTTGTCTCCCTCGTGGACATTAAAGTCGCCCCAACCAATTTGGCCAAGCACTTGTCTTGTAGCGGGGTCGGGAGCGCCATGCCGGGATCAAATAGATCCGGACAAAACGTTGGCTAGGCTTGAGCAAGCTTCGTCGCTATTTTCTAATTGGAATTGGCCCCTGCGTTCCCCCATTGTACCCACAGCGCTGCTACGACACAGCTCAGTGAAGATTGAGACCTTC$'

def BWT(Text):
    x, y = [], [] 
    for i in range(len(Text)):
        x.append(Text[i:])
        y.append(i)
    y = sorted([Text[i:] + Text[:i] for i in range(len(Text))]) #cyclic rotations
    bwt = ([Text[-1] for Text in y])
    return bwt

print (''.join(BWT(Text)))
