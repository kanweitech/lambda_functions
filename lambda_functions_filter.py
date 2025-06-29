#Lambda functions
#Filtering with filter(): lambda functions can act as the condition checker

numbers = [1,2,3,4]

even_number = list(filter(lambda x: x % 2 == 0, numbers))

print(even_number)
