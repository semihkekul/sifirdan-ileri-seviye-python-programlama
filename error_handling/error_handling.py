try:
    print(10/5)
except Exception as ex:
    print("An error occureed", ex)    
else:
    print("hersey yolunda")    

# 2.0
# hersey yolunda

try:
    print(10/0)
except Exception as ex:
    print("An error occureed", ex)    
else:
    print("hersey yolunda")    

# An error occureed division by zero    