import csv
from dup_product import Product
class Bill:
    def __init__(self):
        print("********************************Billing stage*********************************")
        self.name = input('Enter your name : ')
        self.passcode=input('Enter your password:')
        self.phone= int(input("Enter  Your Phone Number : "))
    def form(self):
            with open("customer.csv","r",newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if(row['uid']==self.name and row['pwd']==self.passcode):
                         print("username :",row["uid"])
                         print("Phone number:",self.phone)
                         print("village :",row['village'])
                         print("pincode :",row['pincode'])
                    else:
                         print("Invalid username or password")
                         ob=Bill()
                         ob.form()
            print("Thank you for shopping 👍👍! Have Nice day......👋👋")
# ob=Bill()
# ob.form()
    
