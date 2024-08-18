import random
import string

#list from which computer will select randomly one word
words=['apple','banana','orange','grapes','papaya','mango']
word=random.choice(words)
print(f'computer choosed word = {word}')
chances=6
l=len(word)
alpha=list(string.ascii_lowercase) 
word1='-'*len(word)
rej=[]

while chances != 0:
    print(f'current word : {word1}')
    user=input('Enter letter : ')
    if user in word:
        for i in range(len(word)):
            if word[i]==user:
                word1=word1[0:i]+user+word1[i+1:]
        alpha.remove(user)
        if word1==word:
            print('user won the game')
            break
    else:
        chances=chances-1
        print(f'chances left {chances}')
        alpha.remove(user)
        rej.append(user)
        if chances==0:
            print(f'user lost the game')
            break
