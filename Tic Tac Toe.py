# Tic Tac Toe Game for Python Bootcamp By Jose Portilla

def printrules():
    i=0
    while i<=6:
        print(f"{i+1} | {i+2} | {i+3} ")
        if i!=6:
            print("_________")
        i+=3
        
def checkforwin():
    if (l[0]==l[1]==l[2]=='X' or l[0]==l[1]==l[2]=='O') or (l[2]==l[5]==l[8]=='X' or l[2]==l[5]==l[8]=='O') or (l[6]==l[7]==l[8]=='X' or l[6]==l[7]==l[8]=='O') or (l[0]==l[3]==l[6]=='X' or l[0]==l[3]==l[6]=='O') or (l[0]==l[4]==l[8]=='X' or l[0]==l[4]==l[8]=='O') or (l[2]==l[4]==l[6]=='X' or l[2]==l[4]==l[6]=='O') or (l[3]==l[4]==l[5]=='X' or l[3]==l[4]==l[5]=='O') or (l[1]==l[4]==l[7]=='X' or l[1]==l[4]==l[7]=='O'):
        return True
    else:
        return False
        
def printboard(k):
    flag=0
    while flag!=1:
        turn=int(input("Click the number where you want to put the cross or circle : "))
        if turn not in turnlist:
            flag=1
            turnlist.append(turn)
        else:
            print("Try again!")
    if k==1:
        l[turn-1]='X'
    else:
        l[turn-1]='O'
    i=0
    while i<=6:
        print(f"{l[i]} | {l[i+1]} | {l[i+2]} ")
        if i!=6:
            print("_________")
        i+=3
    if checkforwin():
        if k==1:
            print("Player 1 wins")
            return 'yes'
        if k==2:
            print("Player 2 wins")
            return 'yes'
    else:
        return 'no'
    

    
# Main
i=0
choice='yes'
printrules()
global l
l=[' ']*9
global turnlist
turnlist=[]
win='no'
while choice=='yes':
    while i<9 and win=='no':
        print("Player 1 goes and has cross")
        i+=1
        win=printboard(1)
        if win=='yes':
            break
        if i<9:
            print("Player 2 goes and has circle")
            i+=1
            win=printboard(2)
        if win=='no' and i>=9:
            print("DRAW!")
    
    i=0
    win='no'
    choice=input("Do you want to play again? (yes/no) : ")
    l=[' ']*9
    