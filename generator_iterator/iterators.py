L = [1,2,3,4,5]

I = iter(L)

print(I) # <list_iterator object at 0x000002194A7A9D20>

print(next(I)) # 1
print(next(I)) # 2

while True:
    try:
        elem = next(I)
        print(elem)
    except StopIteration:
        break    
'''
3
4
5
'''    

class MyNumbers:
    def __init__(self, start, stop):
        self._start = start
        self._stop = stop
        pass
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._start <= self._stop:
            x = self._start
            self._start += 1
            return x
        else:
            raise StopIteration
        
L = MyNumbers(7,13)        
for i in L:
    print(i)
'''
7
8
9
10
11
12
13
'''    