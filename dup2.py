a=input('enter the string \n')
out=''
for i in range(len(a)):
    if a[i] in a[i+1:] and len(a)-1:
        out+=a[i]
print(out)
