message1 = "Global Variable"

def myFunction ():
	print ("\nINSIDE THE FUNCTION")
	#Global variable are accessible inside a function
	print (message1)

	#Declaring a local variable
	message2 = "Local Variable"
	print (message2)
'''
Calling the function
Note that myFunction bla bla bla
'''
myFunction ()

print ("\nOUTSIDE THE FUNCTION")

#Global variables are accessible outside the function
print (message1)

#Local variables are NOT accessible outside function
print (message2)