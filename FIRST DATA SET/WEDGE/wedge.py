

#   cardDeck      represent existence of card 2d array boolean
#   13*4        array where the first index is the suit(row) and the second index is the column(card value)
#   cardValue   represents the names of the cards ACE -> KING, used to name card taken from deck
#   cardSuit

#def initDeck(cardDeck, numColumns, numRows):
    # This function receives an empty list and the number of suits and card values
    # and returns the cardNumber back to the maximum and resets deck to true
    #print('initDeck')
    #return(cardDeck, numValues, numSuits)

import random
import time

NUM_VALUES = 13
NUM_SUITS = 4
NUM_CARDS = NUM_VALUES * NUM_SUITS
CARD_VALUE = ['ACE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING', 'ACE']
CARD_TYPE = ['CLUB', 'DIAMOND', 'HEART', 'SPADE']

ANTE = 1

def INIT_DECK():
    #This function receives nothing
    #and returns a NUM_VALUES * NUM_SUITS 2D array, with every value being True
    CARD_DECK = [[True for i in range(NUM_VALUES)] for j in range(NUM_SUITS)]
    return CARD_DECK

def BUBBLE_SORT(CARD_ONE, CARD_TWO):
    #This function receives the first and second card
    #and puts them in an array
    #and runs a modified bubblesort to sort the cards into ascending order
    #and returns the first and second card
    #(the value and suits might be opposite of what they were before, if they needed to be sorted)
    CARD_VALUES = [int(CARD_ONE[0]), int(CARD_TWO[0])]
    l = len(CARD_VALUES)
    for i in range(l):
        SWITCHED = False
        for j in range(l - i - 1):
            if CARD_VALUES[j] > CARD_VALUES[j + 1]:
                CARD_VALUES[j], CARD_VALUES[j + 1] = CARD_VALUES[j + 1], CARD_VALUES[j]
                CARD_ONE[1], CARD_TWO[1] = CARD_TWO[1], CARD_ONE[1]
                SWITCHED = True
        if not SWITCHED:
            CARD_ONE[0], CARD_TWO[0] = str(CARD_VALUES[0]), (CARD_VALUES[1])
            return CARD_ONE, CARD_TWO


def GET_CARD(NUM_DRAWN, CARDS_DRAWN, CARD_DECK):
    #This function receives the number of cards that have been requested, the total cards that have been drawn, and the
    #deck of cards that determines whether the card has already been drawn
    #and runs a loop NUM_DRAWN times
    #in this loop, a random card is drawn if it exists in the deck (using CARD_DECK)
    #if NUM_CARDS (52) cards have been drawn from the deck, the deck is reset
    #and returns the new total cards that have been drawn, the value/suit of the cards that have been drawn in an array
    #and the deck of cards, with drawn cards being flipped to False in the 2D array
    CARD_RETURN = []
    for i in range(NUM_DRAWN):
        CARD_FOUND = False

        while not CARD_FOUND:
            x = random.randint(0, 3)
            y = random.randint(0, 12)
            if CARD_DECK[x][y]:
                CARD_RETURN.append(str(y) + ' ' + str(x))
                CARD_DECK[x][y] = False
                CARD_FOUND = True
                CARDS_DRAWN += 1

        if CARDS_DRAWN == NUM_CARDS:
            CARD_DECK = INIT_DECK()
            CARDS_DRAWN = 0
    return CARDS_DRAWN, CARD_RETURN, CARD_DECK

