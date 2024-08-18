import random

if __name__ == '__main__':
    l=1
    h=1000
    feedback=''
    while feedback != 'c':
        guess=random.randint(l,h)
        feedback=input (f"{guess} is low or high or correct low='l',high='h',correct='c'\n")
        if feedback=='c':
            break
        elif feedback =='l':
            l = guess + 1
        elif feedback =='h':
            h=guess-1
    print(f'hey computer guessed correctly the number is {guess}')