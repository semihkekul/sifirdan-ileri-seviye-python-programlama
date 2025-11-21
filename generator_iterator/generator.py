def cube():
    for i in range(5):
        yield i ** 3

print(cube()) # <generator object cube at 0x000002465CE44DC0>       

iter = cube()

print(next(iter)) # 0
print(next(iter)) # 1
print(next(iter)) # 8


for i in cube():
    print(i)
'''
27
64
'''    

gen = (i**3 for i in range(5))
print(gen) # <generator object <genexpr> at 0x0000026ED193F780>

for i in gen:
    print(i)
'''
0
1
8
27
64
'''