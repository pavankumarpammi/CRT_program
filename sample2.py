# integer input form user if that integer if it is divisible by 3 and 6 print good number  if the number divisible 2 and 7 print an average number
# if the integer divisible 4 or 9 print awesome number else print bad number
num =int(input())
if((num%3 ==0) and (num%6 ==0)):
    print('good number')
elif((num%4==0 ) or (num%9==0)):
    print('awesome number')
else:
    print('Bad number')


    