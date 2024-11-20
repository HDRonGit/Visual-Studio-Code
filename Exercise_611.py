import os
os.system('cls')

amount_above = 0
amount_under = 0
ages = [10,14,16,19,21,22]
for age in ages:
    if age >= 18:
        amount_above = amount_above + 1
    else:
        amount_under = amount_under + 1
        
print(f"Numbers of ages above 18: {amount_above}")
print(f"Numbers of ages under 18: {amount_under}")