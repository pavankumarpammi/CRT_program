#your if year is year%4 and y%100!=0 or y%400 then is called leap year
year = int(input())
if((year%4==0 and year%100 !=0) or  (year%400 == 0)):
    print("It is a Leap Year")
else:
    print("Not a Leap year")

