numbers = [1, 10, 5, 16, 4, 8, 10, 9]
letters = ['m', 'e', 't', 'e', 'a', 'r', 'z', 'u'] 

print(max(numbers), min(numbers))
# 16 1

print(max(letters), min(letters))
# z a

#splicing

print(numbers[3:6])
# [16, 4, 8]

print(numbers[:3])
# [1, 10, 5]

print(numbers[4:])
# [4, 8, 10, 9]

numbers.append(49)
print(numbers)
# [1, 10, 5, 16, 4, 8, 10, 9, 49]

numbers.insert(3, 888)
print(numbers)
# [1, 10, 5, 888, 16, 4, 8, 10, 9, 49

numbers.insert(-1, 2222)
print(numbers)
# [1, 10, 5, 888, 16, 4, 8, 10, 9, 2222, 49]

print(numbers.pop())
# 49
print(numbers)
# [1, 10, 5, 888, 16, 4, 8, 10, 9, 2222

print(numbers.pop(0))
# 1

numbers.remove(888)
print(numbers)
# [10, 5, 16, 4, 8, 10, 9, 2222]

print(letters.count('e'))
# 2

print(letters.clear())
print(letters)
# []