print('enter \n 1---->ROCK \n 2---->PAPER \n 3--->SCISSOR')
p1=input('player 1:-')
p2=input('palyer 2:-')
if p1==p2:
    print('match tie')
elif p1=='1' and p2=='3':
    print('player 1 won')
elif p1=='2' and p2=='1':
    print('player 1 won')
elif p1=='3' and p2=='2':
    print('player 1 won')
else:
    print('player 2 won')
