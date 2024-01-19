s=input('enter a String:')
i=0
out=[]
start=0
while i<len(s):
    if s[i]==' ':
            out+=[s[start:i]]
    start=i+i
    i+=1
if start<len(s):
    out+=[s[start:]]
print(out)        

