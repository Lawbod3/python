import random

my_turple = ()
sum_odd = 0
sum_even = 0
sum = 0
product_first_five = 1
for number in range(20):
    my_turple = my_turple + (random.randint(1,20),)
print(my_turple)
for number in range(len(my_turple)):
    if number % 2 != 0:
        sum_odd += my_turple[number]
print(sum_odd)
for number in range(len(my_turple)):
    if number % 2 == 0:
        sum_even += my_turple[number]
print(sum_even)
for number in range(len(my_turple)):
    sum += my_turple[number]
print(sum)
smallest = min(my_turple)
print(smallest)
largest = max(my_turple)
print(largest)
total = smallest + largest
first_five = (my_turple[0], my_turple[1], my_turple[2], my_turple[3], my_turple[4])
for number in range(len(first_five)):
    product_first_five *= first_five[number]
print(product_first_five)

