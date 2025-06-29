#Lambda functions
#Reducing with reduce(): For perdorming a cumulative operation over a list of items, lambda functions can be used with reduce() from the functools module

from functools import reduce

numbers = [1,2,3,4]

add = reduce(lambda x,y: x + y, numbers)

print(add)
