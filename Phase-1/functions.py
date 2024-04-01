# # # # #write a function which takes two parameters a ,b type caste the value of second argument into integer
# # # # #then multiply the both the arguments and print the last digit of result
# # # # def multiply_and_print(a, b):
# # # #     val = int(b)
# # # #     res=a*val
# # # #     print(res%10)
# # # # multiply_and_print(5,"7")
# # # # def normal_function(a,b):
# # # #     print(a+b)
# # # # def default_value(a=0,b=0):
# # # #     print(a+b)
# # # # def valued_funtion(a,b):
# # # #     print(a+b)
# # # # # def No_variable(*arga,**kwargs):
# # # # #     print(arga+kwargs)

# # # # normal_function(5,10)
# # # # default_value()
# # # # default_value(5,10)
# # # # valued_funtion(b=10,a=5)
# # # #write a function to calculate sum of first and last digit of  a number taken as agruments
# # # # def sum_first_last(dup):
# # # #     first=dup%10
# # # #     while(dup>0):
# # # #         rem=dup%10
# # # #         dup//=10
# # # #         last=rem
# # # #     print(first+last)

# # # # sum_first_last(12545789)
# # # #Write a login funtion which accepted the user only when username and password are name and display a message
# # # #login successful otherwise it keep asking the user to enter the credientals until they are correct


# # # # def login():
# # # #     # username="admin"
# # # #     # password="123456"
# # # #     # flag=True
# # # #     while(True):
# # # #         name=input("Enter the username:")
# # # #         code=input("Enter the password:")
# # # #         if (name==code):
# # # #             print("Login Successful")
# # # #             break
# # # #         else:
# # # #             print('Wrong creditanls')

# # # # login()


# # # # def fibnonaci(num):
# # # #     if(num<1):
# # # #         return 1
# # # #     else:
# # # #         return fibnonaci(num-2)+fibnonaci(num-1)

# # # # def fact(num):
# # # #     if(num==0):
# # # #         return 1
# # # #     else:
# # # #         return num*fact(num-1)

# # # # print(fibnonaci(10))
# # # # print(fact(10))


        
# # # #recurrsive program to print a digit in reverse order 

# # # # def rev(num):
# # # #     if(num==0):
# # # #         return 
# # # #     else:
# # # #         print(num%10)
# # # #         rev(num//10)
# # # # rev(123456)

# # # #write a recersive function to count the no of digit of a number
# # # #2.write a recer  calc the sum of digit of a num

# # # # def rev(num,s,cnt):
# # # #     if(num==0):
# # # #         print(s,cnt)
# # # #         return 
# # # #     else:
# # # #         sum=num%10
# # # #         return rev(num//10,s+sum,cnt+1)



# # # # rev(12345,0,0)

# # # # def rev(num):
# # # #     if(num==0):
# # # #         return 0
# # # #     else:
# # # #         return 1+rev(num//10)
# # # # print(rev(123))

# # # # def rev(num):
# # # #     if(num==0):
# # # #         return 0
# # # #     else:
# # # #         return num%10+rev(num//10)
# # # # print(rev(1237658))

# # # #amstrong number

# # # # def cnt(n):
# # # #     if(n==0):
# # # #         return 0
# # # #     return 1+cnt(n//10)
# # # # def arm(num,p):
# # # #     if(num==0):
# # # #         return 0
# # # #     return ((num%10)**p)+arm(num//10,p)

# # # # #val =arm(153,cnt(153))
# # # # inp=int(input())
# # # # val=arm(inp,cnt(inp))

# # # # if(val==inp):
# # # #     print('armstrong')
# # # # else:
# # # #     print('Not armstrong')

# # # #creating a list and accessing

# # # # lis=[1,2,3,"vamsi","birthday","Happy"]
# # # # print(lis[7:2:-1])
# # # # lis.append(5)
# # # # print(lis)
# # # # # dup=[dup.append(for i in lis)]
# # # # lis.insert(3,"to u")
# # # # print(lis[6:2:-1])
# # # # # print([x for x in lis if "a" in x])
# # # # lis[0]="hello"
# # # # print(lis)


# # # #1.add min and max
# # # # lis=[12,42,23,96,7,18,10,133]
# # # # # 12,42,23,96,7,18,10,133
# # # # #print(lis)
# # # # min=lis[0]
# # # # max=lis[0]
# # # # min_ind,max_ind=0,0
# # # # for i in range(0,len(lis)):
# # # #     if lis[i]<min:
# # # #         min=lis[i]
# # # #         min_ind=i
# # # #     if lis[i]>max:
# # # #         max=lis[i]
# # # #         max_ind=i
# # # # lis[min_ind]=max-min
# # # # lis[max_ind]=max+min
# # # # print(min+max)
# # # # print(lis)

# # # #creation of tuple adding values manullay and check the tuple are mutable or not
# # # # tup=(1,2,3,"Vamsi",True,None,[],{})
# # # # print("Tuple is : ",end="")
# # # # print(tup)
# # # # print(tup[0])
# # # # tup=tup+(4,5,6)
# # # # print(tup)
# # # # # print(sorted(tup))
# # # # print(sorted(tup[:3]))
# # # # tup=(5,6,9)+tup
# # # # print(tup)
# # # # print(sorted(tup[:6]))

