if  __name__ =='__main__':
    def game(X,O):
        zero='X' if X[0]==1 else ('O' if O[0]==1 else 0)
        one='X' if X[1]==1 else ('O' if O[1]==1 else 1)
        two='X' if X[2]==1 else ('O' if O[2]==1 else 2)
        three='X' if X[3]==1 else ('O' if O[3]==1 else 3)
        four='X' if X[4]==1 else ('O' if O[4]==1 else 4)
        five='X' if X[5]==1 else ('O' if O[5]==1 else 5)
        six='X' if X[6]==1 else ('O' if O[6]==1 else 6)
        seven='X' if X[7]==1 else ('O' if O[7]==1 else 7)
        eight='X' if X[8]==1 else ('O' if O[8]==1 else 8)
        
        print(f"{zero} | {one} | {two}")
        print('--|---|--')
        print(f'{three} | {four} | {five}')
        print('--|---|--')
        print(f'{six} | {seven} | {eight}')

   
    def checkwin(X,O):
        win_indexlist=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] 
        for i in win_indexlist:
            a,b,c=i
            if X[a]+X[b]+X[c]==3:
                print('X won the game')
                return True
            if O[a]+O[b]+O[c]==3:
                print('O won the game')
                return True
        return False

    X=[0 for i in range(9)]
    O=[0 for i in range(9)]
    game(X,O)

    turn=1
    count=9
    print('\nUsers are allowed to enter the value from 0 - 8 as shown in the figure\n')
    while count > 0:
        if turn==1:
            print("\nX's turn")
            index=int(input('Enter value : '))
            X[index]=1
            game(X,O)
            turn = 0
        else:
            print("\nO's turn ")
            index=int(input("Enter value : "))
            O[index]=1
            game(X,O)
            turn = 1
        count=count-1
        if checkwin(X,O) == True:
            print('Game over ')
            break
