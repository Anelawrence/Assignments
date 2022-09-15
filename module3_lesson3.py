#  Create a class called “Group_leader” that inherits from the class “Students” that we created in the practical session today. 
# (Initialize the class and let it&nbsp; take an argument of the list of students under the group leader. Let the parent class take care of the other arguments)

class Students:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.fullname = first, " ", last
        self.email = first , last , "@stutern.com"
      
    def fullname(self):
        return self.fullname

    def email(self):
        print(self.email) 


#print(stud_4.fullname)
#print(stud_5.email)


class GroupLeader(Students):
    def __init__(self, first, last):
        self.leader_list = []
        super().__init__(first, last)
        # initializing empty list using [] operator or list() function.
        

    # Define a method that adds students to the list of student under the group leader.
    def add_stud(self, stud):
        return self.leader_list.append(stud)
        #print(self.leader_list)
   
    # Define a method that removes students from the list of students under the group leader.
    def rem_stud(self, stud):
        self.leader_list.remove(stud)

    # display_list: This prints all the elements of the given list.
    # Implement methods for appending, deleting, and displaying list elements,
    # and return the corresponding values.
    def display_list(self):
        print(self.leader_list)

# Create an object to represent the class.
#list_object = GroupLeader(None, None)


# Create 3 more instances of the parent class.
stud_1 = (Students("Bukola", "Dare"))
stud_2 = (Students("Temitope", "Balogun"))
stud_3 = (Students("Mariam", "Alade"))
stud_4 = (Students("Okon", "Joseph"))
stud_5 = (Students("Ahmed", "Musa"))

# Create 2 instances of the sub class.
leader1= GroupLeader('Nne', 'Nne')
leader2= GroupLeader("Nne", "Nne")

new_stud1 = ("Peter", "Obi")
new_stud2 = ("Atiku", "Abubaka")
new_stud3 = ("John", "Jones")
new_stud4 = ("Bola", "Tinubu")

# Add 2 students each to the list of students under the instances of your subclass.
leader1.add_stud(new_stud1)
leader1.add_stud(new_stud2)
leader2.add_stud(new_stud3)
leader2.add_stud(new_stud4)

leader1.display_list()
#print(self.leader_list)

# Remove 1 student each from the list of students under the instances of your subclass
leader1.rem_stud(new_stud2)
leader2.rem_stud(new_stud4)

leader1.display_list()
leader2.display_list()

# Print the fullname of the students in the list of students under the instances of your subclass.
# for i in leader1.display_list():
#     print(i.fullname())

# Print the email of the instances of your subclass.
#stud_7.email()

