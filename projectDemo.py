class Company:

    def __init__(self):
        print("*********************Hello welcome to xyz car showRoom******************************")
        print()
        print("We are providing this company cars:")
        print()
        print("Please Select the car according to Number:")
        print("1.Mahindar")
        print("2.Totyota")
        print("3.Mercedes")
        car_company =int(input("Enter the number according to company : "))
        if(car_company==1):
            name="1.Mahindar"
        elif(car_company==2):
            name="2.Totyota"
        elif(car_company==3):
            name="3.Mercedes"
        else:
            return
        print()
        print("==================================WELCOME TO ",car_company," ========================================")
        print()
        lis=["1.Model-1","2.Model-2","3.Model-3"]
        print("Having model of :")
        print(lis)
        print("Enter the Model in number (1/2/3):")
    def model_car(self,model):
        if(model==1):
            self.price=1500000
        elif(model==2):
            self.price=2000000
        elif(model==3):
            self.price=2500000
        else:
            self.price=1500000
            print("Sorry for wrong input")
            exit
    def variant(self,input):
        if input==1:
            self.cgst=0.1
            self.sgst=0.12
        elif input==2:
            self.cgst=0.12
            self.sgst=0.15
        else:
            print("Wrong input")
            exit
    def display(self):
        print("The ex-showroom price:",self.price)
        print("The road prize is:",(self.price)+(self.price*self.cgst)+(self.price*self.sgst)+self.price*0.2)
while(True):
    obj=Company()
    model=input()
    obj.model_car(model)
    print("Having a variant:")
    print("1.Petrol ")
    print("2.Disel")

    n=int(input("Enter the choose in number(1/2):"))

    obj.variant(n)
    obj.display()
