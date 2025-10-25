gl1 = 123
gl2 = 456

def func():
    gl1 = 111
    global gl2 
    gl2 = 555

func()
print(f"{gl1} {gl2}")
# 123 555