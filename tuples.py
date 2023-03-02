# TUPLES
# IMMUTABLE
# VALUES CANNOT BE CHANGED

fruits = ('apple', 'mango', 'grapes')
fruits2 = ['apple', 'mango', 'grapes']

print(fruits)

fruits2[1] = 'berry'
fruits[1] = 'berry'
print(fruits)
print(fruits2)
print(type(fruits))