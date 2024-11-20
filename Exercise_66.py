import os
os.system('cls')

vehicles = ['car', 'bike', 'bus', 'trian']
for i in range(len(vehicles)):
    l = len(vehicles[i])
    if l >= 4:
        vehicles[i] = 'truck'
        
print(vehicles)
    

