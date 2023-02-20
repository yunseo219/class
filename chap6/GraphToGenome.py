"""
GraphToGenome(GenomeGraph)
     P ← an empty set of chromosomes
     for each cycle Nodes in GenomeGraph
          Nodes﻿ ← sequence of nodes in this cycle (starting from node 1)
          Chromosome ← CycleToChromosome(Nodes)
          add Chromosome to P
     return P
     
Code Challenge: Implement GraphToGenome.

Input: The colored edges ColoredEdges of a genome graph.
Output: The genome P corresponding to this genome graph.

Sample Input:
(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)

Sample Output:
(+1 -2 -3)(-4 +5 -6)
"""

Edges = '(1, 4), (3, 6), (5, 7), (8, 10), (9, 12), (11, 14), (13, 15), (16, 18), (17, 20), (19, 21), (22, 23), (24, 25), (26, 27), (28, 29), (30, 31), (32, 34), (33, 35), (36, 37), (38, 39), (40, 42), (41, 44), (43, 45), (46, 47), (48, 50), (49, 52), (51, 54), (53, 2), (56, 58), (57, 59), (60, 61), (62, 63), (64, 66), (65, 68), (67, 70), (69, 72), (71, 74), (73, 75), (76, 78), (77, 79), (80, 81), (82, 84), (83, 85), (86, 88), (87, 89), (90, 91), (92, 94), (93, 95), (96, 97), (98, 99), (100, 102), (101, 103), (104, 106), (105, 107), (108, 109), (110, 112), (111, 114), (113, 55), (116, 117), (118, 120), (119, 122), (121, 124), (123, 125), (126, 127), (128, 130), (129, 131), (132, 133), (134, 135), (136, 137), (138, 139), (140, 142), (141, 143), (144, 145), (146, 148), (147, 150), (149, 151), (152, 153), (154, 156), (155, 157), (158, 115), (159, 161), (162, 163), (164, 166), (165, 168), (167, 169), (170, 171), (172, 173), (174, 175), (176, 177), (178, 179), (180, 182), (181, 184), (183, 185), (186, 187), (188, 190), (189, 191), (192, 193), (194, 195), (196, 197), (198, 200), (199, 202), (201, 160), (203, 206), (205, 207), (208, 209), (210, 211), (212, 213), (214, 216), (215, 218), (217, 219), (220, 222), (221, 223), (224, 225), (226, 228), (227, 230), (229, 232), (231, 234), (233, 235), (236, 237), (238, 240), (239, 242), (241, 244), (243, 245), (246, 247), (248, 204), (250, 252), (251, 254), (253, 255), (256, 257), (258, 260), (259, 261), (262, 263), (264, 265), (266, 267), (268, 269), (270, 272), (271, 273), (274, 276), (275, 277), (278, 279), (280, 281), (282, 284), (283, 285), (286, 287), (288, 290), (289, 291), (292, 293), (294, 296), (295, 297), (298, 299), (300, 302), (301, 303), (304, 305), (306, 249), (307, 309), (310, 311), (312, 314), (313, 315), (316, 318), (317, 319), (320, 321), (322, 324), (323, 326), (325, 327), (328, 329), (330, 332), (331, 334), (333, 336), (335, 338), (337, 340), (339, 341), (342, 344), (343, 346), (345, 348), (347, 349), (350, 352), (351, 353), (354, 355), (356, 308), (357, 359), (360, 361), (362, 364), (363, 366), (365, 367), (368, 369), (370, 372), (371, 373), (374, 376), (375, 377), (378, 380), (379, 382), (381, 384), (383, 386), (385, 388), (387, 390), (389, 392), (391, 394), (393, 396), (395, 397), (398, 399), (400, 402), (401, 403), (404, 358)'

def CycleToChromosome(Nodes):
    Chromosome = []
    for j in range(1,abs(len(Nodes)),2):
        if Nodes[j-1] < Nodes[j]:
            Chromosome.append(Nodes[j] // 2) #float
        else:
            Chromosome.append(-Nodes[j-1] // 2)
    return Chromosome


def GraphToGenome(GenomeGraph):
    P = []
    Cycles = []
    Cycle = []
    startnode = []
    if len(GenomeGraph) == 0: #empty no 
        return -1
    while len(GenomeGraph) != 0: #check if for each cycle Nodes in GenomeGraph
        Cycle = []
        startnode = GenomeGraph[0]
        while startnode != -1:
            Cycle += startnode #Nodes﻿ ← sequence of nodes in this cycle (starting from node 1)
            GenomeGraph.remove(startnode)
            startnode = Movenext(startnode, GenomeGraph) 
        Cycles.append(Cycle)
    for Cycle in Cycles: #feed cyclenode to chrom
        Chromosome = CycleToChromosome([Cycle[-1]] + Cycle[:-1])
        P.append(Chromosome)
    return P

def Movenext(startnode, edges, i=0):
    #startnode = []
    #edges = []
    if len(edges) == 0:
        return -1
    elif len(edges) != 0:
        while not (startnode[1] + 1 == edges[i][0] or startnode[1] - 1 == edges[i][0]):
            i += 1      
            if i == len(edges):
                return -1
    return edges[i]

if __name__ == "__main__":
    Edges = Edges.split('), (')
    for i in range(len(Edges)):
        Edges[i] = Edges[i].replace('(', '').replace(')', '')
        Edges[i] = [int(x) for x in Edges[i].split(',')]
    m = GraphToGenome(Edges)
    for j in range(len(m)):
        m[j] = ('(' + ' '.join(('+' if i > 0 else '') + str(i) for i in m[j]) + ')')
    print(''.join(m))