def COLLECT_ANTE(PLAYER_ONE_BAL, PLAYER_TWO_BAL, POT):
    #This function receives player one's balance, player two's balance, and the number of chips in the pot
    #and if the pot is empty, collects the ante from each player, and prints balances
    #if the pot is not empty, prints balances
    #and returns player one's new balance, player two's new balance, and the new number of chips in the pot
    if POT == 0:
        time.sleep(1)
        print('\nTHE ANTE IS ' + str(ANTE) + ' CHIP')
        if PLAYER_ONE_BAL != 1:
            time.sleep(1)
            print('\nPLAYER ONE HAS ' + str(PLAYER_ONE_BAL) + ' CHIPS')
        else:
            time.sleep(1)
            print('\nPLAYER ONE HAS ' + str(PLAYER_ONE_BAL) + ' CHIP')

        if PLAYER_TWO_BAL != 1:
            time.sleep(1)
            print('PLAYER TWO HAS ' + str(PLAYER_TWO_BAL) + ' CHIPS')
        else:
            time.sleep(1)
            print('PLAYER TWO HAS ' + str(PLAYER_TWO_BAL) + ' CHIP')

        if PLAYER_ONE_BAL > 0:
            time.sleep(1)
            print('\nPLAYER ONE HAS PAID THE ANTE')
            PLAYER_ONE_BAL = PLAYER_ONE_BAL - 1
            POT = POT + 1
        else:
            time.sleep(1)
            print('\nPLAYER ONE HAS NO MORE MONEY')
        if PLAYER_TWO_BAL > 0:
            time.sleep(1)
            print('PLAYER TWO HAS PAID THE ANTE')
            PLAYER_TWO_BAL = PLAYER_TWO_BAL - 1
            POT = POT + 1
        else:
            time.sleep(1)
            print('PLAYER TWO HAS NO MORE MONEY')
    else:
        if PLAYER_ONE_BAL != 1:
            time.sleep(1)
            print('\nPLAYER ONE HAS ' + str(PLAYER_ONE_BAL) + ' CHIPS')
        else:
            time.sleep(1)
            print('\nPLAYER ONE HAS ' + str(PLAYER_ONE_BAL) + ' CHIP')

        if PLAYER_TWO_BAL != 1:
            time.sleep(1)
            print('PLAYER TWO HAS ' + str(PLAYER_TWO_BAL) + ' CHIPS')
        else:
            time.sleep(1)
            print('PLAYER TWO HAS ' + str(PLAYER_TWO_BAL) + ' CHIP')
    return PLAYER_ONE_BAL, PLAYER_TWO_BAL, POT

def QUIT(PLAYER_ONE_BAL, PLAYER_TWO_BAL):
    #This function receives player one's balance and player two's balance
    #and prints out the final balances of the players, and the results of the game (who won)
    #and returns nothing
    time.sleep(1)
    if PLAYER_ONE_BAL == 1:
        print('\nPLAYER ONE ENDED WITH 1 CHIP')
    else:
        print('\nPLAYER ONE ENDED WITH ' + str(PLAYER_ONE_BAL) + ' CHIPS')
    time.sleep(1)
    if PLAYER_TWO_BAL == 1:
        print('PLAYER TWO ENDED WITH 1 CHIP')
    else:
        print('PLAYER TWO ENDED WITH ' + str(PLAYER_TWO_BAL) + ' CHIPS')
    time.sleep(1)
    if PLAYER_ONE_BAL > PLAYER_TWO_BAL:
        print('\nPLAYER ONE WON')
    elif PLAYER_TWO_BAL > PLAYER_ONE_BAL:
        print('\nPLAYER TWO WON')
    else:
        print('\nTHE GAME WAS A TIE')

def CHECK_ACE(TURN, CARD_ONE, CARD_TWO):
    #This function receives whose turn it is, the suit/value of the first card drawn,
    #and the suit/value of the second card drawn
    #and checks if either of them is an ace
    #if only one of them is an ace, asks whether the player would like it to be high/low
    #and assigns a new value to the card's value.
    #it can be 13 because the thirteenth index in the list of card values is also set to 'ACE'
    #if both are aces, automatically sets one to high and one to low
    #returns the first and second card, regardless of if they have changed
    if int(CARD_ONE[0]) == 0 and int(CARD_TWO[0]) == 0:
        CARD_TWO[0] == '13'
    elif int(CARD_ONE[0]) == 0:
        VALID_RESPONSE = False
        while not VALID_RESPONSE:
            time.sleep(1)
            if TURN:
                print('\nPLAYER ONE: ACE HIGH OR LOW')
            else:
                print('\nPLAYER TWO: ACE HIGH OR LOW')
            INPUT = input().upper()
            if INPUT == 'HIGH':
                CARD_ONE[0] = '13'
                VALID_RESPONSE = True
            elif INPUT == 'LOW':
                CARD_ONE[0] = '0'
                VALID_RESPONSE = True
    elif int(CARD_TWO[0]) == 0:
        VALID_RESPONSE = False
        while not VALID_RESPONSE:
            time.sleep(1)
            if TURN:
                print('\nPLAYER ONE: ACE HIGH OR LOW')
            else:
                print('\nPLAYER TWO: ACE HIGH OR LOW')
            INPUT = input().upper()
            if INPUT == 'HIGH':
                CARD_TWO[0] = '13'
                VALID_RESPONSE = True
            elif INPUT == 'LOW':
                CARD_TWO[0] = '0'
                VALID_RESPONSE = True
    return CARD_ONE, CARD_TWO

