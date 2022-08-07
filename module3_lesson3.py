#  Create a class called “Group_leader” that inherits from the class “Students” that we created in the practical session today. 
# (Initialize the class and let it&nbsp; take an argument of the list of students under the group leader. Let the parent class take care of the other arguments)
# • Define a method that adds students to the list of student under the group leader.
# • Define a method that removes students from the list of students under the group leader.
# • Define a method that prints out the full names of students in the list of students under group leader.
# • Create 3 more instances of the parent class we defined in the practical session.
# • Create 2 instances of the sub class you created.
# • Add 2 students each to the list of students under the instances of your subclass.
# • Remove 1 student each from the list of students under the instances of your subclass
# • Print the fullname of the students in the list of students under the instances of your subclass.
# • Print the email of the instances of your subclass.

class Students:
    def __init__(self, first, last, student=[]):
        self.first = first
        self.last = last
        self.fullname = first + " " + last
        self.email = first + last + "@stutern.com"
      
       
stud_1 = (Students("Bukola", "Dare"))
stud_2 = (Students("Temitope", "Balogun"))
stud_3 = (Students("Mariam", "Alade"))

#print(stud_4.fullname)
#print(stud_5.email)
stud_1.email_add()

class Group_leader(Students):
    def __init__(self, first, last, student=[]):
        self.student = student
        super().__init__(first, last)

    def add_student():
        self.student.append(student)
        



# studentlist = []
# studentlist.append(Group_leader("Daniel", "Okon"))
# studentlist.append(Group_leader("John", "Doe"))

# for student in studentlist:
#     print('Name : {} {}'.format(student.first, student.last))

#####tut