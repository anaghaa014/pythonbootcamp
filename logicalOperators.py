'''age=int(input("enter your age"))
if(age>=18 and age<=24):
 print(f" you are eligible to drive 2 wheeler\n")
elif(age>=25 and age<=45):
 print(" you are eligible to drive 2 wheeler and 4 wheeler")
elif(age>=46 and age<=60):
 print("you are eligible to drive 2 wheeler ,4 wheeler and 6 wheeler")
else:
 print("you are not eligible to drive")

a=int(input("the number of apples are: \n"))
b=int(input("the number of bananas are: \n"))
o=int(input("the number of oranges are: \n"))
asum=a*15
bsum=b*4
osum=o*5
print(f"apples cost is{ a*15}")
print(f"banana cost is{ b*4}")
print(f"oranges cost is{ o*5}")
total=asum+bsum+osum
print(f"sum of fruits is{asum+bsum+osum}\n")
amt=int(input("enter the given amount by y"))
if(total<=amt):
 print("shopkeeper didnt deceive")
elif(total>amt):
 print("shopkeeper deceived")'''

'''num1=int(input("enter the number"))
if(num1>0 and num1%2==0):
 print(f"the number is positive even")
elif(num1>0 and num1%2==1):
 print(f"the number is positive odd")
elif(num1<0 and num1%2==0):
 print(f"the number is negative even")
elif(num1<0 and num1%2==1):
 print(f"the number is negative odd")'''



'''mr z is selected for olympics. 
he is participating in swimming ......only one winner will be selected.
z is selected. z has friends named x,your
x participates in shuttle
y participates in table tennis
according to selection committee, the requirements of badminton players are
1)h: 140 cm
2)w:factors of 2
3)bodyfat:<12%
according to selection committee, the requirements of table tennis are
1)h:118-148 cm
2)w: factors of no of medals won by mr z
3)body fat=14%
according to previous history, z partcipated in 14 games , out of which he is having success rate of 50%

write a program to check x,y,z travel in same plane or not'''

'''
xh=int(input("enter the height "))
xw = int(input("enter the weight "))
xbf=int(input("enter the bodyfat "))
yh=int(input("enter the height of y :"))
ybf=int(input("enter the bodyfat of y :"))
yw= 14/0.5
if((xh>140)and (xw%2==0) and (xbf<14)):
 if(((yh>118)and(yh<148)) and (yw>0) and (ybf<14)):
   print("they are travelling in the same plane")
else:
   print("they are not travelling in the same plane")'''



           














