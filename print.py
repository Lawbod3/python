setTaker = float(input('Enter the amount of number you want to calculate: '))

smallest = 2**31 - 1
largest = -2**31 
total = 0
average = 0
range = 0
counter = 0

while counter < setTaker:
	userInput = float(input('Enter a number: '))

	if userInput > largest:
		largest = userInput

	if userInput < smallest:
		smallest = userInput

	total += userInput
	average = total / setTaker
	range = largest - smallest
	counter += 1 

print('Total is: ',  total)
print('Largest is: ', largest)
print('Smallest is: ', smallest)
print('Average is: ', average)
print('Range is: ', range)


