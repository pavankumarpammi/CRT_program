class Mahindra:

    def __init__(self):
        print()
        print("==================================WELCOME TO MAHINDRA ========================================")
        print()
        lis=["1.Model-1","2.Model-2","3.Model-3"]
        print("Having model of :")
        print(lis)
    def model_car(self,model):
        if(model==1):
            self.price=1500000
        elif(model==2):
            self.price=2000000
        elif(model==3):
            self.price=2500000
        else:
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

        

class Totyota:
    def __init__(self):
        print("=================================WELCOME TO TOTYOTA =============================================")
        print()
        lis=["1.Model-1","2.Model-2","3.Model-3"]
        print("Having model of :")
        print(lis)
    def model_car(self,model):
        if(model==1):
            self.price=1500000
        elif(model==2):
            self.price=2000000
        elif(model==3):
            self.price=2500000
        else:
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

class Mercedes:
    def __init__(self):
        print("=================================WELCOME TO MERCEDES ==========================================")
        print()
        lis=["1.Model-1","2.Model-2","3.Model-3"]
        print("Having model of :")
        print(lis)
    def model_car(self,model):
        if(model==1):
            self.price=1500000
        elif(model==2):
            self.price=2000000
        elif(model==3):
            self.price=2500000
        else:
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


print("*********************Hello welcome to xyz car showRoom******************************")
print()
print("We are providing this company cars:")
print()
print("Please Select the car according to Number:")
print("1.Mahindar")
print("2.Totyota")
print("3.Mercedes")
n =int(input("Enter the number according to company"))
if(n==1):
    obj=Mahindra()
    print("Enter the model according to the number:")
    model=int(input())
    obj.model_car(model)
    print("We are providing this variant :")
    print("1.Petrol","2.Disel")
    vari=int(input())
    obj.variant(vari)
    obj.display()
    
elif(n==2):
    obj=Totyota()
    print("Enter the model according to the number:")
    model=int(input())
    obj.model_car(model)
    print("We are providing this variant :")
    print("1.Petrol","2.Disel")
    vari=int(input())
    obj.variant(vari)
    obj.display()
elif(n==3):
    obj=Mercedes()
    print("Enter the model according to the number:")
    model=int(input())
    obj.model_car(model)
    print("We are providing this variant :")
    print("1.Petrol","2.Disel")
    vari=int(input())
    obj.variant(vari)
    obj.display()


