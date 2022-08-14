#Generate an array of numbers between 1 and 100 with both numbers included and find the LCM of the even numbers. 
import numpy as np
arr = np.arange(1, 101, 3)
#print(arr)

#Generating even numbers
even_no = list(filter(lambda x: (x%2 == 0), arr))
even_no = np.array(even_no, dtype=np.int64)
print(even_no)

#Generating the LCM
from math import gcd
a = even_no #[100, 200, 150]   #will work for an int array of any length
lcm = 1
for i in a:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)

