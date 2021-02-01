cipher = "PNUKLYLWRQKGKBE"
key = "EICTDGYIYZKTHNSIRFXYCPFUEOCKRN"
plain = ""
i = 0
for letter in cipher:
	val  = ord(letter)- ord(key[i])
	if(val<0):
		val += 26
	val += ord('A')
	plain += chr(val)
	i+=1
	if(i>=len(key)):
		i=0
		
print(plain)
