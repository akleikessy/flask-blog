import sys
from random import choice
#for debuggin
import pdb

random1 = [1,2,3,4,5,6,7,8,9,10,11,12]
random2 = [1,2,3,4,5,6,7,8,9,10,11,12]

while True:
	print("To exit this game type 'exit'")

	pdb.set_trace()

	num1 = choice(random1)
	num2 = choice(random2)
	answer = input("What is {} times {}? ".format(num2, num1))


	#exit
	if answer.lower() == "exit":
		print('Now exiting game!')
		sys.exit()


	#test = int(choice(random2)) * int(choice(random1))

	#determine if number is correct
	elif int(answer) == int(num2) * int(num1):
		print("correct!")
	else:
		print("wrong!")


