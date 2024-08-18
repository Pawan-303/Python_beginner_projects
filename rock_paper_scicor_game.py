import random 

def game():
    user=input('enter your choice rock[r] , paper[p], scissor[s]\n')
    comp=random.choice(['r','p','s'])
    print(f'user choice {user}')
    print(f'computer choice {comp}')
    result=''
    if user==comp:
        result='tie'
    elif user=='r':
        if comp=='p':
            result='lost'
        else:
            result = 'won'
    elif user == 'p':
        if comp=='s':
            result='lost'
        else:
            result = 'won'
    elif user=='s':
        if comp=='r':
            result='lost'
        else:
            result = 'won'
    return result

r=game()
if r=='tie':
    print('game tie')
else:
    print(f'user have {r} the game')