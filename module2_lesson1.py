def max_num(x, y, z):
    if y <= x >= z:
        return x
    elif x <= y >= z:
        return y
    else:
        return z

m = max_num(int(input()), int(input()), int(input()))
print("The maximum number is",m)