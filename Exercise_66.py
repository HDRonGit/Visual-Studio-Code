import os
os.system('cls')

vehicles = ['car', 'bike', 'bus', 'trian']

first = (vehicles[0])
count = len(first)
if count > 3:
    vehicles[0] = 'truck'
    
second = (vehicles[1])
count = len(second)
if count > 3:
    vehicles[1] = 'truck'
    
    
thirth = (vehicles[2])
count = len(thirth)
if count > 3:
    vehicles[2] = 'truck'
    
    
    
forth = (vehicles[-1])
count = len(forth)
if count > 3:
    vehicles[-1] = 'truck'
    print(vehicles)
