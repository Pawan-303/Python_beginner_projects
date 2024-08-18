import random

count = 0
n=random.randint(0,100)

def guess():
    global count
    while(True):
        x=int(input('guess number: '))
        count = count + 1
        if n==x:
            print('Hoorray you are right')
            break

        if n>x:
            print('guess larger')
    
        else:
            print('guess smaller')
    print(f'no of guess taken : {count}')

