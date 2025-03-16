list = []
my_dict = {}

for counter in range (1, 31):
    if counter % 2 == 0:
       list.append(counter)
       my_dict[counter] = counter**3

print(my_dict)