# Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance
#-------------------------------------
class Person:
    name = "void string"
    def __init__ (self, name = None ):
        self.name = name
#-------------------------------------
men_1 = Person("pham trung hieu")
print (Person.name , men_1.name )

men_2 = Person() # khai bao men2 thuoc Person 
men_2.name = "nico"
print ( men_2.name )