# BlackJack for Python Bootcamp For Jose Portilla
import random

class Player:
    
    def __init__(self,name,bet,num):
        self.name=name
        self.bet=bet
        self.hand=[]
        self.num=num
        
    
    def addcard(self):
        while True:
            c=random.choice(list(cards.keys()))+" of "+random.choice(types)
            if (c not in self.hand) and (c not in cardstable):
                self.hand.append(c)
                cardstable.append(c)
                break
    def calc_hand(self):
        s=0
        for i in self.hand:
            if i[0:2]=="10":
                s+=10
            elif i[0]!="A":
                s+=int(cards[i[0]])
            else:
                s+=int(input("Player{} For the value of A, do you want 1 or 11: ".format(self.num)))
        return s
    
    def checkfor21(self):
        if self.calc_hand()==21:
            self.bet+=(3/2)*self.bet
            return True
        
        return False
    
    def checkforgreater21(self):
        if self.calc_hand()>21:
            self.bet=0
            return True
        
        return False
    


cards={'A':[1,11], '1':1, '2':2, '3':3, "4":4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
types=["Hearts", "Diamonds", "Spades", "Clubs"]
cardstable=[]
playerstable=[]

nplays=int(input("How many players: "))
#First round of cards being given out
if(nplays>=1):
    print("Player1")
    name=input("Name of the player: ")
    bet=int(input("Please place your bets! "))
    player1=Player(name,bet,1)
    player1.addcard()
    print(player1.hand[0])
    playerstable.append(player1)
    
print("\n")
    
if(nplays>=2):
    print("Player2")
    name=input("Name of the player: ")
    bet=int(input("Please place your bets! "))
    player2=Player(name,bet,2)
    player2.addcard()
    print(player2.hand[0])
    playerstable.append(player2)
   
print("\n")

if(nplays>=3):
    print("Player3")
    name=input("Name of the player: ")
    bet=int(input("Please place your bets! "))
    player3=Player(name,bet,3)
    player3.addcard()
    print(player3.hand[0])
    playerstable.append(player3)

print("\n")

print("Dealer")
dealer=Player("Dealer",0,0)
dealer.addcard()
print(dealer.hand[0])
print("\n")

#Second round of cards being given out
if(nplays>=1):
    print("Player1")
    player1.addcard()
    print(player1.hand[0])
    print(player1.hand[1])
    
print("\n")

if(nplays>=2):
    print("Player2")
    player2.addcard()
    print(player2.hand[0])
    print(player2.hand[1])
    
print("\n")

if(nplays>=3):
    print("Player3")
    player3.addcard()
    print(player3.hand[0])
    print(player3.hand[1])
    
print("\n")
    
print("Dealer has received the second card faced down.")
dealer.addcard()

#Check for bust/21
for i in range(0,len(playerstable)):
    if playerstable[i].checkfor21():
        print("Player{} has a 21 which is a bust. You receive 1 and half times your bet!".format(playerstable[i].num))
        playerstable[i]=""

#Ask for hit or stay till they say no
for i in range(0,len(playerstable)):
    H_S=input("Player{}, do you want to hit or stay? Press h for hit and s for stay: ".format(playerstable[i].num))
    while H_S == "h" or H_S == "H" or H_S == "hit":
        playerstable[i].addcard()
        
        if playerstable[i].checkfor21():
            print("Player{} has a 21. You receive 1 and half times your bet!".format(playerstable[i].num))
            print(playerstable[i].hand[-1])
            playerstable[i]=""
            break
            
        elif playerstable[i].checkforgreater21():
            print("Player{} has a hand that is greater than 21 which is a bust. You are out of the game! Your bet will be taken away by the dealer ".format(playerstable[i].num))
            print(playerstable[i].hand[-1])
            playerstable[i]=""
            
            break
        print(playerstable[i].hand[-1])
        H_S=input("Player{}, do you want to hit or stay? Press h for hit and s for stay: ".format(playerstable[i].num))

        
#Reveal dealer's cards
print("The dealer's second card is: {}".format(dealer.hand[-1]))
    #If it is 16 or under, the dealer takes another card
while dealer.calc_hand()<17:
    dealer.addcard()
    print("Dealer's initial hand was under sixteen hence the dealer took another card: {}".format(dealer.hand[-1]))
    if dealer.calc_hand()>21:
        print("Dealer got busted, everyone gets twice their bet")
        for i in playerstable:
            if i !="":
                i.bet*=2
    #If it is 17 or higher then the dealer stays with the hand
    #If the dealer busts then everyone gets 2*bet
    #If the player has a higher hand than the dealer then gets 2*bets otherwise equal or lower then bet gets taken away

for i in range(0,len(playerstable)):
    if playerstable[i]!="":
        sumplayers=playerstable[i].calc_hand()
    sumdealer=dealer.calc_hand()
    if sumplayers>sumdealer and playerstable[i]!="":
        playerstable[i].bet*=2
    elif playerstable[i]!="":
        playerstable[i].bet=0
        print("Player{} has a lower hand than the dealer hence your bet has been taken away".format(playerstable[i].num))
        

for i in range(0,len(playerstable)):
    if playerstable[i]!="":
        print("Player{} has: {}".format(playerstable[i].num,playerstable[i].bet))
        

    
    
    
    
    
    




