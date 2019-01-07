import random
flag=0
x=0
while(flag==0):
    options = ["rock", "paper", "scissor", "lizard", "spock"]
    comp =random.choice(options)
    user = input("Pick your choice ------> ")
    user=user.lower()
    print("comp choice is ----> ",comp)
    print("\n")
    if user == "rock":
        if (comp == "paper" or comp == "spock"):
            print("YOU LOSE")
            x=x-1
        elif comp=="lizard" or comp=="scissor":
            print("YOU WIN")
            x=x+1
        else:
            print("TIE")

    elif user == "paper":
        if comp=="scissor" or comp=="lizard":
            print("YOU LOSE")
            x=x-1
        elif comp=="rock" or comp=="spock":
            print("YOU WIN")
            x=x+1
        else:
            print("TIE")

    elif user == "scissor":
        if comp=="rock" or comp=="spock":
            print("YOU LOSE")
            x=x-1
        elif comp=="paper" or comp=="lizard":
            x=x+1
            print("YOU WIN")
        else:
            print("TIE")

    elif user == "lizard":
        if comp=="rock" or comp=="scissor":
            print("YOU LOSE")
            x=x-1
        elif comp=="paper" or comp=="spock":
            print("YOU WIN")
            x=x+1
        else:
            print("TIE")

    elif user == "spock":
        if comp=="paper" or comp=="lizard":
           print("YOU LOSE")
           x=x-1
        elif comp=="rock" or comp=="scissor":
           print("YOU WIN")
           x=x+1
        else:
           print("TIE")
    print("\nSCORE : ",x)
    c=input("Wanna go again? [Y/N] ")
    if c=="Y":
        flag=0
        print("\n\n")
        continue
    else:
        break






    
        
   
 


   
   

   