polymorphism in classes
we can achieve polymorphism in 2 ways
1.) method overloading --> it is not possible in python
2.) method overriding

tasks
write the code for the below tasks using function
1.)d1 = {"shirt": 1000, "pant":1500, "shoes": "900", "handkey": 30}
a.) find the min ans max priced product
b.) find the product starts with 's' and 's'

2.) find the n = 67, is strong number or not

3.) l1 = [1,2,3,4,5,6]
n=2 --> [5, 6, 1,2,3,4]
n=3 --> [4,5,6, 1,2,3]
# method riding
#*polymyresation in classes
class bank:
    def ratio( self )
    print ("all banks has repo rate ")
#class SBI (bank):
 #   def ratio (self )
#print ("sBI rate is 9%)
#class ibo (bank ):
#def ratio (self )
 #print ("iob rate is 7.5%")

#i=IOB()
 #.ratio()
 #s= SBI()
 #.ratio()
 #?Eg:2
 
class India(USA):
    def language(self):
        print("None")

    def capital(self):
         print("New delhi")

#I = India()
#I.language()
#I.capital()
         
class triangle(shapes):
    def traingle_sides(self):
        print("3 sides")

    def name(self):
        
        print("Iam traingle")

   def sides (self):
       pass

class square(shapes):
    def square(self):
        print("4 sides")
        
tr triangle()
tr.traingle_sides()
tr.name()
# ! Rules to define abstract class1
1.) abract class cannot be instantiated
2.) from abc import abc, abstractmethod
3.) subclass the normal class with ABC
4.) convert the normal method inside the abstract class to abstract method
5.) all the child classes have to be subclassed with abstract class
6.) the abstract method should be present in the
child classes

# ! Eg:2
# * super() --> used to access the parent class method from class method
from abc import ABC, abstractmethod
class c1(ABC):
    @abstractmthod
    def m1(self):
        print("this is abstract class")

class c2:
    def m2(slf):
        print("iam child 1")

    def m1(self):
        pass

class1 = c1()
class2.m2()

class2 = c2()
class.m2()

#def display (self):
# print ( self.__ phone )
#C= c1()
#C. display ()
#* ------>Eg:3
#? declare private method
class class 1:
    def m1 (self):
        print ("iam private method" )

c= class1()
c._m1()# error
a

# def decor (func):

d1 = {"shirt": 1000, "part": 1500, "shoes": 900, "handkey": 30}
for val in d1:
    if d1[val] == min(d1.values()):
        print(val)
for val in d1:
    of d1[val] == max(d1.values()):
        print(val)
for val in d1:
    if val.startswitch('s') or val.startswith('s'):
        print(val)



















