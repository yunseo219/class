k = 12
Text = 'GCGGGAAGGTCCCGACGAAGGTCTTCCTTGGGTCAAGTGTCGACGTTCTGTTCCACTGTTATTCACACATGCCGATGAGCAACGTAGCGTCAACCGTGTAGAACTGCTCCAGCAGTTTGACAGTTGGCATAGTAATTTATTCACAACCGATCGGGGTAGCTTAATGGTGTATTAGTTGCCCAGAGTCGGAGTTGATGCAGAATCTGTATAACTGACTTATGATATTTCCCGCATACAAAAACCGTTTGAGTTCCAAAGCGATGCTGATAGAAGCTTCAGTATTAGACTCGTAAGCTGGCGAAGATTGTAAGTGTACCTCAACGGAGCACATCTGTGACCCAACTGCGTGACGCCGATAGTCGCGCGCGCAGCTCTAACTTCTCCATCAATTCTCCTTGTTGTTCCGCGCGGCATAAGTCCACAATTGGGGCCAGGACCGTCCGGACAGATCGAATGCACCGCGAACTCTGGCTAGTGAACGAAAAGAATTGGATGTAACTCGGTCCGTAGGACGAGTTCATAGGATCTGCACGATTAAACTCATCCGGCGAGCTCAGTTTCACCCAGCTTTCGATTTTTTACAAGAGATACGGTGGTGTCTCCTAGCTAAAGCTCGAAAATCGCGCGTTCTTGGGTTATGCGGGGCGAACGGATCATGGTTCATGATGATAAAGAGTGAGGGACGCGCGAGCTATACAACCAGATGGCGTCCTCACCTCGCTCGTAACGAACGTACCTACCTGATATACTGGTCTAACCGTGACGACCTTTGTCAGTTCACTAAGCCAGGGATGAAGTTACTCCGAATAACAGTGGGCAATGGCGAAAGTAATGTACCCGAAACTCGTATTCCGTTTCAACCCTCTCTGCACGATCGTTGTCGCACAGGACGACGCTAGTTCGACGCAATATTTTGTCCCTCAGAGTTCGATCGCCTGATTGAGAAGACCATTTATAATAGGCAAAGAGGCCCTTGAATGCGCGCTAGTGAGGCTGTGAACAGATACCTGAGTTAGGACGGTAATACCCAGTACACGCAAAGATCTGTACGATAACAAGGCCCGAGCTCTGGCTGAACCATATAGTAGATCCCGGGAATTATTATTCGGGTGTCGCCAGCGACTGTATGGATAGGGATGCACTCGGTCAGTTACACGATACTCTGTGGTAGACTAATAAGAAACGGGTTACCAACCTTTTGTCCCACGGCCCGGGTTAGCAACACTGCGTAGTATCATGGGTCCTTTTACGTTGGGGCTGATCTGACCCCGACCATGGTGCCACGTAGCCTTTCATACATAGTTTGCAGATGGCTCCCTCGTTATGTGGTGATCTATCAGGAACAACTGCACACCAGGCGTAATGAATGGCCGGATCGTGGCCGGTAATGTACAGTAGCTGAGTGTCTATTCTTGGGAAACGGCGCCTATTTTTGGCCTACCTTTCTAAACGCGCGAGCTGTAAGTGATGCTCGCCATTCTCCACGCTCTCAATCCGAAACGACACCCCATCGGTGTTGTACGCGGTCCCGTACGGCTGCTGGCATCCCAAAAAGTTGCATATGTTCCTCCGGACTCCTCCGTCACGAAACAAAATTGTAACACAGGGCCATCTCAACGCAATGGGCCAGTGAACCCGACAAAAAGATCCCTGAGATACGACCCCCTTTTTTACGTTGTGAAAATCTCCGAACTCATACGTTGTCTCACACGATGTTGACAAGCTTGTCCCCTTAGAACAGTGCGCTCGCCTACGCACCACAGTGTGGCTTCGGGACGTGGAAAATCACAGTGCCGGCGCATAGTATAGTTTATTGCATACGGGCCAACCTTATCCTCTAACAGAGAATCTTTGATATTCAATAGAGAAAACGCCGACTGGCGACTGTACGGGCGCCTTCCCAGAGGGCATCTGTTATTCCAAAATGATTGCCATTTGCGGGAAGTTTCGCGCCTACTTAGAGGAAAGTTTTGGCATCGAATTGTGGATGCAGACTCTTG'


def DeBruijnGraph(k,Text):
	nodes = {} #create nodes for graph
	edges = {} #create edges 
	kmers = []
	temp = [] #templist to add
	for i in range(len(Text)-k+2):
		kmers.append(Text[i:i+k-1])
	for i,s in enumerate(kmers):
		nodes[i] = s
	inn = {s:i for i,s in nodes.items()}
	for i in range(len(Text)-k+1):
		if inn[Text[i:i+k-1]] in edges:
			edges[inn[Text[i:i+k-1]]].append(inn[Text[i+1:i+k]])
		else:
			edges[inn[Text[i:i+k-1]]] = [inn[Text[i+1:i+k]]]
	for key,values in edges.items():
		temp.append(nodes[key]+' -> '+','.join(sorted([nodes[val] for val in values])) )
	return temp

print('\n'.join(sorted(DeBruijnGraph(k,Text))))