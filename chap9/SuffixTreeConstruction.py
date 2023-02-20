"""
Code Challenge: Solve the Suffix Tree Construction Problem.

Input: A string Text.
Output: The edge labels of SuffixTree(Text). You may return these strings in any order.

Sample Input:
ATAAATG$

Sample Output:
AAATG$
G$
T
ATG$
TG$
A
A
AAATG$
G$
T
G$
$
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
                    node = SuffixTreeNode(j, len(self.text))
                    current.children[self.text[j]] = node
                    self.nodes.append(node)
                    break
                else:
                    node = current.children[self.text[j]]
                    k = node.start
                    while k <= node.end and self.text[j] == self.text[k]:
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

text = 'ATAAATG$'
tree = SuffixTree(text)
edge_labels = tree.get_edge_labels()
print('\n'.join(edge_labels))

