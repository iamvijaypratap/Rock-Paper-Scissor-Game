import random
def Game(comp,you):
        if comp==you:
            return None
        elif comp=="rock":
             if you=="paper":
                return True
             if you=="scissors":
                return False

        elif comp=="paper":
             if you=="scissors":
                return True
             if you=="rock":
                return False

        elif comp=="scissors":
             if you=="rock":
                return True
             if you=="paper":
                return False
while True:        
                welcome_msg= '''                                              Hello Users
                                ***Welcome To Rock , Paper , Scissors***   :
    *Instructions ---> A player who decides to choose rock will beat another player who has chosen scissors ("rock crushes scissors" ),
                               but will lose to one who has Chosen paper ("paper covers rock") .
                 if you chose paper will lose to Another player who chosen scissors ("scissors cuts paper").
                                      Let's PLAY : PLEASE CHOOSE BETWEEN ROCK PAPER AND SCISSORS '''
                print(welcome_msg)
                randNo = random.randint(1, 3)
                if randNo == 1:
                   comp = "rock" 
                elif randNo == 2:
                   comp = "paper"
                elif randNo == 3:
                   comp = "scissors"   
                you = (input("Your Turn: Rock, Paper, or Scissors:\n"))
                print(f"Computer choose : {comp}")
                print(f"You choose {you}")
                if Game(comp,you)== None:
                   print("THIS IS A TIE")
                elif Game(comp,you) == True:
                   print("Congratulations ,You Win")
                else:
                   print("AHH You Loose")
                user = input("Do You Want To Play Again Y/N : \n")
                if user == "y" or user =="Y":
                    continue
                else:
                    print("Thank You For Playing COME BACK SOON")
                    break
             