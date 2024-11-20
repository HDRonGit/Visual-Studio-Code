import os
os.system('cls')

animals = ['cat', 'dog', 'rabbit', 'hamster', 'lion']
for i in animals:
    print(i)
    
animals.remove ('lion')
# animals.pop (4)
animals.append ('tiger')
animals.append ('elephant')
print(animals)
