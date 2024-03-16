import csv
class Auth:
    def registration(self):         #,uid,pwd,pincode,village,phone):
        print("***************************Welcome to the User Registration Page***************************")
        self.uid=input('Enter your username             :')
        self.pwd=input("Enter your password             :")
        self.pincode=input("Enter your village pin code :")
        self.village=input("Enter  your Village name    :")
        self.phone=input("Enter the phone num           :")
        self.header=["uid","pwd","pin","village","phone"]
        if(self.uid!="" and self.pwd!="" and self.pincode!="" and self.village!="" and self.phone!=""):
            pass
        else:
            print("Invalid input!")
            ob=Auth()
            ob.registration()
        
        with open("customer.csv", "a",newline="") as file:
            s=csv.writer(file)
            s.writerow([self.uid,self.pwd,self.pincode,self.village,self.phone])
            print("Registration Successfully Done")
            # ob=Auth()
            # ob.login()
            
    def login(self):
        print("**********************welcome to login page***********************************")
        self.uid=input('Enter your username             :')
        self.pwd=input("Enter your password             :")
        with open("customer.csv","r",newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                #print(row["uid"])
                if(row['uid']==self.uid and row['pwd']==self.pwd):
                    print("*********************Login successful! welcome  to {0} ********************************".format(row['uid']))
                    return True
            else:
                print("User not found !")
                print("Perfer to register the user")
                obj=Auth()
                obj.registration()
                
                    
    def header(self):
        with open("customer.csv", "w",newline="") as file:
            writer=csv.writer(file)
            writer.writerow(["uid","pwd","pincode","village","phone"])



# ob.registration()