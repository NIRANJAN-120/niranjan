print("Welcome to smb travells")
print(" select the destination  to travell")
print('\n banglore \n 1--> chennai \n 2--> Delhi \n 3-->Mumbai \n 4--> Hydarabad')
# print('1-->AC seats: \n 2-->Non-Ac seats: ')
c=eval(input("enter the destination"))
if c==1:
  e=350
  print("total  350 km  for banglore to chenni")
elif c==2:
   e=2000
   print("total  2000 km  for banglore to Delhi")
elif c==3:
   e=800
   print("total  800 km  for banglore to Mumbai")
elif c==4:
   e=500
   print("total  500 km  for banglore to Hydarabad")
else :
   print("plz allow given options")

print('seats :  \n 1-->  adult :    \n 2--> childerns :')
a=int(input("no of seats for adults"))
b=int(input("no of seats for childrens"))
print("total no of seats ",a+b)

print('\n 1-->AC  \n 2-->Non-Ac ')
Ac=int(input("enter the choice"))
if Ac==1:
   print(10*a*e)
   print(5*b*e)
   print((10*a*e)+(5*b*e))
elif Ac==2 :
    print(5*a*e)
    print(3*b*e)
    print((5*a*e)+(3*b*e))

   