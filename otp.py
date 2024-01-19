import random
out = []
while len(otp)<6:
    out+=[random.choice['@','$','*','&','!','+']]
    out+=[chr(random.radint(97,123))]
    out+=[str(random.raint(0,9))]
random.shuffle(out)
captcha =''
for i in out:
    captcha+=i

print(captcha