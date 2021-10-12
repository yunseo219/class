def BLOSUM62():
    file = 'BLOSUM62.txt'
    with open(file) as f:
        lines = f.read().splitlines()
    matrix = []
    readlines = lines[0].split()
    for i in range(1,len(lines)):
        matrix.append(list(map(int,lines[i][1:].split())))
    return matrix,readlines

def middle_column_score(v, w, scoring_matrix, sigma = 5):
    '''Returns the score of the middle column for the alignment of v and w.'''

    # Initialize the score columns.
    S = [[i*j*sigma for j in xrange(-1, 1)] for i in xrange(len(v)+1)]
    S[0][1] = -sigma
    backtrack = [0]*(len(v)+1)

    # Fill in the Score and Backtrack matrices.
    for j in xrange(1, len(w)/2+1):
        for i in xrange(0, len(v)+1):
            if i == 0:
                S[i][1] = -j*sigma
            else:
                scores = [S[i-1][0] + scoring_matrix[v[i-1], w[j-1]], S[i][0] - sigma, S[i-1][1] - sigma]
                S[i][1] = max(scores)
                backtrack[i] = scores.index(S[i][1])

        if j != len(w)/2:
            S = [[row[1]]*2 for row in S]

    return [row[1] for row in S], backtrack


def MiddleEdge(v, w, scoring_matrix, sigma):
    '''Returns the middle edge in the alignment graph of v and w.'''

    # Get the score of the middle column from the source to the middle.  The backtrack matrix is unnecessary here.
    source_to_middle = middle_column_score(v, w, scoring_matrix, sigma)[0]

    # Get the score of the middle column from the middle to sink.  Reverse the order as the computations are done in the opposite orientation.
    middle_to_sink, backtrack = map(lambda l: l[::-1], middle_column_score(v[::-1], w[::-1]+['', '$'][len(w) % 2 == 1 and len(w) > 1], scoring_matrix, sigma))

    # Get the componentwise sum of the middle column scores.
    scores = map(sum, zip(source_to_middle, middle_to_sink))

    # Get the position of the maximum score and the next node.
    max_middle = max(xrange(len(scores)), key=lambda i: scores[i])

    if max_middle == len(scores) - 1:
        next_node = (max_middle, len(w)/2 + 1)
    else:
        next_node = [(max_middle + 1, len(w)/2 + 1), (max_middle, len(w)/2 + 1), (max_middle + 1, len(w)/2),][backtrack[max_middle]]

    return (max_middle, len(w)/2), next_node



