import csv
class Sol:
    def __init__(self):
        with open("Student.csv","a",newline="") as f:
            s =csv.writer(f)
            s.writerow(["StudentID","Rollno","Name","Phoneno"])
    def storing(self):
        with open("Student.csv","a",newline="") as f:
            s =csv.writer(f)
            studentId=int(input("Enter the studentid:"))
            roll=int(input("Enter rollno:"))
            name=input("Enter name:")
            phone=int(input("Enter phone:"))
            s.writerow([studentId,roll,name,phone])
            print("Student record has saved")

    def reading(self):
        with open("Student.csv","r",newline="") as file:
            reader=csv.DictReader(file)
            for row in reader:
                print(row["StudentID"] ,"=",row["Name"])


obj=Sol()
while(True):
    print("Enter the choose:")
    print("1.Entering data to file")
    print("2.Reading file data")
    ch=int(input())
    if(ch==1):
        obj.storing()
    elif(ch==2):
        obj.reading()
    else:
        obj=Sol()

# name=input("Enter the username:").lower()
# code=input("Enter the password:")
# f=open(name+".csv","r",newline="")
# s=csv.writer(f)
# s.writerow([code])
# s.writerow(["10000"])
# print("record has saved successfully")
# f.close()
# word =f.read(6)
# if(word==code):
#     print("authencation successful")
# else:
#     print("wrong password")
