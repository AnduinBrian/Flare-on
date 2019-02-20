def DeriveVallocType(r,c):
	temp = ~(r*30+c)
	return temp & 0xFFFFFFFF

def AllocateMemory():
	VALLOC_TYPE = [4294966400,4294966657,4294967026]
	for i in range(0,30):
		for j in range(0,30):
			flag = True
			r = i+1
			c = j+1
			if DeriveVallocType(r,c) in VALLOC_TYPE:
				flag = False
				print "flag = false: \nrow: {0} - col: {1}\n".format(r,c)

AllocateMemory()
