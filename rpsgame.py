p1=eval(input('player 1 choose your choice among ROCK....PAPER......SCISSOR  \n'))
p2=eval(input('player 2 choose your choice among ROCK....PAPER......SCISSOR  \n'))
if p1=='ROCK' and P2=='PAPER':
    print('p1 win')
elif p1=='PAPER' and p2=='SCISSOR':
    print('p2 win')
elif p1=='ROCK' and p2=='SCISSOR':
    print('p2 win')
elif p1=='ROCK' and p2=='ROCK':
    print('it is tie')
elif p1=='PAPER' and p2=='PAPER':
    print('it is tie')
elif p1=='SCISSOR' and p2=='SCISSOR':
    print('it is tie')
else:
    print('choose the correct choice')
