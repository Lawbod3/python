import math
user = int(input("Enter a three digit number: "))
while user < 0 or user > 1000:
    print("Invalid input")
    user = int(input("Enter a three digit number: "))

extraction1 = math.floor(user / 100)   
extraction2 = math.floor(user / 10 % 10)
extraction3 = math.floor(user % 10)

result = extraction1 + extraction2 + extraction3
print(result)        