import os

print(os.name) # nt

print(os.getcwd()) # D:\dev\sifirdan-ileri-seviye-python-programlama

# os.makedir("new_dir")
# os.makedirs("new_dir/new_dir2")

for f in os.listdir():
    print(f)
'''
.git
.gitignore
advanced_modules
basics
Data structures
error_handling
file_io
functions
...
'''    

print(os.path.abspath("os.py")) # D:\dev\sifirdan-ileri-seviye-python-programlama\os.py
