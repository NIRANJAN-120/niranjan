x=eval(input('enter x value \n'))
if type(x) in (bool,int,float,complex):
    print(x**2)
else:
    print(3*len(x)+1)

