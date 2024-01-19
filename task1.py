n=eval((input('enter the character')))
if n in '0123456789':
       print('number')
elif n>='A' and n<='Z':
           print("upper case")
elif n>='a' and n<='z':
            print('lower case')
else:
            print("special character")
