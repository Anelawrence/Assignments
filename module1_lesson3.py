# "Exponential Calculator"
print("Exponential Calculator")
x = int(input())
y = int(input())

x = x ** y
if y == 0:
    print("x =", 1)
else:
    print("x =",x)