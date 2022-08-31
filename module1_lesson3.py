# "Exponential Calculator"
print("Exponential Calculator")
x = int(input('Enter a number: '))
y = int(input('Enter it power: '))

z = x ** y
if y == 0:
    print("x =", 1)
else:
    print(f"{x} exponential {y} is:",z)