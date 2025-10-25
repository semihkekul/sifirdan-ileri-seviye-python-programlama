message = "Hello there. My name is Semih Kekul"

print(message.upper())
# HELLO THERE. MY NAME IS SEMIH KEKUL

print(message.lower())
# hello there. my name is semih kekul

print(message.title())
# Hello There. My Name Is Semih Kekul

print(message.capitalize())
# Hello there. my name is semih kekul

message2 = "            Hello Tehere. My name is Semih Kekul" # space in the beginning
print(message2.strip())
# Hello there. My name is Semih Kekul

print(message.split())
# ['Hello', 'there.', 'My', 'name', 'is', 'Semih', 'Kekul']

print(message.split('.'))
# ['Hello there', ' My name is Semih Kekul']

splitted = message.split()
print(' % '.join(splitted))
# Hello % there. % My % name % is % Semih % Kekul

print(message.find("Semih"))
# 24

print(message.find("Semihk"))
# -1

print(message.startswith("H"))
# True

print(message.endswith("H"))
# False

print(message.replace("Semih", "Mete"))
# Hello there. My name is Mete Kekul

print(f"[{message.center(100,'*')}]")
# [********************************Hello there. My name is Semih Kekul*********************************]