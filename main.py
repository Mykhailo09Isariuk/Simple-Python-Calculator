import math

num_1 = float(input("Enter first number >>>   "))
num_2  = float(input("Enter second number >>>  "))
action = str(input("Enter action >>>  "))

if action == '+':
    answ = num_1 + num_2
    print(f'Answer: {answ}')

elif action == '-':
    answ = num_1 - num_2
    print(f'Answer: {answ}')

elif action == '*':
    answ = num_1 * num_2
    print(f'Answer: {answ}')

elif action == '/':
    answ = num_1 / num_2
    print(f'Answer: {answ}')

elif action == '%':
    answ = num_1 % num_2
    print(f'Answer: {answ}')