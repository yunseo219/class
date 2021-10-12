'''
CycleToChromosome(Nodes)
     for j ← 1 to |Nodes|/2
          if Nodes2j−1 < Nodes2j
               Chromosomej ← Nodes2j /2
          else
               Chromosomej ← −Nodes2j−1/2
     return Chromosome
'''

Nodes = '(1 2 4 3 5 6 7 8 9 10 12 11 13 14 15 16 17 18 19 20 21 22 23 24 25 26 28 27 29 30 32 31 33 34 36 35 37 38 39 40 42 41 44 43 46 45 48 47 50 49 52 51 53 54 56 55 58 57 59 60 62 61 64 63 66 65 68 67 70 69 72 71 74 73 76 75 77 78 79 80 82 81 83 84 85 86 87 88 90 89 92 91 94 93 95 96 98 97 100 99 101 102 104 103 105 106 107 108 110 109 112 111 114 113 115 116 117 118 119 120)'

def CycleToChromosome(Nodes):
    Chromosome = []
    for j in range(1,abs(len(Nodes)),2):
        if Nodes[j-1] < Nodes[j]:
            Chromosome.append(Nodes[j] // 2)
        else:
            Chromosome.append(-Nodes[j-1] // 2)
    return Chromosome


if __name__ == "__main__":
    Nodes = Nodes.replace('(', '').replace(')', '')
    Nodes = [int(x) for x in Nodes.split(' ')]
    print('(' + ' '.join(['+'+ str(x) if x > 0 else str(x) for x in CycleToChromosome(Nodes)]) + ')')