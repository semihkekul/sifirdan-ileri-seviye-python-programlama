print([x**2 for x in range(10) if x%3 == 0])
# [0, 9, 36, 81]

print([x if x%2==0 else 'ODD' for x in range(10)])
#  [0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD']

print([(x,y) for x in range(3) for y in range(3)])
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]