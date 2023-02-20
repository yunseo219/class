"""
Longest Shared Substring Problem: Find the longest substring shared by two strings.

Input: Strings Text1 and Text2.
Output: The longest substring that occurs in both Text1 and Text2.

Sample Input:
TCGGTAGATTGCGCCCACTC
AGGGGCTCGCAGTGTAAGAA

Sample Output:
AGA
"""

def longest_shared_substring(text1, text2):
    # initialize variables to store length and position of longest common substring
    longest_length = 0
    longest_position = 0

    # create a table to store the lengths of common substrings
    table = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

    # fill the table using dynamic programming approach
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > longest_length:
                    longest_length = table[i][j]
                    longest_position = i
            else:
                table[i][j] = 0

    # extract the longest common substring from the first text
    longest_substring = text1[longest_position - longest_length: longest_position]

    return longest_substring


text1 = 'TCGGTAGATTGCGCCCACTC'
text2 = 'AGGGGCTCGCAGTGTAAGAA'
print(longest_shared_substring(text1, text2))  # Output: 'AGA'
