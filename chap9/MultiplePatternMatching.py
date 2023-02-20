"""
Code Challenge: Solve the Multiple Pattern Matching Problem.

Input: A string Text followed by a collection of strings Patterns.
Output: All starting positions in Text where a string from Patterns appears as a substring.

Sample Input:
AATCGGGTTCAATCGGGGT
ATCG
GGGT

Sample Output:
1 4 11 15
"""

def multiple_pattern_matching(text, patterns):
    positions = []
    for pattern in patterns:
        # find all occurrences of the pattern in the text
        start = 0
        while True:
            index = text.find(pattern, start)
            if index == -1:
                break
            positions.append(index)
            start = index + 1
    # sort the list of positions in ascending order and return as a space-separated string
    return " ".join(str(pos) for pos in sorted(positions))

text = "AATCGGGTTCAATCGGGGT"
patterns = ["ATCG", "GGGT"]
positions = multiple_pattern_matching(text, patterns)
print(positions)
