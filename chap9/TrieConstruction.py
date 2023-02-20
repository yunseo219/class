"""
Code Challenge: Solve the Trie Construction Problem.

Input: A collection of strings Patterns.
Output: The adjacency list corresponding to Trie(Patterns), in the following format. If Trie(Patterns) has n nodes, first label the root with 0 and then label the remaining nodes with the integers 1 through n - 1 in any order you like. Each edge of the adjacency list of Trie(Patterns) will be encoded by a triple: the first two members of the triple must be the integers labeling the initial and terminal nodes of the edge, respectively; the third member of the triple must be the symbol labeling the edge.

Sample Input:
ATAGA
ATC
GAT

Sample Output:
0->1:A
1->2:T
2->3:A
3->4:G
4->5:A
2->6:C
0->7:G
7->8:A
8->9:T

TrieConstruction(Patterns)
    Trie ← a graph consisting of a single node root
    for each string Pattern in Patterns
        currentNode ← root
        for i ← 1 to |Pattern|
            if there is an outgoing edge from currentNode with label currentSymbol
                currentNode ← ending node of this edge
            else
                add a new node newNode to Trie
                add a new edge from currentNode to newNode with label currentSymbol
                currentNode ← newNode
    return Trie

#Bruteforce is not optimal
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.node_count = 0
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                self.node_count += 1
            node = node.children[char]
        node.is_word_end = True
    
    def build_adjacency_list(self):
        adjacency_list = []
        node_labels = {self.root: 0}
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            for char, child in node.children.items():
                if child not in node_labels:
                    self.node_count += 1
                    node_labels[child] = self.node_count
                    queue.append(child)
                adjacency_list.append((node_labels[node], node_labels[child], char))
        return adjacency_list

patterns = ['ATAGA', 'ATC', 'GAT']
trie = Trie()
for pattern in patterns:
    trie.insert(pattern)
adjacency_list = trie.build_adjacency_list()
for edge in adjacency_list:
    print(f'{edge[0]}->{edge[1]}:{edge[2]}')
