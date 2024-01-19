a=input('enter a string \n')
out=""
dup=""
for i in a:
    if i  not in out:
        out=out+i
    else:
        dup=dup+i
print(dup)
