import sys

x = 'LANRHRMQYLSKCFNIWFHNPTEFNWLGNEKRAHAALTRQSECIHNGEWWYITEKHAEPIAIQEKLEFENDKNQHFENSIFYHEKYHGQAEVGVDLIFEEQTMYLKSKRCRHYMSHMINQVLPDGTQWGRFEFRRIARLCVVWTAVKLQMSGCFMRSSLWHDCQVKLIECWFCYPGLSICTDGADCMIMNENHDPPMVRMNLEIDIRWFYGKDNTAHYQKKPCGCHFWSVQAGAGLYAHSMNYGMVVAFDILQLFNATDQTTQGPIRLTVYLMRIGSNVEQQLVAYVFFLWPEGMFTRHFLTRMCGNCEHGRMHPGRTAQWKVAQMKEDKAGPSKIAMEHWKFAMRPQIAFARWKSGYDWRRCWVADVPLAIAKTSYIKPRCVKAVWPNVHQTQYGSWRPRVKMNCCASSGRATTPDCNIFDIEIEQCSPTMTAPWFMWVQYRFTHGGVIMPHMNVWMCNSMSIIRKGFPAKWEAYLVAWTTFYNNHLGMYSRISGISGEMSTARFEGCIEVFLIDLMEMDYGKRETWETQIWLFVHWKYDQRTHQLQPEDERRHRNHNGSKDGRLKHDYSYLSRMIPRAINSCGQIFNEVTPKHQNYQGIYPNPKQEGRYVCSKIECGRMDGAEHNWRGMMGGASYMFPDWWGGSRTAHVIWQKIPVMVNPHKIWANANVSKTTLCYVHCHEQEREHHLKNEQFYISKLCIWGWRMGVWQVYQNCHWLREKNQYFVPDNKGKCWCNLMIFRWFCKGKCFGELCSYAAAERGPVEVENMMNNFMPWICASGI'
y = 'LARMPQARHRMGYLSKCTGDNIFTFNFHNPTEFNWLDNEMRYDSMTIGSECFYNNRSADALTRQGWLINGEWWYIHGQQLEKHAKPFMKTKLIQEKLEMMENKYIGQAEVGVDLIREKQTMDSAIICMLCVEGQVQPDGTQWGRFEFRRIARLVVWTVRPMGSHLFQSHALLCCVVIECWFCYPGLSFCTDLKRYWIWADCMIMNEWFHRWCPPMVRMNLEIDYGKDNTRFWNTYYHYQKKPCASCTCTFSSHSNYGMVVSAFDISQLFNAVMDQTTQGPFRLTVYLMRIGSNVWQQDPMPSLELWGSCYIMAYRFFLWPSNARDYGDDGMKTRHFKIVANTRMCGNCSHGRMQTPSHPAQMKAVHTYWEDHFAWEHWKFAMRPQIGGEADPKWKSGYQWWRSWVADMVTRNPQFIAKTSYIKCKPMGICYEVKAQWPNLHQSQGRATTPDCWIFSPTMTAWHGDRRRQCFYFFGGVICNSMSIIRPAKWEAYNVAWTMCVYNSRISGISGEEMTARDEQCIQVFLIFLMEMDYGKREDWEIQIWLFVHWKYPDCARKGAPEDERRHRNGHVPGLIVHKDGRLKYIPNFADANLSRMHYHCLPRAINSAHHQRHDCYQGRYPHPPQEGRYECNKYECGRCPYTKQVCRSYMFFDMQYQGHRIWQKITCRRFNTHAMVNGDTNSDICWKPKINANFHCDEQERISKLCIWMVWRMGVWFHWLREKNQYFIFDCCPDNKGKMCLPWCNLMIRWFCKMEDCTWFCCFGEDCSYAAAERGKCARVVEVENMMNLNTFMPWICAWGI'

def BLOSUM62():
	file = 'BLOSUM62.txt'
	with open(file) as f:
		lines = f.read().splitlines()
	matrix = []
	readlines = lines[0].split()
	for i in range(1,len(lines)):
		matrix.append(list(map(int,lines[i][1:].split())))
	return matrix,readlines

def GlobalAlignment(x,y,indelpenalty=5):
	matrix,readlines = BLOSUM62()
	s = [[0 for toj in range(len(y)+1)] for toi in range(len(x)+1)]
	backtrack = [[0 for toj in range(len(y)+1)] for toi in range(len(x)+1)]
	s[0][0] = 0 
	for i in range(1,len(x)+1): #first col
			s[i][0] = -i * indelpenalty
	for j in range(1,len(y)+1): #first row
			s[0][j] = -j * indelpenalty
	for i in range(1,len(x)+1):
		for j in range(1,len(y)+1):
			scoretrack = matrix[readlines.index(x[i-1])][readlines.index(y[j-1])]
			deletion = s[i-1][j] - indelpenalty
			insertion = s[i][j-1] - indelpenalty
			match = s[i-1][j-1] + scoretrack
			s[i][j] = max(s[i][j-1] - indelpenalty, s[i-1][j] - indelpenalty, s[i-1][j-1] + scoretrack)
			if s[i][j] == deletion:
				backtrack[i][j] = "south" 
			elif s[i][j] == insertion :
				backtrack[i][j] = "east"
			else : #mis/match
				backtrack[i][j] = "southeast" 

	return s[len(x)][len(y)],backtrack

def Backtrack_edge(backtrack,x,y):
	i = len(x)
	j = len(y)
	track = []
	while i > 0 or j > 0:
		if backtrack[i][j] == "south" :
			track.append([x[i-1],'-'])
			i -= 1
		elif backtrack[i][j] == "east" : 
			track.append(['-',y[j-1]])
			j -=1
		else :
			track.append([x[i-1],y[j-1]])
			i -= 1
			j -= 1
		track.reverse()
		alignment1 = []
		alignment2 = []
		for i in range(len(track)):
	        alignment1.append(track[i][0])
        	alignment2.append(track[i][1])
	return "".join(alignment1), "".join(alignment2)
if __name__ == '__main__':
	score,backtrack = GlobalAlignment(x,y,indelpenalty=5)
	alignment1,alignment2 = Backtrack_edge(backtrack,x,y)
	print('\n'.join([str(score),alignment1,alignment2]))