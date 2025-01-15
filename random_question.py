import random

passed = 0
failed = 0

for count in range(10):
    number1 = random.randrange(1, 100)
    number2 = random.randrange(1, 100)
    result = number1 - number2
    user_result = int(input(f'Solve the equation {number1} - {number2}= '))	
    if user_result == result:
        passed += 1
    else:
        failed += 1

if passed >= failed:
    print(f"Score = {passed}")

else:
    score = 10 - failed
    print(f"Score = {score}")
 
    