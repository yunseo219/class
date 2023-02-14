"""
Solve the Longest Path in a DAG Problem.

Input: An integer representing the starting node to consider in a graph, followed by an integer representing the ending node to consider, followed by a list of edges in the graph. The edge notation "0->1:7" indicates that an edge connects node 0 to node 1 with weight 7.  You may assume a given topological order corresponding to nodes in increasing order.
Output: The length of a longest path in the graph, followed by a longest path. (If multiple longest paths exist, you may return any one.)
Extra Dataset and Test Datasets

Sample Input:
0
4
0->1:7
0->2:4
2->3:2
1->4:1
3->4:3

Sample Output:
9
0->2->3->4
"""

import sys
sys.setrecursionlimit(3000)
def LCSBackTrack(v, w):
    s = {}
    Backtrack = {}
    for i in range(len(v)+1):
        s[(i, 0)] = 0
    for j in range(len(w)+1):
        s[(0, j)] = 0
    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            match = 0
            if v[i-1] == w[j-1]:
                match = 1
            s[(i, j)] = max([s[(i-1, j)] , s[(i,j-1)] , (s[(i-1, j-1)] + match)])
            if s[(i,j)] == s[(i-1,j)]:
                Backtrack[(i, j)] = "↓"
            elif s[(i, j)] == s[(i, j-1)]:
                Backtrack[(i, j)] = "→"
            elif s[(i, j)] == (s[(i-1, j-1)] + match):
                    Backtrack[(i, j)] = "↘"
    return Backtrack
