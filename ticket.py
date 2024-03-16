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

from abc import ABC ,abstractmethod
class ticket(ABC):
    @abstractmethod
    def book_ticket(self):
        pass
class makeMyTrip(ticket):
    def book_ticket(self):
        print()
        print("*******************************welcome to MakeMyTrip***************************************")
        name=input("Enter your name:")
        phone=int(input("Enter the Phone number:"))
        mail=input("Enter the email Id:")
        self.name=name
        self.phone=phone
        self.mail=mail
    def display(self):
        print("Thank you for booking from MakeMyTrip")
        
class irctc(makeMyTrip):
    def trip_type(self):
        print("Enter trip type one way or round way(1/2):")
        n=int(input())
        if(n==1):
            print("Thank you for choosing irctc")
        elif(n==2):
            obj=makeMyTrip()
            print("Enter the return ticket details:")
            obj.book_ticket()
            print("Thank you for choosing irctc")
        else:
            print("sorry for inconvinence...")
class indigo(irctc,makeMyTrip):
    def transport(self):

        print("Choose the mode of travelling :")
        print("1.flight") 
        print("2.train")
        print("3.Bus")
        n=int(input("Enter the choose of trip:"))
        if(n==1):
            self.type="flight"
        elif(n==2):
            self.type="train"
        elif(n==3):
            self.type="Bus"
        else:
            print("Wrong input!")
    
        print("Details of passenger:")
        print("Name:",self.name,"phone:",self.phone,"mail:",self.mail)
        print(self.type)


        
    
   

obj=indigo()
obj.book_ticket()
obj.trip_type()
obj.transport()
"""
create a atm system
1.Display the remaining amount in the atm
2.Authecuntication of user if the user authenctiate give him following option to choose
   2.1 check balance
   2.2 cash withdrawal
       2.2.1 remaining balance left
   2.3 cash deposite
       2.3.1 total amount added 
   2.4 Mini statement of last three transcations
   2.5 card renewel

"""