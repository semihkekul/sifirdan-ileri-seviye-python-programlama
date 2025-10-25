x, y = 5, 25

x = y
y = 10

print(x,y)
# 25, 10

###################
# reference types #
###################
L1 = [1 , 2, 3, 4, 5]
L2 = ['a', 'b']

L1 = L2 

L2[1] = 'bbbb'

print(L1 , L2)
# ['a', 'bbbb'] ['a', 'bbbb']
