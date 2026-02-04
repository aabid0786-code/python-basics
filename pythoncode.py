a=15
b=4
result = a*b
print(result)

result1 = a**b
print (result1)
result2 = (a//b)
print(result2)
result3 = (a%b)
print(result3)

a= 15
b=40
c= 15*3
print ( "total cost of pen", c)
d= 40*2
print ("total cost of notebook", d)


n1 = int (input("enter the first number : "))
n2= int (input("enter the 2nd number : "))
n3 = int (input("enter the third number : "))
n4 = int (input("enter the fourth number : "))
n5 = int (input("enter the fifth number : "))
total = n1+n2+n3+n4+n5
print (total/5)
n= int (input("enter any number :"))
square = (n**2)
cube =(n**3)
square_root= ( n ** 0.5)
print ( square , cube , square_root )


n = int(input("enter any number in seconds : "))
minutes= n/60
print (minutes)
total_distace = 120
total_time = 3
average_speed = 120/3
print (average_speed)


n1= int(input("enter the first number :"))
n2 = int(input("enter the second number :"))
if (n1%n2==0):
    print("n1 is multiple of n2")
else:
    print("n1 is not the multiple of n2")



p = int (input("enter the principle"))
num = int(input("enter the number : "))
if  num>0:
    print ("the number is positive")
elif  num < 0:
    print("the number is negative")
else:
    print("the number is zero")

age = int(input("enter the age of any person : "))
if age>= 18:
    print("the person is eligible for vote")
else:
    print("the persom is not eligible for vote ")


num = int(input("enter your number : "))
if num % 2== 0:
    print("your number is even")
else:
    print ("your number is odd")

num1 = int(input("enter your first number : "))
num2 = int (input("enter your second number : "))
if num1>num2:
    print ("your first number is greater than second")
else:
    print("your second number is greater than first")

num = int(input("enter your number : "))
if  num % 5 == 0:
    print("the number is divisible by 5")
else :
    print ("the number is not divisible by 5")

year = int (input("enter the year"))
if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
 print("this is leap year")
else :
 print("this year is not a leap year")

num = int(input("enter your number : " ))
if num<10:
    print("the number is single digit ")
elif num >10 and num <100:
 print("the number is two digit ")
else :
    print ("the number is three digit")

temperature = int (input( " enter the temperature in celsius : "))
if temperature <= 0:
    print("freezing")
elif temperature <= 20:
    print("cold")
elif temperature > 20 and temperature <= 35:
    print ("warm")
else:
    print("hot")

overview/technology use/ industrial use kya hai / features  and future plan / market use 

num = int (input ("enter the number : "))
if num > 0 and num % 2 == 0:
    print ("the number is even positive")
elif num>0 and num%2 != 0:
    print ("number is positive odd ")
else:
    print ("number is negative")

password = int (input(" enter the password : "))
if password  == 12345678:
    print("Access Granted")
else:
    print ("Access Denied ")
  
side1 = int(input ("enter the first side : "))
side2 = int(input("enter the second side : "))
side3 = int (input("enter the third side : "))
if side1+side2>side3 or side1+side3>side2 or side3+side2> side1:
     print("the triangle is valid")
else:
 print("triangle is not valid")

sub1 = int (input ("enter the marks of 1st subject : "))
sub2 = int (input ("enter the marks of 2nd subject : "))
sub3 = int (input ("enter the marks of third subject : "))
if sub1+sub2+sub3>=35:
    print ("passed")
else:
    print ("failed")

alpha = input("enter your alphabet : ").lower()
if alpha.isalpha():
   if alpha in 'aeiou':
      print("alphabet is vowel")
   else:
      print("alphabet is constat")
else:
   print("alphabet is not an alphabet")
   