
tuple1 = (1, 'iki', 3)
tuple2 = 1, 'iki', 3

print(tuple1, "\n", tuple2)
# (1, 'iki', 3) 
#  (1, 'iki', 3)

# 
# tuple1[0] = 'bir'
#     tuple1[0] = 'bir'
#     ~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

print(tuple2.index(3))
# 2

print(tuple1 + tuple2)
# (1, 'iki', 3, 1, 'iki', 3)