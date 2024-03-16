# class Faculity:
#     def __init__(self,name,dept,no) -> None:
#         self.name =name
#         self.dept=dept
#         self.no=no
#     def info(self):
#         print("Faculity Details:")
#         print("Name : ",self.name)
#         print("Department : ",self.dept)
#         print("Id",self.no)

# class cse(Faculity):
#     pass

# obj=cse("Vamsi","Ds",4459)
# obj.info()

#create a class of name palcements which as a function info which displays "we have ###".
#create another class name dept which function display which will display name of dept present in clg
#create a class pragati with function welcome() which display's msg "welcome to pragati engineering college we glad "
# pragati class should also display details about dept names and placements

# class  Placements:
#     def info(self,num):
#         print("We Have {} Placed Students.".format(num))
#         print("still counting.....")
# class Dept:
#     def display(self):
#         print("We are having various departments:")
#         print("\tCSE")
#         print("\tECE")
#         print("\tMEC")
#         print("\tCIVIL")
#         print("\tEEE")
#         print("\tAIML")
#         print("\tAI")
#         print("\tDS")
#         print("\tIT")
# class pragati(Dept,Placements):
#     def welcome(self):
#         print("*************************************WELCOME TO PRAGATI ENGINEERING COLLEGE****************************************")

# obj=pragati()
# obj.welcome()
# obj.display()
# obj.info(653)

#FUNCTION OVERLOADING NOT SUPPORTED IN PYTHON

# class A:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)

# obj=A()
# obj.add(7,4,1)
# obj.add(1,2)
# obj.add(10)

#OVERRIDING IS NOT POSSIBLE IN PYTHON
class Father:
    def bike(self):
        print("Galmour")
    def laptop(self):
        print("Dell")
class vamsi(Father):
    def laptop(self):
        print("Hp 15")
obj=vamsi()
obj.bike()
obj.laptop()

#create a class ticket which will be the abstract class inside that create a function Book ticket
#which will be abstract method and has nothing in it.
#create a class makeMyTrip which will use the book ticket funtion from ticket class to take the details 
#such as name phoneno emailId journey date and display's a message "thank you for booking from makeMyTrip"
#create a class irctc which use the Book ticket of ticket class and takes the same details has makeMyTrip 
#but in the end it will give a option to user to select whether it one way or round trip if the user option is
#rounded it again asks the user to enter the return data as well and then prints a msg "thanks for choosing irtc"
#else "Thank u for choosing irctc."
#create a class Indigo which takes all details as irctc and just askes which mode of transport u r to goint
#plain or flight or bus  and display "thank u for choosing Indigo"