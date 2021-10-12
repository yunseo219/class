import sys

str1 = 'ATWCEGQCEHCDLYFSEESSSQNYKCHRYQYPTCQYCNNEIRGMHFMVMYHWHAKHYDQTWVAIGVGMMHPLRPPREPRQHTVGTLDWRCKRCDYPHSAYQNNNGYFYHTTIRDLAMTCMWRQIFDLTFWISHPTALKAPKVDISWTFFLAEEDCCYDTWEEIMVAGVDFVDEYAHSVYHFKGNVPNLNKCGECDRFDSAYNTSWIMDIRFSFCRHHKVAENEWTTMYCRSDCPLALYWCEWPFESYPMYQSNCEVFNNEFRMNQDMPGWVRGWWKHIMVWFGMTYFEHQYAQIDQWHYCIWNMDWYGLPQFAGQQHPWTWKITVISYWMMHLRGDSAPDMCTYRRTWVAWNFMFSAHEFIAQNTWFMICEVEEMRLDTEASRNVFRTTMRIASHFSELVYAPAMITNHYMIELPSIALMLYCHDGDPTNDCMGNFFDFYYGKHGNPEAINWSQQLYCNIRMNRIHCLEANMQSRSEKVECYLSCFEIIDDWMIPLHLLQGNFFAMNMGHRFIQNTNRGINVIVEAQHLTNGTMFKNMCKNSSRVHLRKKASEKVDTHYNFLVGEGKEACPMWGNWMGRQYLGTPWIFPMWLIAWKVNMYAPRQYVYKKFCIVGQTKKHIIPFNAQEEPHVKLCNGLLMCDNMSTMWLLDTMGEYTFPMNRMKAQGKPQSTHAPHYRFLALQVSYHVRTTKWVDCMLFLRVIVLFAQMYHMYAYYTLTLNDNKKLMARAPVHPYYYLEDRPNREKDWTHAIGSHMGQLRHLMRWDMRAGFSKPWDEKQHHFFQTKWPQVHQLEKVGMQEVDFETFRVGLCTPREYSFLQTDYVNTGEYYKFHGSITWPLACERVFAVEIQRRGVWETHFMFEFIDANWVKECWWTDIWFQLSSLEMYIHLYYIRKQKLSF'
str2 = 'YDLLQHRQSSCFWTIFQSKRLCRFSFALEWFCMENHLFQDAGNGLWCTVWMRATHLMQDWEAMKQYGFSYLFPVINIPKDGFGFLSINLFIQWAPDLEFMFPKCPMVYLTKFWFKVYARDWNKDEVQASKSLMIAFMENMNHSLCRSLCPQHAYYYVFGRNVLYWYATHPVKGQETLWKKPQPMKSGMAACNHGMHSFKQECQLIAQEVYMYEMKNTWQDMINPDFQSAHQYAHMCKEVRNDKRYFEHGPWAQIDQWHYCIDNYIIQICLPQKDAGQQHPWTWKIFNAMSIAVISFKQRAGTRGDSLCHCPDMCTYRRDWVAQLLTFPDGNDMFSTQIHEFIAQNICPPEEMRLDTEASVQDNVKRTTMRIASHQSELPYIFWWNGYYMIELPSIAPTNDCMQDSSMFQFFDFYYGKHGNPENISPAKWSQQLHCNIYMNRIHCLEVDLNTSAINMQSRSYNDIPLIVECYLWHYAEACFEIILEQDCGHDQKISLQGNFFMMNMGHRFIQNAPHFINHCNRGMIVEAVHLTNGTMFKNMCKNSNYQGSEYVDTHYNFLVGEGLEACPMWGNWMGWEFPHHVLMVGSKMTPWIFPMWLIDHQGKEWKVNMYADRQYKYKVLQMLKVFCIVGQTKKHIIPFAAQEEPHVKLCVGLLMCDNYSTMWVGARHEHSLYVRDSYGFSSQEFMPRATVLSLYSTTRQLWPFPTASRGMQTKEMSYTESTHECMTDAEDSRGMPMFMNNIGMFAFKENECPNQKKLTKNWTKKCWGISFHWWQLMVPIDISFHEAPCWQSLVFAGHSAEAMGFSNYQCIAPVSTWCIPNCLWCGLTYTGNVYREHGWPDYYNVTKQPNICINVKWKTEAGEVVKRCHCKRGQQDVYLMPSFAMEQLPWKISTIICAKFPFDDINCTMEYDNIYELYGWPTSYCDHPMAGNSSCCILRACDRTNNAGMFYTLSSGDWH'

def Score():
	file = 'PAM250.txt'
	with open(file) as f:
		lines = f.read().splitlines()
	score = []
	readlines = lines[0].split()
	for i in range(1,len(lines)):
		score.append(list(map(int,lines[i][1:].split())))
	return score,readlines

def LocalAlignment(x,y,indelpenalty=5):
	score,readlines = Score()
	s = [[0 for toj in range(len(y)+1)] for toi in range(len(x)+1)]
	backtrack = [[0 for toj in range(len(y)+1)] for toi in range(len(x)+1)]
	s[0][0] = 0 
	for i in range(1,len(x)):
		for j in range(1,len(y)):
			scoretrack = score[readlines.index(x[i-1])][readlines.index(y[j-1])]
			deletion = s[i-1][j] - indelpenalty
			insertion = s[i][j-1] - indelpenalty
			match = s[i-1][j-1] + scoretrack
			s[i][j] = max(0, s[i][j-1] - indelpenalty, s[i-1][j] - indelpenalty, s[i-1][j-1] + scoretrack)
			if s[i][j] == 0: 
				backtrack[i][j] = "NO"
			elif s[i][j] == deletion:
				backtrack[i][j] = "south" 
			elif s[i][j] == insertion:
				backtrack[i][j] = "east"
			else : #mis/match
				backtrack[i][j] = "southeast" 

	return s,backtrack

def Backtrack_max(s,backtrack,x,y): #highest scoring
	track = [[],[]]
	maxrow = [max(row) for row in s]
	maxcol = [max(col) for col in s]
	maxscore = max(maxcol)
	i = maxrow.index(maxscore)
	j = maxcol.index(maxscore)
	while i != 0 or j != 0:
		if backtrack[i][j] == "NO":
			break
		elif backtrack[i][j] == "south" :
			track[0].append(x[i-1])
			track[1].append('-')
			i -= 1
		elif backtrack[i][j] == "east": 
			track[0].append('-')
			track[1].append(y[j-1])
			j -=1
		else :
			track[0].append(x[i-1])
			track[1].append(y[j-1])
			i -= 1
			j -= 1

		alignment1 = ''.join(track[0][::-1])
		alignment2 = ''.join(track[1][::-1])
	return maxscore, alignment1, alignment2

if __name__ == '__main__':
	score,backtrack = LocalAlignment(str1,str2,indelpenalty=5)
	maxscore,alignment1,alignment2 = Backtrack_max(score,backtrack,str1,str2)
	print('\n'.join([str(maxscore),alignment1, alignment2]))