#Lambda functions
#Sorting with sorted(): Lambda functions can serve as a quick key generator

people = [
  {
  'name':'Alice', 'age':30
  },
  {
    'name':'Bob', 'age':25
  }
]

sorted_people = sorted(people, key=lambda person: person['name'])

print(sorted_people)
