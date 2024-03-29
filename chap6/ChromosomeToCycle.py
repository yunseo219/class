"""
Code Challenge: Implement ChromosomeToCycle.
Input: A chromosome Chromosome containing n synteny blocks.
Output: The sequence Nodes of integers between 1 and 2n resulting from applying ChromosomeToCycle to Chromosome.

Sample Input:
(+1 -2 -3 +4)

Sample Output:
(1 2 4 3 6 5 7 8)
"""

Chromosome = '(+1 -2 -3 -4 +5 +6 +7 +8 +9 +10 -11 -12 -13 -14 +15 +16 +17 +18 -19 -20 -21 -22 +23 +24 -25 -26 +27 +28 -29 +30 -31 -32 +33 +34 -35 +36 +37 -38 +39 -40 -41 -42 -43 -44 +45 -46 -47 -48 +49 +50 +51 -52 +53 -54 -55 +56 -57 -58 -59 -60 +61 +62 +63 +64 +65 -66)'
#we will use the integers 2x and 2x − 1, respectively. 
#the original genome (+1 −2 −3 +4) is transformed into the cyclic sequence of nodes (1, 2, 4, 3, 6, 5, 7, 8).
def ChromosomeToCycle(Chromosome):
    Nodes = []
    for i in Chromosome: #i = j
        if i > 0:
            Nodes.append(2 * i- 1)
            Nodes.append(2 * i)
        else:
            Nodes.append(-2 * i)
            Nodes.append(-2 * i - 1)
    return Nodes

if __name__ == "__main__":
    Chromosome = Chromosome.replace('(', '').replace(')', '')
    Chromosome = [int(x) for x in Chromosome.split(' ')]
    print('(' + ' '.join(map(str, ChromosomeToCycle(Chromosome))) + ')') 
