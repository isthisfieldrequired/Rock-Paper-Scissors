import random

options = ("R","P","S")
rules = {
    "R":"S",
    "P":"R",
    "S":"P"
    }

userwins = int(0)
gamecount = int(0)
draws = int(0)


user = input("R/P/S?")
while user != "N":
    try: #Input check
        assert user in options
    except:
        print(
            "invalid selection, try again\n-------------------------------------\n"
            )
    else:
        comp = options[random.randint(0,2)]
        if user == comp:
            print("It was a draw! This round doesn't count.")
            draws += 1
        elif rules.get(user) == comp:
            print("You won! Computer chose {}".format(comp))
            userwins += 1
            gamecount += 1
        else:
            print("You lost! Computer chose {}".format(comp))
            gamecount += 1
        if userwins > gamecount/2: #user is winning game
            print(
                "You're winning {} out of {} round(s) but I bet I'll win best out of {}!"
                .format(userwins, gamecount,userwins*2+1)
                )
        elif userwins < gamecount/2: #user is losing game
            print(
                "I'm winning, {} of {} rounds ({} drawn)."
                .format(gamecount-userwins, gamecount, draws)
                )
        else: #if even
            print(
                "We are tied with {} wins out of {} round(s) ({} drawn)."
                .format(userwins, gamecount, draws)
                )


        print(
            "--------------------End of Round {}, {} if you cout the draws--------------------\n"
              .format(userwins, gamecount+draws)
              )
    finally:
            user = input("R/P/S? or N to quit")



            #Feature request:
            #github
            #stats - speed, %R/P/S (user and comp)
            #r...P...S... with delay
            #GUI
            #Keyboard Stting
            #Game mode - speed - Automatically change game speed depending on user
