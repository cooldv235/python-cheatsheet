# A list is a collection which is ordered and changeable. Allows duplicate members

# Create a list
numbers = [1,2,3,4,5]
fruits = ['Apples','Oranges','Grapes','Pears']

# Or Use a constructor
# numbers2 = list((1,2,3,4,5))

# Get a value
print(fruits[1])

# Get a length
print(len(fruits))

# Append to list
fruits.append('Mangoes')

# Remove from list
fruits.remove('Grapes')

# Insert into a specific postion in list
fruits.insert(2,'Strawberries')

# Change value
fruits[0] = ' Blueberries'

# Remove with pop
fruits.pop(2)

# Reverse list
fruits.reverse()

print(fruits)

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)
print(fruits)