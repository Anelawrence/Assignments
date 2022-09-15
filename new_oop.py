# creating a class named ListOperations
class ListOperations():
  # Default constructor to initialize its values(initializing an empty list).
    def __init__(self):
      # initializing empty list using [] operator or list() function.
        self.givenllist = []
    # Creating three methods inside the class.
    # AddEle: Which appends the given argument to the list using the append function.

    def AddEle(self, eleme):
        return self.givenllist.append(eleme)
    # RemEle: Which removes the given argument from the list using the remove() function.

    def RemEle(self, eleme):
        self.givenllist.remove(eleme)
    # DisplayList: This prints all the elements of the given list.
    # Implement methods for appending, deleting, and displaying list elements,
    # and return the corresponding values.

    def DisplayList(self):
        return (self.givenllist)


# Create an object to represent the class.
listObject = ListOperations()
# taking a choice from the user .
# initializing option as 1
option = 1
while option != 0:
    print("Enter [0] to Exit the program")
    print("Enter [1] to Add element to the given list")
    print("Enter [2] to remove element from the given list")
    print("Enter [3] to print all the elements of the given list")
    option = int(input("Enter some random choice from 0 to 3 = "))
    if option == 1:
      # scanning the element as user input using
      # int(input()) and storing it in a variable
        ele = int(
            input("Enter some random number to be appended to the given list = "))
        listObject.AddEle(ele)
        print("The given list after adding element=",
              ele, '\n', listObject.DisplayList())

    elif option == 2:
        ele = int(
            input("Enter some number which should be removed from the given list = "))
        listObject.RemEle(ele)
        print("The given list after removing the given element=",
              ele, '\n', listObject.DisplayList())

    elif option == 3:
        print("The given list : \n", listObject.DisplayList())
    elif option == 0:
        print("Exit of program")
    else:
        print("The choice entered by user is invalid")

    print()