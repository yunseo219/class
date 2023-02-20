"""
Code Challenge: Implement TrieMatching to solve the Multiple Pattern Matching Problem.

Input: A string Text and a collection of strings Patterns.
Output: All starting positions in Text where a string from Patterns appears as a substring.

Sample Input:
AATCGGGTTCAATCGGGGT
ATCG
GGGT

Sample Output:
1 4 11 15
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word_end = True
    
    def get_match_positions(self, text):
        positions = []
        for i in range(len(text)):
            node = self.root
            j = i
            while j < len(text) and text[j] in node.children:
                node = node.children[text[j]]
                j += 1
                if node.is_word_end:
                    positions.append(i)
        return positions

def trie_matching(text, patterns):
    trie = Trie()
    for pattern in patterns:
        trie.insert(pattern)
    return trie.get_match_positions(text)

text = 'AATCGGGTTCAATCGGGGT'
patterns = ['ATCG', 'GGGT']
positions = trie_matching(text, patterns)
print(' '.join(map(str, positions)))