# # # #create dict to min 4 pairs acessing values using keys acessing whole dict using for loops 
# # # # dic={'name':'vamsi','village':'elamanchi','age':21,'class':'15th'}
# # # # print(dic)
# # # # for key in dic:
# # # #     print(dic[key])
# # # # dic['name']='vessam vamsi'
# # # # print(dic)
# # # # for key ,value in dic.items():
# # # #     print(key,"=",value)
# # # # del d
# # # # print(dic)

# # # #1. -1,42,65,1,-4,6 write a program to find the second smallest negative number without inbuilt funtion
# # # # lis=[22,-1,42,65,1,-4,6]
# # # # min=999
# # # # sec_min=-1
# # # # for i in lis:
# # # #     if i<min:
# # # #         min=i
# # # #     if i!=min and i<sec_min:
# # # #         sec_min=i
# # # # # for i in lis:
    
# # # # print(min)
# # # # print(sec_min)

# # # #optimal approach
# # # lis=[22,-1,42,65,1,-4,6]
# # # min=lis[0]
# # # sec_min=lis[0]
# # # for i in lis:
# # #     if i<min:
# # #         sec_min=min
# # #         min=i
# # #     elif sec_min>i and sec_min>min:
# # #         sec_min=i
# # # print(min)
# # # print(sec_min)

# # # #lambda function is  a = Lamda x:x+10   b=Lamda x,y :x**y   to call  a(10)  b(10,2) 
# # # #b=list(map(lamda x:x//10))

# # #a,b,c=map(int,input().split())

# # #set 
# # s={1,3,4,7}
# # s.add(5)
# # print(len(s))
# # print(s)
# # s.add(2)
# # # print(s[:5])
# # s.remove(3)
# # print(s)

# # fs =frozenset(s)
# # print(fs)

# # 2,0,1024,0,40,230,0  shift the all zero to right

# lis=[2,0,1024,0,40,230,0]
# # dup=[]
# # count=0
# # for i in lis:
# #     if(i!=0):
# #         dup.append(i)
# #     else:
# #         count+=1
# # while(count<len(lis)-1):
# #     dup.append(0)
# #     count+=1
# # print(dup)
# first_ind=0
# last_ind=len(lis)-1

# # while(i<=j):
# #     if(lis[i]==0):
# #           first_ind=i
# #     if(lis[last]!=0):
# #             temp=lis[first]
# #             lis[first]=lis[last]
# #             lis[last]=temp
# #     first+=1
# #     last-=1
# first=0
# last=len(lis)-1
# for i in range(0,len(lis)):
#     if(lis[i]==0):
#         first=i
#     j=len(lis)-i-1
#     if(lis[j]!=0):
#         last=j
#     if(first>0 and last<len(lis)-1):
#         temp=lis[i]
#         lis[i]=lis[j]
#         lis[j]=temp

# print(lis)
# # create a class f15 with funtions lights fans ac   desp lig->the color of light which is taken as parameter as funtion
# # fan-> It display the speed with it regulator speed taken as a parameter 
# # ac -> display the room temp and outside temp which are taken as parameters
# fourth display->which display the difference outside - room temp and also display fan speed
# class F15:
#     def __init__(vamsi,start_time,end_time):
#         print("The Features provided by F15 Timinging from ",start_time," to ",end_time )
#         vamsi.start=start_time
#         vamsi.end=end_time
#     def light(vamsi,color):
#         print("The color of light :",color)
#     def fans(vamsi,speed):
#         print("The regulator speed :",speed)
#         vamsi.speed=speed
#     def ac(vamsi,room_temp,outside_temp):
#         print("The room temperature :",room_temp)
#         print("The outside temperatue:",outside_temp)
#         vamsi.room_temp=room_temp
#         vamsi.outside_temp=outside_temp
#     def display(vamsi):
#         print("Differenc is temp: ",vamsi.outside_temp - vamsi.room_temp)
#         print("Fans speed :",vamsi.speed)
#         print(vamsi.start ," ",vamsi.end)


# obj = F15(9,4)
# obj.light("white")
# obj.fans(5)
# obj.ac(16,32)
# obj.display()
# # obj = F15()
# #constructor in java is as class name but in python it as __init__
# #parameterized constructor 
#details of road price and millage display to user
# 3 car  tatyota mahindra mercides
# take input from user for car company name and in the input message 3 compaines 
# user input company name those as input/argument to model_name funtion() ,which welcome the user according
# to the company name ask the user to enter the sepicfic model name for that company 
# the second function whose name is variant() according to the company_name and car_model the user should
#ask enter variant he would like choose from petrol ,disel
#last funtion according to the car_company,car_model,car_variant first its exshowromm_price display and then on_road_price
#on_road_price should display which calculated as ex_showroom_price+cgst+sgst+ins.
#sgst ,cgst,ins having common value through out the carshowroom

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


