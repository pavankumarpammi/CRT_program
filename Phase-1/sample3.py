#write a program to check the no road price of a bike under the conditions 
#if the prize is >72 thousand the income taxes 10% of original price and insurance will be 15% of actual price
# if the prize is >1.50 lac and less than <2 lac the tax could be 25% and ins will be 20%
# if the prize is >2 lac then tax 35% and ins will be 28%
# other wise minimum prize start with 75 enter a  correct input
#print the on road prize of bike actual prize +tax+ins

actual =int(input("Enter the prize:"))
total="tax+ins+actual"
if(actual >= 72000 and actual <= 150000):
  tax = actual*0.1
  ins = actual*0.15
  #total =actual+tax+ins
  print("On Road  Price of Bike :",eval(total))
elif(actual>150000 and actual<=200000):
  tax = actual*0.25
  ins = actual*0.20
  total =actual+tax+ins
  print("On Road  Price of Bike :",total)
elif(actual>200000):
  tax = actual*0.35
  ins = actual*0.28
  total = actual+tax+ins 
  print("On Road  Price of Bike :",total)
else:
  print("Correct value of prize")
  print("Bike prize start from 750000") 

#simple check leap year
