# Catch each error below
# 1)
try:
    if int("tree"):
        print('nope1')
    else:
        raise ValueError("nope1")
except ValueError as err:
    print(err)

# 2)
try:
    if int("15.99"):
        print('nope2')
    else:
        raise TypeError("nope2")
except ValueError as err:
    print(err)

# 3)

my_list = [1, 2, 3, 4, 5]
try:
    if my_list[5]:
        print('nope3')
    else:
        raise IndexError("nope3")
except IndexError as err:
    print(err)

#dumb