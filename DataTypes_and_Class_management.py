import pandas as pd
import numpy as np


#Let's create a class Person with 2 attributes and 1 method
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printinfo(self):
    print(self.firstname, self.lastname,)


#Let's create a class Student that inherits attributes and methods from class People
class Student(Person):
    def __init__(self, fname, lname, school_name):
       Person.__init__(self, fname, lname)
       self.schoolname = school_name

    def printinfo(self):
        print(self.firstname, self.lastname, self.schoolname)
 
  


#Use the Person class to create an object, and then execute the printname method:
one_person = Person("John", "Doe")
one_person.printinfo()

one_student = Student ("Philipp", "Smith", "my school")
one_student.printinfo()

#Let's create a dictionary
mydictionary1 = dict({'Location': ['Madrid', 'Barcelona', 'Valencia'] , 'Inhabitants': [100, 20, 2] })
mydictionary2 = {'Location': ['Madrid', 'Barcelona', 'Valencia'] , 'PIB': [100, 20, 2] }

#Let's create a DataFrame
my_dataframe = pd.DataFrame(mydictionary1)

#Let's create an Array  --> important: include the Numpy library
my_array = np.array([[0 , 5, 1] , [6, 7, 2]])
my_array_1D = np.array([6, 7, 2])
print(my_array[0][1])
for i in range(my_array[:][0].size - 1):
    print(my_array[i][0])

print(my_array[0][1])


#Let's create a List. It is like an array but:
#  - is easier to manage (add, delete, modify values)
#  - consumes more memory
#  - can include different datatypes (arrays can not)
my_list = [[1,2,3], [5,6,7]]
my_list.append([10, 10, 10])
print(my_list[1][1])
