


	
count = 1
highest = 
smallest = 0
average = 0
while count <= 10:
 scoreTaker = int(input('Enter score: '))
 if scoreTaker > highest: 
     highest = scoreTaker
 if scoreTaker < smallest:
    smallest = scoreTaker
total += scoreTaker
average = total / 10
count = count + 1

print('highest is: ', + highest)
print('smallest is: ', + smallest)
print('total is: ', + total)
print('average is: ', + average)
 



	