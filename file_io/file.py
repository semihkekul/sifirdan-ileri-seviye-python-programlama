file = open("file_io/newfile.txt","w", encoding="utf-8")
file.write("deneme\n")

file.close()

file = open("file_io/newfile.txt", "r")
print(file.read())
# deneme
file.close()

file = open("file_io/newfile.txt","a")
file.write("ekleme")
file.close()

file = open("file_io/newfile.txt", "r")
print(file.read())
# deneme
# ekleme

file.seek(0)
print(file.read(3))
# den
print(file.read(6))
# eme
# ek

file.seek(0)
print(file.readline())
# deneme
#

print(file.readline())
# ekleme
#

file.seek(0)
print(file.readlines())
#['deneme\n', 'ekleme']
file.close()

print("========")
with open("file_io/newfile.txt", "r") as file:
    print(file.read())
    # deneme
    # ekleme

    file.seek(3)
    print(file.tell())
    # 3

    print(file.read())
    # eme
    # ekleme
