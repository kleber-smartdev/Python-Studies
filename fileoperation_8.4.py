inputFile = open ('myfile.txt', 'r')
outpuFile = open ('myoutputfile.txt', 'w')

msg = inputFile.read(10)

while len(msg):
	outpuFile.write(msg)
	msg = inputFile.read(10)

inputFile.close()
outpuFile.close()