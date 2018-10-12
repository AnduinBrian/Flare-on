f = open("rev_challenge_1.dat_secret.encode","rb")
data = f.read()

string1 =""

for i in data:
	num2 = ord(i)
	string1 += chr(((num2>>4) | ((num2 << 4) & 240)) ^ 0x29)
string1 += "\0"
print string1

string2 =""
for j in range(len(string1)/2):
	string2 += string1[j*2+1]
	string2 += string1[j*2]
print string2

string3 =""
for k in range(len(string2)):
	string3 += chr(ord(string2[k])^0x66)
print string3

