def Update(string, i, l):
	

	temp = []
	for x in range(i, l+i):
		temp.append(string[x])


	for y in range(i, l+i):
		string[y] = temp[l-1-(y-i)]

	return (string)


def Query(string,i,l):
	mlen = 0
	length = 0
	for x in range (i, l+i):
		if string[x]==1:
			mlen +=1
			if x == (l+i)-1:
				if (mlen>length):
					length=mlen
		elif string[x]==0:
			if (mlen>length):
				length = mlen
			mlen=0


	return (length)


firstLine = raw_input()
O = firstLine.split(' ')[1]
testString = raw_input()
strung = list(map(int, testString))

for x in range(0, int(O)):
	line = raw_input()
	spline = line.split(' ')
	func = int(spline[0])
	i = int(spline[1])
	l = int(spline[2])

	if func == 1:
		strung = Update(strung, i,l)
	if func == 2:
		print(Query(strung, i,l))