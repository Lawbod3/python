import random
sum = 0
for count in range (2):
    number = random.randrange(1, 100)
    sum += number
    print(number)

user_sum = int(input('Enter the sum of the two digit above: '))	
if user_sum == sum:
    print(True)
else:
    print(False) 