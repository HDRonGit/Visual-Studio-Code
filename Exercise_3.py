import os
os.system('cls')

x = 0
first = int(input('Enter first number: '))
second = int(input('Enter second number: '))

x = (first + second)
if first < second:
    y = first % second
    
else:
    y = second % first
    
print('Sum:', x)
print('Defference', y)
