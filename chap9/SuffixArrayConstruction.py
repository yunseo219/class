"""
Suffix Array Construction Problem: Construct the suffix array of a string.

Input: A string Text.
Output: SuffixArray(Text).

Sample Input:
AACGATAGCGGTAGA$

Sample Output:
15, 14, 0, 1, 12, 6, 4, 2, 8, 13, 3, 7, 9, 10, 11, 5
"""

def suffix_array(text):
    n = len(text)
    # create a list of all suffixes and their indices
    suffixes = [(text[i:], i) for i in range(n)]
    # sort the suffixes lexicographically
    suffixes.sort()
    # extract the indices of the sorted suffixes
    return [suffix[1] for suffix in suffixes]
    
text = "AACGATAGCGGTAGA$"
suffix_array = suffix_array(text)
print(suffix_array)
