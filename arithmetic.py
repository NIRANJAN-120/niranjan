var1=eval(input('enter value of var1  \n'))
var2=eval(input('enter value of var2   \n'))
var3=eval(input('enter the operator you want to perform \n'))
if var3=='+':
    print(var1+var2)
elif var3=='-':
    print(var1-var2)
elif var3=='*':
    print(var1*var2)
elif var3=='/':
    print(var1/var2)
elif var3=='//':
    print(var1//var2)
elif var3=='%':
    print(var1%var2)
elif var3=='**':
    print(var1**var2)
else:
    print('enter correct operator')
