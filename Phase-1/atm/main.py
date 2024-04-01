"""
create a atm system
1.Display the remaining amount in the atm
 # rupay -2000
   visa -5000  mastercard-8499
2.Authecuntication of user if the user authenctiate give him following option to choose

   2.1 check balance
   2.2 cash withdrawal
       2.2.1 remaining balance left
   2.3 cash deposite
       2.3.1 total amount added 
   2.4 Mini statement of last three transcations
   

"""
import auth
class ATM:
    def __init__(self):
        print("****************************************welcome to the ATM *************************************************")
        print()
        self.money=25000
        self.atm_balance=10000
        print("select the card type :")
        print("Rupay")
        print("Visa")
        print("MasterCard")
        card_type = input("Enter the card type :").lower()
        lis={"rupay":2000,"visa":5000,"mastercard":8499}
        if card_type in lis:
            self.val =lis[card_type]
        else:
            print("Invalid type!")
            obj=ATM()
        self.lis={}
    def auth(self):
        name=input("Enter the userName:")
        code=input("Enter the password:")
        self.move =auth.Auth().login(name,code)
        if(self.move==1):
            print("Authentication Successful")
            return 1
        else:
            print("Incorrect username or Password ")
            return 0  
    def check_balance(self):
        print("We are having the Balance of :",self.money)
    def cash_withdraw(self,amount):
        #print("Withdraw amount is:",amount)
        if(amount<self.val):
            if(amount<self.money):
                self.money -= amount
                self.atm_balance -= amount
                if(self.atm_balance>=0):
                    #lis["withdrawal"]=amount
                    print("Congrat you withdraw amount of ",amount)
                    print("The Balance in your account is :",self.money)
                    print("The atm having amount of ",self.atm_balance)
                    self.lis["withdrawal -"+str(amount)]="success"
                else:
                    print("Atm  balance is over. out of service")
            else:
                print("your account does not having that much amount")
        else:
            print("card limit exceeded")
    def cash_deposit(self,amount):
        self.money+=amount
        self.atm_balance+=amount
        print("successfully deposited the amount")
        print("The Balance in your account is :",self.money)
        print("The atm having amount of ",self.atm_balance)
        self.lis["Deposit -"+str(amount)]="success"
    def mini_statement(self):
        print("Mini Statement:")
        print(self.lis)
        pass

obj=ATM()
val =obj.auth()
if(val==1):
    pass
else:
    obj.auth()
while(True):
    print("***********************************welcome to atm **********************************")
    print("\n1.Check balance\n2.Deposite money\n3.Withdraw money\n4.Display Mini Statement\n5.Exit")
    ch=int(input("Enter Your choice: "))
    if(ch==1):
        obj.check_balance()
    elif(ch==2):
        n =int(input("enter the amount:"))
        obj.cash_deposit(n)
    elif(ch==3):
        m=int(input("Enter the amount to withdraw:"))
        obj.cash_withdraw(m)
    elif(ch==4):
        obj.mini_statement()
    elif(ch==5):
        break
    else:
        obj=ATM()