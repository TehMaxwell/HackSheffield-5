# -*- coding: utf-8 -*-
"""
A simple black jack game to test the NN against.
"""
#MODULES
import numpy
import random
from keras.models import load_model
import os, sys

#DEFINITIONS
numberOfHands = 100

#FUNCTIONS
def playerHand(deck, playerCount, playerBusts):
    playerPlaying = True

    #While the player has not stuck
    while playerPlaying:
        playerCount += deck.pop()
        print("Player Count: {}".format(playerCount))

        if playerCount <= 21:
#             if playerCount < 17:
#                 playerPlaying = True
#             else:
#                 playerPlaying = False
#             '''
            inputWrong = True
            while inputWrong:
                #Getting the Players Decision
                decision = input("(S)tick or (T)wist: ").upper()

                #Processing the players decision
                if decision == "T":
                    playerPlaying = True
                    inputWrong = False
                elif decision == "S":
                    playerPlaying = False
                    inputWrong = False
                else:
                    inputWrong = True
        else:
             print("Player Bust with {}".format(playerCount))
             playerPlaying = False
             playerBusts += 1

    return playerCount, playerBusts

def machineHand(deck, model, machineCount, machineBusts):
    machinePlaying = True

    #While the player has not stuck
    while machinePlaying:
        machineCount += deck.pop()
        print("Machine Count: {}".format(machineCount))

        if machineCount <= 21:
            #Getting the Machines Decision
            prediction = model.predict([machineCount])

            #Processing the players decision
            if prediction[0] >= 0.3:
                machinePlaying = True
            else:
                machinePlaying = False
        else:
            print("Machine Bust with {}".format(machineCount))
            machinePlaying = False
            machineBusts += 1

    return machineCount, machineBusts

#MAIN CODE
#Importing the Machine Learing Model
NN = load_model("blackjackGauss.h5")

#For all hands
handCount = 0
playerWins = 0
machineWins = 0
ties = 0
playerBusts = 0
machineBusts = 0

sys.stdout.flush()
print("""\
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%,,...,,....,.,,,..   ,(((###%#%%%######%##%%#%#%%################((/.,*,*/#%((@@&@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/,.....,,.,,.,,,.   .//(#####%%%%%#%#%%####%%%#%##%%###%############(#/, .,*,//(#@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*,...,. ..,,,....   ,/((##########%%%%###%%#%%%%%#%#######%####%%######(/*..,***,*%&&@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&*,......   ..,   .  ,//(((#######%#%%%%%%%%%%%%%%%%%%%#%###(((**,*,,,,,,(##(,.,,,//*/%#@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/*,. ...    ....    .*/(((((#####%##%%%%%%%%%%%%%%%%%%#%#(**,.... ..,,,,*,**/#(.,,,,(//*(@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(%*...... .. . .    .*//((#(##########%%%%%%%%%%%%%%%####//**,.....*//((((((#%#(#/..,.*/#(##@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*,...., . ..     .,*/((((/****,......,,*,/(#####%#%##(///**,*,,,,*/(((//*//((#%##...,,*/%(#%@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@*.... ..       ..,**///*,,...............,*/*/(((######(//**,,,,*,../#((/...,*(#% ..,,/(/(#@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%...,. .. .   .,***///,....*/(((((((//*//,****///(((####((/***,,,*#%,...%%%/,,,/###%# ..,*/(/#&@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&(,,,,... .   .,*/**/(,..*//(#(#(#(##(#((((/////////(((#####//**(,(#..(   (/*(#(/((##%(..,**/(/%@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%&/.,,... .   .,**/*/(**//(((((/,,..,(((*,*,//////(///(((######/(((//(((//**/((((######%( ,,**/*&@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@(*,,....     .,**/(////(((//*,../%%(*/%%%%*,/(((/((((((########((((#####((#(((##########/ .,**/(#@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&/,*,,....     .,,*/((#(((////,.,&%/..#..*%(/(###(#((((((###########(((################%%%%#..,*./(%@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#(*(/,*,,,. ..  .,,*/##(((/////***//*//(#(((/(#####((((########%%#####((((#################%%%...,.,,/%&@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%*#(***,,,...    .,*(##((((//((##((((/((############((#####(((#%#((/#%%##((##################%#. .,,////@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&(@%/***,,,...    ..*((#(((((#(#######((############(((####((////(/***..***/(##########(((((((%#(...,,#%%&%@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#&@(/*,*,,,.,...   .,/(####(#####################%##((#((#(/*..,,**,  .,,../(((((/((/(((((/(((###*,...,*(#@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@/%/*,,*.,,,.... ..,/(###(######%##################(***/*...,**,...,,,,*/(///////**,*////////((##, ....,,/%@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(//*,,,,..,,....,  ,*(###################%%%########(*.,,**///**//*,.. .. ,,,*****,*,**.,***///(/,... ..,,//
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(/%(**,,. .,, ..,,  .*((############(####%%%##(((####((((/**.... .,*,         ....,..,..,,,**/**,,,.,,....,,*
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%%%(/,.,  .,,...,.  .,((########((((#####%###(//(((((//,*.... .   .*,.        ..... .......,,(/**,.....,.,,,,
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@#%/,.. ...,....,.. .,/(#####(#(((########(/*,,*/****,.,*.  . .. ./((/,,...    .. .     ,..,/***,,...........
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(&*,. ....,. ..,.   .,,/####(##((##(((((/*.*****,,,,.....  . . ,////((((((//*,..   ..,.,,.*/(/,,............
@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@#/&/,... .,.  . .    .,.,((#(##(((//////*........ ....... ..,/(#%%####//////////***//(/**,*(/*,,,............
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&(,,,...,.  . .    . .../*((((/*/****,,... ..    . ...,*(((*/***/*****(*,*,*/////((/(**,(**,,.... .........
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#/**,,,,.   .         .,.,,,.**,*/**,... .      .,,*//////*,,,**,*,,,,***,**///(((((((/*,**................
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%*(*,*,.              . ....,,,,,****,..   ,//(((((//(///,,*/**/**/*,,*,*/(/(((((((/(//**,,.. ...........,*
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&(/#*,*.   .                ..,...,**,*,,../((((((((((((((((((#(((#(**,*///((((((((((///,,....  ...........,
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#(/*,.   .                   ..,,,*,,,,,,,/(((((((((((((((((#(####(*.*//**/////(((((//***...  . ... .....*,,,
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%&%((,,....          .   . .    ..,...,.,,*/*,(###(((((##(#####(((/#(/,*((/*(**,*/**////*,......   ....,..,,*
@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&(/(/*.. .                     .  . . ....,,,,*##((##########(#(//((*////*,//,,,,,..,.,,,. .. ..... .....,,,,
@@@@@@@@@@@@@@@@@@@@@@@@@@%@%%(#(#,,...  .         .            .   .   ..,.**/(########(#///(*/*/**/*,,,//,*,...........      .........,..
@@@@@@@@@@@@@@@@@@@@@@@@&&@(%&&%#(*.,. ..    .                          . . .,*//*/(#(#*((*/***,,,,**,.,,/,,,...... .            ..........
@@@@@@@@@@@@@@@@@@@@@@@@#&%&@(*./. .... .                             .  ......,*(//*,**,,,,..,,*,,,.....,.... .     .        . , .,,%,,,,,
@@@@@@@@@@@@@@@@@@@@@@@@&%&%#%#,*. ..... .                                 .....,*,*,,,,.,,,,.,...... ... .                    .  ..,.,.,,,
@@@@@@@@@@@@@@@@@@@@@@@&@@%/,..,*,.,.,  ..                                .  ... ...,.,...,,,.,.,..                               ....,,.((
@@@@@@@@@@@@@@@@@@@@@@@%&&%@@@@%(*,,,... .                               .    ... ...... ...... .   .                           ....,,(*,/&
@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@#,.#/,,..,                                       . .  ....  . .                               .  ......(%///
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*,*%/*..*.                                                .    .  ..               .             ... ..,*#/&@
@@@@@@@@@@@@@@@@@@@@@@@&@%%/,/%/#*,,#*...   .                               .  .    . .                                        ..,,,,,.,*(/
@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&(#*/%%*/....                          .     .                                                .. ....,((,. ,*/
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(/.,...                                           .     .                               ..., ,*#%(/*.,,
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%/.,... /.    .*      .                                                                 .  ...*%##/#&&&

""")
print("Jack Black, the Blackjack Hack Neural Network Machine Learning AI Big Data Deep Learning Algorithm driven by Data Science and Statistical Backgropogation!")

