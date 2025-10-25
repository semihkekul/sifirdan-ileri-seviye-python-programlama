def squ(num): return num ** 2

numbers = [1,2,3,4]

print(list(map(squ, numbers)))
# [1, 4, 9, 16]

print(list(map(lambda x: x**2 , numbers)))
# [1, 4, 9, 16]

print(list(filter(lambda x: x%2==0 , numbers)))
# [2, 4]