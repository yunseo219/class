'''
    GreedySorting(P)
        approxReversalDistance ← 0
        for k = 1 to |P|
            if element k is not sorted
                apply the k-sorting reversal to P
                approxReversalDistance ← approxReversalDistance + 1
            if k-th element of P is −k
                apply the k-sorting reversal to P
                approxReversalDistance ← approxReversalDistance + 1
        return approxReversalDistance



'''


P = '+53 -91 -121 -10 -74 -9 -46 +136 +131 +32 -127 -70 -6 -2 -108 +22 +50 +118 +59 +139 +72 +138 +102 -5 +4 +16 -107 +77 +113 +55 +106 -117 +40 +137 +100 +116 -103 +114 -20 +111 +39 -11 -69 +51 +134 -60 +76 -75 -119 -92 +25 +96 +17 -87 -141 -115 +122 +86 -23 +33 +85 +105 +110 -28 +67 +94 +90 +13 -132 +41 +133 -140 +73 -27 -3 +104 +125 +71 +84 +26 -38 +62 +34 +88 +43 +95 -83 -44 -109 +123 -68 +57 -128 -12 +66 -56 +7 -14 -35 +30 -49 +18 +48 +120 -29 -61 -45 +98 +78 +63 -124 +112 +101 -64 -97 -65 +54 -19 +82 -81 +47 +1 +37 +130 -15 +42 +80 +8 +142 +129 +99 -58 +52 -36 -93 +89 -126 +21 +31 +24 +135 +79'

def GreedySorting(P):
    approxReversalDistance = []
    if len(P) == 0: #check before run 
    	return -1 
    elif len(P) != 0: 
	    for k in range(len(P)):
	        while P[k] != k + 1: #first check 
	            P = k_SortingRev(P, k)
	            approxReversalDistance.append(list(P))
	        #elif P[k_1] != -(k + 1):
	        	#P = k_SortingRev(P, k)
	        	#approxReversalDistance.append(list(P))
	    return approxReversalDistance


def k_SortingRev(P, k):
    k_1 = k
    while P[k_1] != k + 1 and P[k_1] != -(k + 1):
        k_1 += 1
    P[k:k_1+1] = list(map(lambda l: -l, P[k:k_1+1][::-1]))
    return P


if __name__ == "__main__":
	P = [int(x) for x in P.split(' ')]
	for line in GreedySorting(P):
		print(' '.join(['+'  + str(x) if x > 0 else str(x) for x in line])) # - is already written

