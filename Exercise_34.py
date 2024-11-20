import os
os.system('cls')

age = input("How old are you? ")
license = input("Do you have a license? Enter yes or no: ") # under 21, not possible for kid to have license

if (license == "yes" or license == "no"):
    print("valid entry")
else:
    print("read it again please and provide a yes or a no answer")
    
age = int(age)

if (age >= 21 and license == "yes"):
    print("You're an adult with license")
elif (age >= 21 and license == "no"):
    print("You're an adult with no license")
elif (age < 21 and license == "yes"):
    print("Stop lying about your license or age")
else:
    print("You're a kid")