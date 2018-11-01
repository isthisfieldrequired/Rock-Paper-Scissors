#Feature request:

    #stats - user input speed, %R/P/S (user and comp)
    #external db integration
    #GUI

import random # for computer random selection
import time # for gamplay animations

shortcutlegend = {
    "Q":"Rock",
    "W":"Paper",
    "E":"Scissor",
    "R":"Rock",
    "P":"Paper",
    "S":"Scissor"
    }  #Legend for easy play so user doesn't hunt for keys
options = ("Rock","Paper","Scissor")
keys = shortcutlegend.keys()
rules = {
    "Rock":"Scissor",
    "Paper":"Rock",
    "Scissor":"Paper"
    }

userwins = int(0)
gamecount = int(0)
draws = int(0)
user =str ()
duration = []

def userchoice():
    global user
    user = str(input("Rock, Paper, Or Scissor? or N to quit"))


#How to play
print(
    '''--------------------------------------------------------------------------
Welcome or Rock Paper Scissors Version 2!
You may either type {} or use the shortcuts as: {} as shortcut.  Good luck!
--------------------------------------------------------------------------'''
    .format(options, shortcutlegend)
    )
#begin game
while user != "N":
    start_time = time.time()
    userchoice()
    end_time = time.time()
    duration.append(end_time-start_time)
    user = user.upper()
    if user in shortcutlegend:
        user = shortcutlegend.get(user)
#User Input check
    try:
        assert user in options
    except:
        print(
            '''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Invalid selection, you may only use {} try again

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
            .format(keys)
            )
        userchoice()
#Computer chooses and who won?
    else:
        print("Rock")
        def sleeptime():
            time.sleep(min(duration[-1]/5,2))
        print("Paper")
        sleeptime()
        print("Scissor")
        sleeptime()
        print ("and...")
        comp = options[random.randint(0,2)]
        sleeptime()
        print ("I choose {}\n" .format(comp))
        sleeptime()
        if user == comp:
            print("It was a draw! This round doesn't count.")
            draws += 1
        elif rules.get(user) == comp:
            print("You won! {} beats {}".format(user,comp))
            userwins += 1
            gamecount += 1
        else:
            print("You lost! {} beats {}".format(comp,user))
            gamecount += 1

#print summary
        if userwins > gamecount/2: #user is winning game
            print(
                "So far, you're winning {} out of {} round(s) but I bet I'll win best out of {}!"
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
        if len(duration) == 1:
            print ("It took you {} seconds to answer".format(duration))            
        elif duration[-1] == duration[-2]:
            print ("it took you {} seconds to answer, exactly the same as last time! Woah!".format(duration))
        elif duration[-1] > duration[-2]:
            print ("You are slowing down!  It took you {} more seconds than last time to answer".format(duration[-1]-duration[-2]))
        else:
            print ("You are speeding up!  It took you {} less seconds than last time to answer".format(duration[-2]-duration[-1]))
        print(
            "--------------------End of Round {}, {} if you cout the draws--------------------\n"
              .format(userwins, gamecount+draws)
              )
