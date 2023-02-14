"""
Input: Integers n and m, followed by an n × (m + 1) matrix Down and an (n + 1) × m matrix Right. The two matrices are separated by the "-" symbol.
Output: The length of a longest path from source (0, 0) to sink (n, m) in the rectangular grid whose edges are defined by the matrices Down and Right.

Sample Input:
4 4
1 0 2 4 3
4 6 5 2 1
4 4 5 2 1
5 6 8 5 3
-
3 2 4 0
3 2 4 2
0 7 3 3
3 3 0 2
1 3 2 2

Sample Output:
34
"""


def ManhattanTourist(n, m, Down, Right):
    S = [[0 for tom in range(m + 1)] for ton in range(n + 1)]
    for i in range(1, n + 1):
        S[i][0] = S[i - 1][0] + Down[i - 1][0]
    for j in range(1, m + 1):
        S[0][j] = S[0][j - 1] + Right[0][j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            S[i][j] = max(S[i - 1][j] + Down[i - 1][j], S[i][j - 1] + Right[i][j - 1])
    return S[n][m]


file = 'dataset_442856_10.txt'
with open(file) as f:
	lines = f.read().splitlines()
	#n, m = [int(x) for x in lines[0].split()]
n = int(lines[0].split()[0])
m = int(lines[0].split()[1])
Down = []
Right = []
for idex in range(1, n + 1):
	Down.append([int(x) for x in lines[idex].split()])
for idex in range(n + 2, len(lines)):
	Right.append([int(x) for x in lines[idex].split()])
print(ManhattanTourist(n, m, Down, Right))
