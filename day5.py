
1. #add#
s1=int(input("enter the first number: "))
s2=int(input("enter the second number: "))
def sum(s1,s2):
 add=s1+s2;
 return add;
print("sum of nos",sum(s1,s2))

#sub#
s1=int(input("enter the first number: "))
s2=int(input("enter the second number: "))
def sub(s1,s2):
 s=s1-s2;
 return s;
print("sub of nos",sub(s1,s2))

#mul#
s1=int(input("enter the first number: "))
s2=int(input("enter the second number: "))
def mul(s1,s2):
 m=s1*s2;
 return m;
print("mul of nos",mul(s1,s2))

#div#
s1=int(input("enter the first number: "))
s2=int(input("enter the second number: "))
def div(s1,s2):
 d=s1/s2;
 return d;
print("div of nos",div(s1,s2))

2. #function#
def covid(fname=str(input("enter the patient name: "))):
    print("Patient name is: " +fname)
covid()
def temp(x=98):
    return x
print("temperature is: ",temp())
