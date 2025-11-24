import re

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

print(re.findall("Python", str)) 
# ['Python', 'Python']

print(re.split(" ", str)) # same as print(re.split("\s", str)) meaning " " == "\s"
# ['Python', 'Kursu:', 'Python', 'Programlama', 'Rehberiniz', '|', '40', 'saat']

print(re.sub("\s", "-", str)) 
# Python-Kursu:-Python-Programlama-Rehberiniz-|-40-saat

match = re.search("Python", str)
print(match.span(), match.start(), match.end())
# (0, 6) 0 6 

print(re.findall("[abc]", str)) # finds all the characters in []
# ['a', 'a', 'a', 'b', 'a', 'a']

print(re.findall("[a-e]", str)) # finds all the characters between a-e
# ['a', 'a', 'a', 'e', 'b', 'e', 'a', 'a']

print(re.findall("[1-5]", str)) # finds all the characters between 1-5
# ['4']

print(re.findall("[0-395]", str)) # finds all the characters in [012395] meaning 0-3 and 9 and 5


print(re.findall("[^abc]", str)) # finds all the characters not in []
# ['P', 'y', 't', 'h', 'o', 'n', ' ', 'K', 'u', 'r', 's', 'u', ':', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'g', 'r', 'm', 'l', 'm', ' ', 'R', 'e', 'h', 'e', 'r', 'i', 'n', 'i', 'z', ' ', '|', ' ', '4', '0', ' ', 's', 't']

print(re.findall("[^0-9]", str)) # finds all the characters which are not numbers
# ['P', 'y', 't', 'h', 'o', 'n', ' ', 'K', 'u', 'r', 's', 'u', ':', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'l', 'a', 'm', 'a', ' ', 'R', 'e', 'h', 'b', 'e', 'r', 'i', 'n', 'i', 'z', ' ', '|', ' ', ' ', 's', 'a', 'a', 't']

print(re.findall("..", str)) 
'''
.. =>   a   : No Match
        ab  : 1 match
        abc : 1 match
        abcd: 2 match  
'''
# ['Py', 'th', 'on', ' K', 'ur', 'su', ': ', 'Py', 'th', 'on', ' P', 'ro', 'gr', 'am', 'la', 'ma', ' R', 'eh', 'be', 'ri', 'ni', 'z ', '| ', '40', ' s', 'aa']

print(re.findall("s..t", str)) 
# saat

print(re.findall("^P", str))
'''
Checks if the string starts with a :
^a =>   a   : 1 match
        ab  : 1 match
        abc : 1 match
        baaa: No match  
'''
# ['P']

print(re.findall("t$", str))
'''
Checks if the string ends with a :
a$ =>   a   : 1 match
        ba  : 1 match
        aab : No Match  
'''
# ['t']

print(re.findall("saat$", str))
# ['saat']

print(re.findall("sa*t", str)) # * checks if a character is there 0 or more times
'''
ma*n => mn      : 1 
        man     : 1
        maaan   : 1
        main    : No
'''
# ['saat']

