"""
Longest Repeat Problem: Find the longest repeat in a string.

Input: A string Text.
Output: A longest substring of Text that appears in Text more than once.

Sample Input:
ATATCGTTTTATCGTT

Sample Output:
TATCGTT
"""

class SuffixTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.children = {}

class SuffixTree:
    def __init__(self, text):
        self.root = SuffixTreeNode(-1, -1)
        self.nodes = [self.root]
        self.text = text
        self.build()

    def build(self):
        for i in range(len(self.text)):
            current = self.root
            j = i
            while j < len(self.text):
                if self.text[j] not in current.children:
                    node = SuffixTreeNode(j, len(self.text)-1)
                    current.children[self.text[j]] = node
                    self.nodes.append(node)
                    break
                else:
                    node = current.children[self.text[j]]
                    k = node.start
                    while k <= node.end and j < len(self.text) and self.text[j] == self.text[k]:
                        j += 1
                        k += 1
                    if k > node.end:
                        current = node
                        continue
                    else:
                        new_node = SuffixTreeNode(node.start, k-1)
                        node.start = k
                        new_node.children[self.text[k]] = node
                        self.nodes.append(new_node)
                        current.children[self.text[new_node.start]] = new_node
                        break

    def get_edge_labels(self):
        labels = []
        for node in self.nodes:
            if node.start == -1 or node.end == -1:
                continue
            labels.append(self.text[node.start:node.end+1])
        return labels

def longest_repeat(text):
    tree = SuffixTree(text)
    labels = tree.get_edge_labels()
    max_repeat = ''
    for i in range(len(labels)):
        for j in range(i+1, len(labels)):
            k = 0
            while k < len(labels[i]) and k < len(labels[j]) and labels[i][k] == labels[j][k]:
                k += 1
            if k > 0 and k > len(max_repeat):
                max_repeat = labels[i][:k]
    return max_repeat


text = 'ATATCGTTTTATCGTT'
result = longest_repeat(text)
print(result)

#i get TTATCGTT
