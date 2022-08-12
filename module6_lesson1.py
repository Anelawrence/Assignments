# Create a list of integers between 5.5 and 20.5. Write a python program using the lambda function that does the following
a_list = [6, 7, 8, 9, 10, 11,  12, 13, 14, 15, 16, 17, 18, 19, 20]

# count the even and odd numbers in the list.
odd_count = len(list(filter(lambda x: (x%2 != 0) , a_list)))
even_count = len(list(filter(lambda x: (x%2 == 0) , a_list)))  
print("Number of odd numbers in the list is:", odd_count)
print("Number of even numbers in the list is:", even_count)


# Square and cube every number in the list.
print("\nOriginal list of integers:")
print(a_list)
print("\nSquare every number of the list:")
square_nums = list(map(lambda x: x ** 2, a_list))
print(square_nums)
print("\nCube every number of the list:")
cube_nums = list(map(lambda x: x ** 3, a_list))
print(cube_nums)