v = 'TWLNSACYGVNFRRLNPMNKTKWDCWTWVPMVMAAQYLCRIFIPVMDHWEFFGDWGLETWRLGIHDHVKIPNFRWSCELHIREHGHHFKTRFLKHNQFTQCYGLMPDPQFHRSYDVACQWEVTMSQGLMRFHRQNQIEKQRDRTSTYCMMTIGPGFTSNGYDPFVTITITPVQEPVENWFTPGGSMGFMIISRYMQMFFYLTRFSDMTYLVGVHCENYVCWNNVAKFLNGNLQGIFDQGERAYHQFVTWHSYSQYSRCSVGRYACEQAMSRVNSKMTWHWPIRDQGHEHFSEQYLSEKRNPPCNPRIGNAGQHFYEIHRIAHRVAMCNWAPQGQHPGGPTPHDVETCLWLWSLCLKGSDRGYVDRPWMFLADQLGEANLTLITMFHGCTRGCLMWFMDWEECVCSYSVVNPRCHGSEQWSVQNLGWRTCDTLISLWEPECDKHNTPPCLHWEFEDHPSQLRPVMMCDKYVQSIPTDAKWAWTYSKDFVISHWLIWTPIKLEECVFPQINRLWGTACNQGSQKIVIQNVWLRPSSFFQERSKCSDSSCILNVGGSNVNITGKETRTHVPILHMHEIDLISTASSGMRHNLILPHGMLMLHMNWHHSTRAMNPYSSLKLIPWTFQVCETDDRDQNVATHVADPCHKGEDQEIRCCKGGVDHQWKGDRMWMMCMPDMNYVKQDQAPSGTCEGACENYPADKDKCYMIFTIVFDYRRCTKKVCIWISGFPVDAFNLISIANAGFFCCWLEPTELKWRRTFYLGKGTQGWMCTFPHRNIIPVIICAGFGRWVQGEVPFRPVAQISAHSSDRRQGHHPPGTNMCHDYGDQYPIKRVGMQVEEDDGASYCDCAADWKLADMYEADHLSIGVIDFTDWIYPKNGGIWSEIIKSHFHWYHWETPQNTVGAFNTIVGINGSDMCIYHGNTQWEFGWCWKWLNHGHMRNQGPCHLGILEGRISKFAQVTSWWWQTKHDKDWSIEPYGRHWGEAGRPYTYNYCWMRWAIVYNHGNVISVELVPFMDEYPGKCNKEDVQFELFSPMQA'
w = 'LWFKFLQCIFQYFKDQQETNCIWTFSPFSEHICQRVCQVYWNWNTPSSRTSDPRELFANSTIHNNRCGEWRYMFYHTRTLVQTAPLMKETLHSDGKHSMYCEQRHFFRSSYLIKVNYDVSHYLELYTFSEIPWKLTTHGWDGFSWFLLVNSCCTFDIDGKCGILSQCGMSRAFRTRQEDAYHFQTSLMHLHLHLHVQEGKHEKADLFAQFYNMLPMHGGTCGRNTEPSDLFDSATMNKYMAEHPASCKACPNVSKECFVYWWSHDFTKKHKLIEFSCGRDTGQTTQRTWNVDENEGGKWIWRFHYFMRAKALQIDPKFKPYWNEPRAIMRPGHVTAAPCICAQHSQNETAVCNRDQMHIHAIEFQQYHSRAFGEVQTWCDIGKENENDFIYEQHWWLVGGTEGMAGVIWKFVCARCRTQDCDFWKTCLTYSAQPMMKVYDTIFYVNSINPWEFEDHPSQCDKCVQSIPTDAKYAICGKFVISHWLYWTPQKFEECVHNNVRCAPMGNRLWGTACMVIQNVWLRPSMGSHFSCILNVGGSNINIQGKETWTHVPILHMHEIDLISTASSGMETCKPCFLSGPTIHMGFSYEIRAQPYSRDYFCMDWMQEADEVDHNRCETVQPTLPLLQQFEWKTSCMGQRWITIFCDHCQIVCFSTFFCVMPTFLPNTSILDKFYCIYLSISWTHYCNVHALGFIMRLHYSYMGWKEHKRMHAWDIGLDELWAQEGIQRAQLWCGDEFEVAKYPEWITEARTAIATRPWFHNCYIKPWWIREKHLWFGKESKLDHGHRGAMFTPVANDNTEWMHHWYMFCWAGSKNRLKRQIKEKLIFIIKFMITEFGLFLMIDYTQCYIAWMWAYTGIACYIDWEKCLKHDLTTTDLGCCVYRLFKWYEVRHRAPPQVNTRLPWSQIPMVAIQCNIVDECKEQWHFSYKASFVVEYLCPGCCTNGNRWQWYQVKETPFMYAFAASIFGFHHENLVVFITGSVTIPNGLFGCIAWTSPKPVQKTPASANTIIAYDKCILMG'
print(MiddleEdge(v,w, scoring_matrix, sigma))

'''
 "def Middle_Edge(v, w, score_matrix, indel_pentalty):\n",
    "    middle_col = len(w) // 2\n",
    "    matrix     = np.full((len(v) + 1, middle_col + 2), 0, 'float')\n",
    "    \n",
    "    for i in range(1, (len(v) + 1)):\n",
    "        matrix[i, 0] = matrix[i - 1, 0] - indel_pentalty\n",
    "    for j in range(1, (middle_col + 2)):\n",
    "        matrix[0, j] = matrix[0, middle_col - 1] - indel_pentalty\n",
    "    \n",
    "    for i in range(1, (len(v) + 1)):\n",
    "        for j in range(1, (middle_col + 2)):\n",
    "            \n",
    "            matrix[i, j] = max(matrix[i - 1, j]     - indel_pentalty, \n",
    "                               matrix[i    , j - 1] - indel_pentalty, \n",
    "                               matrix[i - 1, j - 1] + (score_matrix.at[v[i - 1],w[j - 1]]))\n",
    "            \n",
    "    j = middle_col        \n",
    "    i = int(np.where(matrix[:, j] == np.max(matrix[:, j]))[0])\n",
    "\n",
    "    if max(matrix[i + 1, j + 1], matrix[i + 1, j], matrix[i, j + 1]) == matrix[i + 1, j + 1]:\n",
    "        direction = 'diagonal'\n",
    "        k, l      = i + 1, j + 1\n",
    "        \n",
    "    elif max(matrix[i + 1, j + 1], matrix[i + 1, j], matrix[i, j + 1]) == matrix[i, j + 1]:\n",
    "        direction = 'right'\n",
    "        k, l      = i, j + 1\n",
    "    else:\n",
    "        direction = 'bottom'\n",
    "        k, l      = i + 1, j\n",
    "\n",
    "    print([i, j], [k, l])\n",
    "    return(direction, i)\n",
    "\n",
    "# Test\n",
    "v = 'PLEASANTLY'\n",
    "w = 'MEASNLY'\n",
    "score_matrix   = BLOSUM62\n",
    "indel_pentalty = 5\n",
    "\n",
    "Middle_Edge(v, w, score_matrix, indel_pentalty)"
    '''