def DEAL_CARD(PLAYER_ONE_BAL, PLAYER_TWO_BAL,TURN, CARDS_DRAWN, CARD_DECK):
    #This function receives player one's balance, player two's balance, the turn, the number of cards that have been drawn, and the deck of cards
    #and takes an input, either DEAL or QUIT (case ignored)
    #if the input is DEAL, gets, prints, sorts, and returns the cards
    #if the input is quit, triggers a quit sequence that ends the program
    CORRECT_RESPONSE = False
    while not CORRECT_RESPONSE:
        if TURN:
            print('\nPLAYER ONE: TYPE \'DEAL\' TO GET DEALT CARDS, TYPE \'QUIT\' TO QUIT')
        else:
            print('\nPLAYER TWO: TYPE \'DEAL\' TO GET DEALT CARDS, TYPE \'QUIT\' TO QUIT')
        INPUT = input().upper()
        if INPUT == 'DEAL':
            time.sleep(1)
            CARDS_DRAWN, CARDS_RECEIVED, CARD_DECK = GET_CARD(2, CARDS_DRAWN, CARD_DECK)
            CARD_ONE, CARD_TWO = BUBBLE_SORT(CARDS_RECEIVED[0].split(), CARDS_RECEIVED[1].split())

            print('\n' + CARD_VALUE[int(CARD_ONE[0])] + ' OF ' + CARD_TYPE[int(CARD_ONE[1])] + 'S')
            print(CARD_VALUE[int(CARD_TWO[0])] + ' OF ' + CARD_TYPE[int(CARD_TWO[1])] + 'S')
            CARD_ONE, CARD_TWO = CHECK_ACE(TURN, CARD_ONE, CARD_TWO)
            return CARDS_DRAWN, CARD_DECK, CARD_ONE, CARD_TWO
        elif INPUT == 'QUIT':
            QUIT(PLAYER_ONE_BAL, PLAYER_TWO_BAL)
            return -1, -1, -1, -1

def CHECK_CASE(CARD_ONE, CARD_TWO, POT, TURN, PLAYER_ONE_BAL, PLAYER_TWO_BAL):
    #Receives the two cards, the pot, whose turn it is, and the player balances
    #and checks which case the player's two cards fall under
    #and returns the bet, the balances, and the pot
    BET = 0
    if str(CARD_ONE[0]) == str(CARD_TWO[0]):
        POT = POT - 2
        time.sleep(1)
        if TURN:
            PLAYER_ONE_BAL = PLAYER_ONE_BAL + 2
            print('\nPLAYER ONE WON 2 CHIPS')
        else:
            PLAYER_TWO_BAL = PLAYER_TWO_BAL + 2
            print('\nPLAYER TWO WON 2 CHIPS')
    elif abs(int(CARD_ONE[0]) - int(CARD_TWO[0])) == 1:
        time.sleep(1)
        if TURN:
            print('\nPLAYER ONE CANNOT BET')
        else:
            print('\nPLAYER TWO CANNOT BET')
    else:
        VALID_RESPONSE = False
        while not VALID_RESPONSE:
            time.sleep(1)
            if TURN:
                if POT < PLAYER_ONE_BAL:
                    print('\nPLAYER ONE: HOW MANY CHIPS WOULD YOU LIKE TO BET (0 -> ' + str(POT) + ')')
                else:
                    print('\nPLAYER ONE: HOW MANY CHIPS WOULD YOU LIKE TO BET (0 -> ' + str(PLAYER_ONE_BAL) + ')')
            else:
                if POT < PLAYER_TWO_BAL:
                    print('\nPLAYER TWO: HOW MANY CHIPS WOULD YOU LIKE TO BET (0 -> ' + str(POT) + ')')
                else:
                    print('\nPLAYER TWO: HOW MANY CHIPS WOULD YOU LIKE TO BET (0 -> ' + str(PLAYER_TWO_BAL) + ')')
            INPUT = input()
            if TURN:
                if INPUT.isdigit() and int(INPUT) <= POT and int(INPUT) <= PLAYER_ONE_BAL:
                    BET = int(INPUT)
                    VALID_RESPONSE = True
            else:
                if INPUT.isdigit() and int(INPUT) <= POT and int(INPUT) <= PLAYER_TWO_BAL:
                    BET = int(INPUT)
                    VALID_RESPONSE = True
    return BET, PLAYER_ONE_BAL, PLAYER_TWO_BAL, POT

