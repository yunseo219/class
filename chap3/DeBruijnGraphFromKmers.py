def DeBruijnGraphFromKmers(Patterns):
	nodes = {}
	edges = {}
	kmers = [k[:-1] for k in Patterns] + [k[1:] for k in Patterns]
	temp = []
	for i in range(len(kmers)):
		nodes[i] = kmers[i]
	inn = {s:i for i,s in nodes.items()}
	for pattern in Patterns:
		if inn[pattern[:-1]] in edges:
			edges[inn[pattern[:-1]]].append(inn[pattern[1:]])
		else:
			edges[inn[pattern[:-1]]] = [inn[pattern[1:]]]
	for key, values in edges.items():
		temp.append(nodes[key] +' -> '+','.join([nodes[val] for val in values]))
	return temp

file = 'dataset_442812_8.txt'   
with open(file) as f:
	Patterns = f.read().splitlines()

print('\n'.join(DeBruijnGraphFromKmers(Patterns)))