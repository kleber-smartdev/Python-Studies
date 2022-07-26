try:
	userInput1 = int (input ("Please enter a number: "))
	userInput2 = int (input ("Please enter another number: "))
	answer = userInput1/userInput2
	print ("The answer is ", answer)
	myFile = open ("missing.txt", 'r')

except ValueError:
	print ("Error: You did not enter a number")

except ZeroDivisionError:
	print ("Error: Cannot divide by zero")

except Exception as e:
	print ("Unknown error: ", e)
