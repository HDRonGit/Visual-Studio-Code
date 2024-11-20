import os

# Clear the terminal screen
os.system('clear')

# Define a list of house types
houses = ['appartment', 'townhouse', 'house', 'mansion', 'castle'] # 1x5

# Print the first and last elements of the list
print(houses[0])  # Output: appartment
print(houses[-1]) # Output: castle

# Print the length of the list
print(len(houses)) # Output: 5

# Iterate through the list and print each element
for i in houses:
    print(i)

print("- - - -")

# Print slices of the list
print(houses[0:3]) # Output: ['appartment', 'townhouse', 'house'] [start:stop]
print(houses[:3])  # Output: ['appartment', 'townhouse', 'house'] [:stop]
print(houses[3:])  # Output: ['mansion', 'castle'] [start:]

# Print elements with a step
print(houses[::2]) # Output: ['appartment', 'house', 'castle'] [start:stop:step]

print("- - - -")

# Reset the list of house types
houses = ['appartment', 'townhouse', 'house', 'mansion', 'castle'] # 1x5
print(houses)

# Change the value of the element at index 1
houses[1] = "barn"
print(houses) # Output: ['appartment', 'barn', 'house', 'mansion', 'castle']

# Append an element to the end of the list
houses.append("igloo")
print(houses) # Output: ['appartment', 'barn', 'house', 'mansion', 'castle', 'igloo']

# Extend the list with multiple elements
houses.extend(["penthouse", "tent"])
print(houses) # Output: ['appartment', 'barn', 'house', 'mansion', 'castle', 'igloo', 'penthouse', 'tent']

# Insert an element at a specific index
houses.insert(2, "yurt")
print(houses) # Output: ['appartment', 'barn', 'yurt', 'house', 'mansion', 'castle', 'igloo', 'penthouse', 'tent']

# Remove the last element from the list
houses.pop()
print(houses) # Output: ['appartment', 'barn', 'yurt', 'house', 'mansion', 'castle', 'igloo', 'penthouse']

# Remove the element at index 2
houses.pop(2)
print(houses) # Output: ['appartment', 'barn', 'house', 'mansion', 'castle', 'igloo', 'penthouse']

# Remove the element "house" from the list
houses.remove("house")
print(houses) # Output: ['appartment', 'barn', 'mansion', 'castle', 'igloo', 'penthouse']

# Clear all elements from the list
houses.clear()
print(houses) # Output: []

# Reverse the list
houses.reverse()
print(houses) # Output: ['penthouse', 'igloo', 'castle', 'mansion', 'barn', 'appartment']

# Sort the list
houses.sort()
print(houses) # Output: ['appartment', 'barn', 'castle', 'igloo', 'mansion', 'penthouse']
