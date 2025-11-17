def outer(num1):
    def inner_inc(num):
        return num + 1
    return inner_inc(num1)

print(outer(9))
# 10 