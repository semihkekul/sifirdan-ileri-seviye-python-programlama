fruits = {'orange', 'apple', 'banana'}

for f in fruits:
    print(f)
print('')
# orange
# banana
# apple

fruits.add('cherry')

for f in fruits:
    print(f)
print('')
'''
cherry
orange
apple
banana
'''   

fruits.update(['apple', 'mango'])

for f in fruits:
    print(f)
print('')

'''
mango
apple
cherry
orange
banana
'''

fruits.remove('mango')
for f in fruits:
    print(f)
print('')
'''
orange
cherry
apple
banana
'''

fruits.discard('apple')
for f in fruits:
    print(f)
print('')
'''
orange
cherry
banana
'''

fruits.pop()
for f in fruits:
    print(f)
print('')
'''
orange
cherry
'''


liste = [1,2,3,4,5,3,3,6,7]
print(set(liste))
# {1, 2, 3, 4, 5, 6, 7}