while handCount <= numberOfHands:
    sys.stdout.flush()
    print("-----------------------------------")
    print("New Hand!")

    #Generating a new deck of cards
    deck = []
    for suit in range(0, 4):
        for card in range (1, 14):
            if card >= 11:
                card = 10
            deck.append(card)


    #Shuffling the Deck
    random.shuffle(deck)
    random.shuffle(deck)
    random.shuffle(deck)

    #Picking if the player or the machine goes first
    playerOrMachine = numpy.random.randint(0, high = 2, size = 1)

    playerCount = 0
    machineCount = 0

    playerCount += deck.pop()
    machineCount += deck.pop()

    #Player First
    if playerOrMachine == 1:
        playerCount, playerBusts = playerHand(deck, playerCount, playerBusts)
        print("\n")
        if playerCount > 21:
            machineWins += 1
            print("\n $$ Jack Black Wins! $$")
            print ("You must never underestimate the power of the eyebrow.")

        else:
            machineCount, machineBusts = machineHand(deck, NN, machineCount, machineBusts)

            if machineCount > 21:
                playerWins += 1
                print("\n $$ Player Wins! $$")
            elif playerCount > machineCount:
                playerWins += 1
                print("\n $$ Player Wins! $$")
            elif machineCount > playerCount:
                machineWins += 1
                print("\n $$ Jack Black Wins! $$")
                print("I'd rather be the King of Kids, than the prince of fools.")
            else:
                ties += 1

    #Machine First
    else:
        machineCount, machineBusts = machineHand(deck, NN, machineCount, machineBusts)
        print("\n")
        if machineCount > 21:
            playerWins += 1
            print("\n $$ Player Wins! $$")

        else:
            playerCount, playerBusts = playerHand(deck, playerCount, playerBusts)

            if playerCount > 21:
                machineWins += 1
                print("\n$$ Jack Black Wins! $$")
                print("You have to mind your P's and Q's a little bit.")
            elif playerCount > machineCount:
                playerWins += 1
                print("\n $$ Player Wins! $$")
            elif machineCount > playerCount:
                machineWins += 1
                print("\n $$ Jack Black Wins! $$")
                print("I am Tenacious.")
            else:
                ties += 1

    print("\nSCOREBOARD:")
    print("Machine Wins: {}".format(machineWins))
    print("Player Wins: {}".format(playerWins))
    print("Ties: {}".format(ties))
    print("Machine Busts: {}".format(machineBusts))
    print("Player Busts: {}\n".format(playerBusts))

    print("-----------------------------------")
