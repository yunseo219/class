'''
Code Challenge: Implement ColoredEdges.
Input: A genome P.
Output: The collection of colored edges in the genome graph of P in the form (x, y).

Sample Input:
(+1 -2 -3)(+4 +5 -6)

Sample Output:
(2, 4), (3, 6), (5, 1), (8, 9), (10, 12), (11, 7)

ColoredEdges(P)
     Edges ← an empty set
     for each chromosome Chromosome in P
          Nodes ← ChromosomeToCycle(Chromosome)
          for j ← 1 to |Chromosome|
               add the edge (Nodes2j, Nodes2j +1) to Edges
     return Edges
'''

P = '(-1 -2 +3 +4 +5 -6 -7 +8 +9 -10 -11 -12 -13 +14 -15 +16 -17 +18 -19 -20 -21 -22 +23 +24 +25 +26 -27 +28 -29 +30 +31)(-32 -33 -34 -35 +36 -37 -38 -39 +40 -41 +42 -43 +44 -45 -46 +47 -48 +49 -50 +51 +52 +53 -54 -55 +56 -57 -58 +59)(-60 +61 +62 +63 -64 -65 +66 -67 -68 -69 -70 -71 -72 +73 -74 -75 -76 -77 +78 +79 +80 -81 -82)(-83 -84 +85 +86 -87 +88 +89 +90 +91 -92 -93 -94 +95 -96 -97 +98 -99 +100 +101 +102 +103)(+104 +105 -106 -107 +108 +109 -110 +111 -112 +113 +114 -115 +116 -117 +118 +119 -120 -121 -122 +123 +124 -125 +126)(+127 -128 -129 +130 -131 +132 +133 +134 +135 -136 -137 -138 -139 -140 +141 +142 +143 +144 +145 +146 +147 +148 -149 +150 -151 +152 +153 -154 +155 +156)(-157 -158 +159 -160 -161 -162 -163 -164 +165 -166 +167 -168 -169 +170 -171 -172 +173 +174 +175 +176 -177 -178 -179 +180 -181 -182 -183)(+184 +185 -186 +187 -188 -189 -190 +191 +192 -193 +194 +195 -196 +197 +198 +199 -200 +201 -202 +203 -204 +205 -206 -207 +208 +209 -210 +211 +212 -213 -214)'


def ChromosomeToCycle(Chromosome):
    Nodes = []
    for i in Chromosome:
        if i > 0:
            Nodes.append(2 * i- 1)
            Nodes.append(2 * i)
        else:
            Nodes.append(-2 * i)
            Nodes.append(-2 * i - 1)
    return Nodes

def ColoredEdges(P):
    Edges = list() #an empty set
    for chromosome in P:
        Nodes = ChromosomeToCycle(chromosome)
        for j in range(1, abs(len(Nodes)), 2):
            if j != len(Nodes) - 1:
                Edges.append([Nodes[j], Nodes[j + 1]])
            else:
                Edges.append([Nodes[j], Nodes[0]])
    return Edges


if __name__ == "__main__":
    P = P[1:-1].split(')(')
    for i in range(len(P)):
        P[i] = [int(x) for x in P[i].split(' ')]
    k = ColoredEdges(P)
    for j in range(len(ColoredEdges(P))):
        k[j] = '(' + ', '.join(str(i) for i in k[j]) + ')'
    print(', '.join(k))
