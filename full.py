st=input('good morning')
i=-1
while i>=-len(st):
    if st[i] not in st[:i-1]:
        prime(st[i])
        break
    i-=1