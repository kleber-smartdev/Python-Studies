inputFile = open ('myimage.jpg', 'rb')
outpuFile = open ('myoutputimage.jpg', 'wb')

msg = inputFile.read(10)

while len(msg):
	outpuFile.write(msg)
	msg = inputFile.read(10)

inputFile.close()
outpuFile.close()