#Lambda functions
#Mapping with map(): Lambda functions can be used to apply transformation to each element in a list

names = ['Alice', 'Bob', 'Charlie']

upper_names = list(map(lambda name: name.upper(), names))

print(upper_names)
