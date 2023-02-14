"""
Input: Two strings s and t.
Output: A longest common subsequence of s and t. (Note: more than one solution may exist, in which case you may output any one.)

    OutputLCS(backtrack, v, i, j)
        if i = 0 or j = 0
            return ""
        if backtracki, j = "↓"
            return OutputLCS(backtrack, v, i - 1, j)
        else if backtracki, j = "→"
            return OutputLCS(backtrack, v, i, j - 1)
        else
            return OutputLCS(backtrack, v, i - 1, j - 1) + vi
            
"""

import os
import sys

v = 'TCACGGCACGCTTCCGATCAACTTACTAACGCTTATCTTTCATGACAGTGATCAGCTCATAAGACATCGGGCTGGCTCCCTTCGTGCTAGGGCGGCCGAGTGCGCGCGGTAGTATGGTCACTGACGCCCGTGAGGCCGGAGGAAATCCGTTGGTTGCGAATGGCTCGCGCTCGATGACGGGAATATCGGCATCTCATATATCGAATTGGTCTAATGTATCCCCGGCCCTACCGTCAGGTTAGCTTCACGATCCAGGTTTGTGATGCGACTATTTGGGTTCGGTCGTCGGACAGGTGCTCCCATTGGAACGCCTTCTTGACTACGCCGGTGGTGACATGATGCCAGGTCAACGATGCCTACTCCGGTATAGCTCACTGCATCTGGCACTTCCGGAGACTTTTATGGACTGGCGCGAGAGTCACGGCGAAGGGACAATCCCCTACCAGGCGGATGAGCTACACTCTTTTACCTTGCTACATCCAATGACCAGCGGCGCACTTTTACTACCTGCCGCTAATGGCGGCTATGAGTACGTTGCCCGTGCGTAAGCCGAAAACGTGTCATGAAACAGGTGTGCCCAGCGCACCCTTGACACCGCATAGTTGAGTCTCATGGAGCATCGCGTGTCTTGGAAAGCGGTCCCAATTAAATGCACCACTGCGGGCATGAATTACGGCCTTTGTTATTCATATAATTCATATCATCTGAAAATGCACGCCTGTCATTCCGTTTAACGTTGGTCGATACCCCTACACAGACCACCGCGGAATCAAAAGCACGTCTGGACAGACGAGGGAAATAATCTTATGGATGAAGACCCAAGCGTTATCCGTTGCCGCTAGCTATTACTGAAGGTTTACCCGC'
w = 'AGTGTTGAATTCGGTGGAGCGATCGAACCCCGAACCCCATTGACGCTCTTCTTAGCTGCAAAGAGATTGAGGGACTGCCCCACATCTACTCGTAATACCTATACTAGGTTGGATGACGACGAAATCCGGAGGACTGGCTCATTACCGAAAGTAAGGGCGTCCGCCTATCGCATGCTGTTGGGCAGACGTTCTGCCGCACAGCCGTACAAAGCAATTTGTTCCCGGGCAAAGGAAGAGGCACCGAGAACTGAAAGGAGTCCCCAAAACAATTTGGTGTAATCCCCTGGAGAAGGGGGTAGGGGGCCATCAAATAGTAGACGTCGGTAGATGAATTACCACACAGGGGGCCTCCTTATGCCGTAGCGACGGGTTAAACGGGCACGTCGCTTTGGCTATCCTCCCGCCGGTGCCTTGCCCAACTTGACAACTCTGTACTATCCCAAGTGTCAGTCCGAGTCACTTTTGTGGTAACTGCGCTTTGCCTTCTCCGGCAAAATGGTGCGGTCCGAGGAATACATAGACAATTTCGTGGATAACTCCTGCATTAGCGGCCCGTTTTCCTCCACGCGAGCCCGCTATTCTAGGAGCGGCGGCTAGTGCATTGGATTGGATGATCTATTCCCCTCAGAGTTGACTTCAATAGTTAGAGATATACCCAGTGGAATACCAGATAGCGGCAGTGGGTAGAGGAATTTGGGCTTAGCTAGTTGTAACTTCACCGATGCGTAAGAGGGCAGGTGCGCATCAGTTGAGGTTCTTAACCTTAGACACTGGAACCTGCTTCGGGGACCCTCCAAGAATTCTAATTTGTCATCAAGTCCGTGATGATAATTTTTGCAAGATCCCTTAACTAGTGAGGAAGGCTCGT'

def LCS(v,w):
    s = [[0 for tow in range(len(w)+1)] for tov in range(len(v)+1)]
    backtrack = [[0 for tow in range(len(w)+1)] for tov in range(len(v)+1)]
    s[0][0] = 0 
    for i in range(0,len(v)):
        s[i][0] = 0 
    for j in range(0,len(w)):
        s[0][j] = 0
    for i in range(1,len(v)):
        for j in range(1,len(w)):
            deletion = s[i-1][j]
            insertion = s[i][j-1]
            match = s[i-1][j-1]+ 1 if v[i-1]==w[j-1] else s[i-1][j-1]
            s[i][j] = max(s[i-1][j], s[i][j-1],  s[i-1][j-1]+ 1 if v[i-1]==w[j-1] else s[i-1][j-1])
            if s[i][j] == deletion:
                backtrack[i][j] = "south"
            elif s[i][j] == insertion:
                backtrack[i][j] = "east"
            elif s[i][j] == s[i-1][j-1]+1 and v[i-1]==w[j-1]:
                backtrack[i][j] = "southeast"
    return backtrack

def OutputLCS(backtrack,v,i,j):
    if i == 0 or j == 0 :
        return
    if backtrack[i][j] == "south":
        OutputLCS(backtrack,v,i-1,j)
    elif backtrack[i][j] == "east":
        OutputLCS(backtrack,v,i,j-1)
    else: #southeast
        OutputLCS(backtrack,v,i-1,j-1)
        lcs.append(v[i-1]) #addition needed

if __name__ == '__main__':
    global lcs
    lcs = []
    limit = 5000
    sys.setrecursionlimit(limit)
    backtrack = LCS(v,w)
    OutputLCS(backtrack,v,len(v),len(w))
    print(''.join(lcs))
