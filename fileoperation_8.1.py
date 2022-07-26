f = open ('myfile.txt', 'r')

firstline = f.readline ()
seconline = f.readline ()
print (firstline, end = '')
print (seconline, end = '')

#Using LOOP to read all document
f = open ('myfile.txt', 'r')

for line in f:
	print (line, end = '')

#Writing data on file
f = open ('myfile.txt', 'a')

f.write ('\nThis setence will be appended.')
f.write ('\nPython is Fun!')

f.close ()