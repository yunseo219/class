class Trie(): 
    class Node:
    	def __init__(self, edgeStr):
    		self.edgeStr = edgeStr
    		self.number = number
    		self.children = []
    
    	def getChild(self,c): #character/string 
    	    for child in self.children: # find
    	    	if c == child.edgeStr:
    	    		return child
    	    child = Node(c)
    	    self.children.append(child)
    	    return child
    
    def buildSuffixTree(s): 
    	root = Node("")
    	for i in range(1,len(s)+1):
    		suffix = s[-i:] #go from the end character
    		currentNode = root # start looking for one
    		for c in suffix: #get child from 
    			currentNode = currentNode.getChild(c) 
    	return root
    
    def listNodeEdgeStr(node):
    	result = list()
    	if node.edgeStr != '':
    		result.append(node.edgeStr)
    	for child in node.children:
    		result += listNodeEdgeStr(child)
    	return result


''' #pseudocodes from book 
TrieConstruction(Patterns)
    Trie = a graph consisting of a single node root
    for each string Pattern in Patterns
        currentNode ← root
        for i ← 0 to |Pattern| - 1
            currentSymbol ← Pattern[i]
            if there is an outgoing edge from currentNode with label currentSymbol
                currentNode ← ending node of this edge
            else
                add a new node newNode to Trie
                add a new edge from currentNode to newNode with label currentSymbol
                currentNode ← newNode
    return Trie
'''
		
    def ConstructTrie(self,pattern):
        trie = Trie()
		for p in range(len(pattern)):
			currentNode = self.nodes[0] #root
			for i in range(len(pattern)-1):
			    currentSymbol = Pattern[i]
			    while currentNode.edgeStr > 1: 
	                currentNode = node.edgestr
                    if currentNode.child[i] is None:
        				#add a new Node
        				newNode = self.Node(self.N)
        				self.nodes.append(newNode)
        				currentNode.child[i] = newNode.number
        				self.nodes[currentNode.number] = currentNode
        return Trie
        				
''' #pseudocodes from book 
TrieMatching(Text, Trie)
    while Text is nonempty
        PrefixTrieMatching(Text, Trie)
        remove first symbol from Text
'''

def TrieMatching(Text, Trie):
    while Text is not None: 
        PrefixTrieMatching(Text, Trie)
        remove(pattern[0])

def PrefixTrieMatching(Text, Trie): 
    

			
def TrieTree(text):
	root = buildSuffixTree(text)
	root = compressSuffixTree(root)
	trieObj = Trie(patterns)
	trieObj.constructTrie()
	return listNodeEdgeStr(root)

#0->1:A
if __name__ == '__main__':
	text = 'AATCGGGTTCAATCGGGGT'
	patterns = ['ATCG','GGGT']
	result = TrieMatching(text,patterns)
	print ' '.join(map(str,sorted(result.keys())))