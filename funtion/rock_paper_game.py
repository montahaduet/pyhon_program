# rock paper scissors
print("what do you want to choose? rock ,paper or scissors")
p1=input()
print("what do you want to choose? rock, paper or scissors")
p2=input()

def game(a,b):
    if a==b:
        return "It's a tite!"
    elif a=='rock':
        if b=='scissors':
            return "rock beats scissors!"
        else:
            return "paper beats rock!"
    elif a=='scissors':
        if b=='paper':
            return "scissors beats paper!"
        else:
            return "rock beats scissors!"
    elif a=='paper':
        if b=='rock':
            return "paper beats rock!"
        else:
            return "scissors beats paper!"
    else:
        return "you have not entered rock,paper or scissors!"
print(game(p1,p2))    