def IN_BETWEEN(BET, POT, TURN, CARD_ONE, CARD_TWO, CARD_THREE, PLAYER_ONE_BAL, PLAYER_TWO_BAL):
    #Receives the bet, pot, whose turn it is, the value of all three cards, and the player balances
    #if the player has made a bet, checks if the third card is in between the first two, and awards chips accordingly
    #and returns the pot, player balances
    if BET > 0:
        if TURN:
            print('\nPLAYER ONE DREW THE ' + CARD_VALUE[int(CARD_THREE[0])] + ' OF ' + CARD_TYPE[
                int(CARD_THREE[1])] + 'S')
        else:
            print('\nPLAYER TWO DREW THE ' + CARD_VALUE[int(CARD_THREE[0])] + ' OF ' + CARD_TYPE[
                int(CARD_THREE[1])] + 'S')
        if int(CARD_ONE[0]) < int(CARD_THREE[0]) < int(CARD_TWO[0]) or int(CARD_TWO[0]) < int(CARD_THREE[0]) < int(
                CARD_ONE[0]):
            time.sleep(1)
            if TURN:
                if BET == 1:
                    print('\nPLAYER ONE WON 1 CHIP')
                else:
                    print('\nPLAYER ONE WON ' + str(BET) + ' CHIPS')
                PLAYER_ONE_BAL = PLAYER_ONE_BAL + BET
            else:
                if BET == 1:
                    print('\nPLAYER TWO WON 1 CHIP')
                else:
                    print('\nPLAYER TWO WON ' + str(BET) + ' CHIPS')
                PLAYER_TWO_BAL = PLAYER_TWO_BAL + BET
            POT = POT - BET
        else:
            time.sleep(1)
            if TURN:
                if BET == 1:
                    print('\nPLAYER ONE PUT 1 CHIP IN THE POT')
                else:
                    print('\nPLAYER ONE PUT ' + str(BET) + ' CHIPS IN THE POT')
                PLAYER_ONE_BAL = PLAYER_ONE_BAL - BET
            else:
                if BET == 1:
                    print('\nPLAYER TWO PUT 1 CHIP IN THE POT')
                else:
                    print('\nPLAYER TWO PUT ' + str(BET) + ' CHIPS IN THE POT')
                PLAYER_TWO_BAL = PLAYER_TWO_BAL - BET
            POT = POT + BET
    return POT, PLAYER_ONE_BAL, PLAYER_TWO_BAL

def GAME():
    #Receives nothing
    #is essentially the main function
    #continues to run until one player loses or quits
    CARD_DECK = INIT_DECK()
    PLAYER_ONE_BAL = 10
    PLAYER_TWO_BAL = 10
    BET = 0
    POT = 0
    CARDS_DRAWN = 0
    GAME_RUNNING = True
    TURN = True
    while GAME_RUNNING:
        PLAYER_ONE_BAL, PLAYER_TWO_BAL, POT = COLLECT_ANTE(PLAYER_ONE_BAL, PLAYER_TWO_BAL, POT)
        if PLAYER_ONE_BAL <= 0 or PLAYER_TWO_BAL <= 0:
            QUIT(PLAYER_ONE_BAL, PLAYER_TWO_BAL)
            return

        time.sleep(1)

        print('\nTHE POT HAS ' + str(POT) + ' CHIPS')

        time.sleep(1)

        CARDS_DRAWN, CARD_DECK, CARD_ONE, CARD_TWO = DEAL_CARD(PLAYER_ONE_BAL, PLAYER_TWO_BAL,TURN, CARDS_DRAWN, CARD_DECK)
        if CARDS_DRAWN == -1:
            time.sleep(1)
            return
        BET, PLAYER_ONE_BAL, PLAYER_TWO_BAL, POT = CHECK_CASE(CARD_ONE, CARD_TWO, POT, TURN, PLAYER_ONE_BAL, PLAYER_TWO_BAL)



        CARDS_DRAWN, CARDS_RECEIVED, CARD_DECK = GET_CARD(1, CARDS_DRAWN, CARD_DECK)
        CARD_THREE = CARDS_RECEIVED[0].split()
        time.sleep(1)
        POT, PLAYER_ONE_BAL, PLAYER_TWO_BAL = IN_BETWEEN(BET, POT, TURN, CARD_ONE, CARD_TWO, CARD_THREE, PLAYER_ONE_BAL, PLAYER_TWO_BAL)

        TURN = not TURN
GAME()