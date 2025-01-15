import math
def get_palindrome(user):
    extraction1 = math.floor(user / 100)   
    extraction2 = math.floor(user / 10 % 10)
    extraction3 = math.floor(user % 10)

    result = extraction1 + extraction2 + extraction3
    return result

def get_multiply(number, number2): 
    sum = 0
    for  count in range (number2):
        sum += number 
    return sum     