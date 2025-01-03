

numbers = [1,-2,4,-5,20,15]

result =list(map(lambda a : a if a > 0 else None,numbers))

print(result)