class MyClass:
    def __str__(self):
        return "my class str()"
    
    def __len__(self):
        return 12345

    def __del__(self):
        print("deleted")

my = MyClass()

print(str(my))      
# my class str()  

print(len(my))      
# 12345

del my
# deleted