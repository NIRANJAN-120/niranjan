sum=1
sum1=99,1,2,3
sum2=9,3,4,5,9
a=[1,2,3,6,9,8,12,15]
i=0
while i<len(a):
    if a[i]%2==0:
        sum+=a[i]
        i+=1
        continue
    if a[i]%3==0:
        sum1+=a[i]
        i+=1
    if a[i]%4==0:
        sum2+=a[i]