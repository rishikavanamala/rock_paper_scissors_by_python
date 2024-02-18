import random
def abc():
    uin=int(input("enter rock-1,paper-2,scissor-3"))
    if(uin==1):
        uin='rock'
    elif uin==2:
        uin='paper'
    elif uin==3:
        uin='scissor'
    else:
        print("invalid input, enter ur option again")
        abc()
    return uin
times=int(input("enter the number of turns you want to play,prefer odd number to avoid draw"))
while(times):
    user=abc()
    userscore=0
    computerscore=0
    a=['rock','paper','scissor']
    comp=random.choice(a)
    print("you choosen ",user,"your opponent was choosen"+comp)
    if(user==comp):
        print("game was draw,scores was added to both")
        userscore=userscore+1
        computerscore=computerscore+1
    else:
        if(user==a[0]):
            if(comp==a[1]):
                computerscore=computerscore+1
            else:
                userscore=userscore+1
        elif(user==a[1]):
            if(comp==a[0]):
                userscore=userscore+1
            else:
                computerscore=computerscore+1
        elif(user==a[2]):
            if(comp==a[0]):
                 computerscore=computerscore+1
            else:
                userscore=userscore+1
    times=times-1
print("your score=",userscore)
print("computer score=",computerscore)
if(userscore>computerscore):
    print("congratulations you won")
elif(userscore<computerscore):
    print("u lost")
else:
    print("draw")


