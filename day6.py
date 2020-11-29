#loop list of numbers +2#
a=[1,2,3,4,5,7,9,10]
for i in a:
    print(i,i+2)

# pattern#
n=int(input())
for i in range(n,0,-1):
    j=i
    while(j>0):
        print(j,end=' ')
        j=j-1
    print()

#fibonacci#
x,y=0,1
while y<15:
    print(y)
    x,y = y,x+y

#Arm strong#
    num=int(input("enter a number"))
    Sum = 0
    temp=num
    while temp>0:
        digit=temp%10
        Sum+=digit**3
        temp//=10
        if num==Sum:
            print("no is armstrong")
        else:
            print("no is not armstrong")

#multiplication table 9#

num=int(input("enter the number"))
print("multiplication table of",num)
for i in range(1,13):
        print(num,"x",i,"=",num*i)


#check no is positive or not#

num=int(input("enter the number"))
if num>0:
    print("positive number")
elif num==0:
    print("Zero")
else:
    print("Negative number")


#Trigonometric function#

import math

# number 
x = 0.75 

# math.cos()
print("math.cos(",x,"): ", math.cos(x));
# math.sin()
print("math.sin(",x,"): ", math.sin(x));
# math.tan()
print("math.tan(",x,"): ", math.tan(x));

#basic calculator#

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    
    choice = input("Enter choice(1/2/3/4): ")

   
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")































        
