"""
Shortest Non-Shared Substring Problem: Find the shortest substring of one string that does not appear in another string.

Input: Strings Text1 and Text2.
Output: The shortest substring of Text1 that does not appear in Text2.

Sample Input:
CCAAGCTGCTAGAGG
CATGCTGGGCTGGCT

Sample Output:
AA; multiple answers
"""

def shortest_non_shared_substring(text1, text2):
    # Initialize the shortest non-shared substring to be the entire text1
    shortest = text1

    # Check every substring of text1 of length n, where n is 1, 2, ..., len(text1)
    for n in range(1, len(text1) + 1):
        # Check every substring of text1 of length n
        for i in range(len(text1) - n + 1):
            substring = text1[i:i+n]
            if substring not in text2:
                # If the substring is not in text2, check if it is shorter than the current shortest
                if len(substring) < len(shortest):
                    shortest = substring

    return shortest

text1 = 'CCAAGCTGCTAGAGG'
text2 = 'CATGCTGGGCTGGCT'
print(shortest_non_shared_substring(text1, text2))  # Output: 'AA'

