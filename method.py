import math
def get_palindrome(user):
    extraction1 = math.floor(user / 100)   
    extraction2 = math.floor(user / 10 % 10)
    extraction3 = math.floor(user % 10)

    result = extraction1 + extraction2 + extraction3
        return result        