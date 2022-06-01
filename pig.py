#!/usr/bin/env python3

import random
import time

players_list = [] # list of players
turn_order = [] # list of player names, player objects, and their respective turn orders in ascending turn order, from left to right, once sorted
goal_points = 100
delay = 4 # the time.sleep() functions used in the code are primarily based on 4 seconds

# dice object
class six_sided_game_die:
    def __init__(self):
        time.sleep(delay/4)
        print("\nDie initialized.\n")
        time.sleep(delay/4)
    def roll(self):
        return random.randint(1, 6)

die6 = six_sided_game_die()

# player object
class player:
    def __init__(self, name):
        self._name = name
        self._score = 0
        self._num = 0 # player-num. Acts as the unique "ID" of the player for when the same names are used. Obsolete but kept in for possible future iterations.
        self._roll_order = 0
        self._roll_count = 0 # holds the number of times a player has rolled
        self._is_comp = False # the computer will be based off of the player class. This determines if a player is a computer or not.
    def add_points(self, points):
        self._score = self._score + points
    def has_won(self):
        return self._score >= goal_points

# rules
def print_rules():
    print("\nRULES\n-----\n")
    time.sleep(delay/4)
    print("1. There is at least two players playing the game. A two player game may be against another player or against the computer. Three or more player games do not have a computer player to play against.\n")
    time.sleep(5)
    print("2. There is at most 4 players in a game.\n")
    time.sleep(delay/2)
    print("3. There is one six-sided die (simulated by the game using a psuedo-random number generator); the faces of the die are numbered 1, 2, 3, 4, 5, and 6. Opposing sides of the die sum to 7 (standard western casino dice).\n")
    time.sleep(5)
    print("4. The game is turn based. The player who goes first is selected by each player rolling the die once. The players are ordered from in ascending order. If there is a tie between two or more players, the computer can break the tie by arbitrarily assigning that player to a position not less than the position the player rolled.\n")
    time.sleep(delay*2)
    print("5. Once each player has had a turn in ascending order, the turn returns to the first player.\n")
    time.sleep(delay/2)
    print("6. Each turn, a player rolls the die.\n")
    time.sleep(delay/2)
    print("\tIf the player rolls a 1, the player scores nothing that turn and it becomes the next player's turn. The player's overall score does not change because the player has lost the points accrued during their turn.\n")
    time.sleep(5)
    print("\tIf the player rolls any other number, the value of the die is added to their turn's score as points and the player's turn may continue. The player's overall score does not change until their turn ends.\n")
    time.sleep(5)
    print("\tIf a player chooses to hold, their turn total is added to their score, and it becomes the next player's turn.\n")
    time.sleep(delay)
    print("\tThe play may not choose to hold until after the die has been rolled at least once.\n")
    time.sleep(delay/2)
    print("The game ends when a player ends their turn with a score of 100 points or greater.\n")
    time.sleep(delay/2)
    print("At the beginning of every die roll, the game displays the current player's total score, current turn score, and how many times the player has rolled. Once the die is rolled, the computer displays the value of the die. If it is a 1, the computer ends the current player's turn and moves on to the next player.\n")
    time.sleep(delay*2)
    print("----------------------------------\n")

# player_init determines how many players will be in the current session and returns whether a computer player will be present
def player_init(num):
    c = False 

    time.sleep(delay/4)
    if num is 2:
        print("Are you playing with another person? Type \'y\' for \"yes\" or \'n\' for \"no\". ")
        clarification2 = input().lower()
        if clarification2 == 'y':
            print("\nInsert Player 1's name: ")
            player1 = player(input())
            player1._num = 1
            players_list.append(player1)

            print("\nInsert Player 2's name: ")
            player2 = player(input())
            player2._num = 2
            players_list.append(player2)
        elif clarification2 == 'n':
            time.sleep(delay/2)
            print("\nSetting the computer as your opponent . . .\n")
            bot = player("CPU")
            bot._num = 2
            bot._is_comp = True
            c = True
            time.sleep(3)

            print("Insert your name: ")
            player1 = player(input())
            player1._num = 1
            players_list.append(player1)
            players_list.append(bot)
        else:
            exit("Inappropriate input.\n")
    elif num is 3 or 4:
        print("\nInsert Player 1's name: ")
        player1 = player(input())
        player1._num = 1
        players_list.append(player1)

        print("\nInsert Player 2's name: ")
        player2 = player(input())
        player2._num = 2
        players_list.append(player2)

        print("\nInsert Player 3's name: ")
        player3 = player(input())
        player3._num = 3
        players_list.append(player3)

        if num is 4:
            print("\nInsert Player 4's name: ")
            player4 = player(input())
            player4._num = 4
            players_list.append(player4)
    else:
        exit("\nInvalid number of players.\n")
    print("\n----------------------------------\n")
    return c # c = True if a computer player is present else False

# turn_resolution determines the turn order of all available players, based on ascending order
def turn_resolution(num):
    count = 0
    print("Initializing turn order, based on ascending order.\n")
    time.sleep(delay/2)
    for current_player in players_list:
        current_player._roll_order = die6.roll()
        print("{} rolled a {}.".format(current_player._name, current_player._roll_order))
        time.sleep(delay/2)
        turn_order.append([current_player._name, current_player, current_player._roll_order])
    turn_order.sort(key=lambda x: x[2])

    print("\nTurn order, from top to bottom: ")
    time.sleep(delay/2)
    for name, player, order in turn_order:
        print(name)
        time.sleep(delay/4)
        count += 1


def main():
    final_state = False # determines if game is in a final state (i.e. a player has won)
    comp_exist = False # status of whether or not a computer player is present
    count = 0

    time.sleep(delay/4)
    print("Welcome to the Pig game.\n")
    time.sleep(delay/2)
    print("Skip printing the rules? Type \'y\' for \"yes\" or \'n\' for \"no\".")
    choice = input().lower()
    if choice == "y":
        pass
    elif choice == "n":
        print_rules()
    else:
        exit("Inappropriate input.\n")
    time.sleep(delay/4)
    print("\nInput the number of players for this game session in integer format (i.e. 2, 3, or 4): ")
    players_num = int(input())
    comp_exist = player_init(players_num)
    time.sleep(delay/2)
    turn_resolution(players_num)

    while final_state is not True:
        for name, player, order in turn_order:
            if final_state == True:
                break
            time.sleep(3)
            print("\n----------------------------------")
            time.sleep(delay/2)
            print("\nIt is {}'s turn.\n".format(name))

            end_of_turn = False # once end_of_turn switches to True in the while-statement below, the next player takes their turn
            choice = "" # holds player input. Expects "roll" or "hold"
            total_current_roll = 0 # keeps track of the sum of cumulative rolls for a player's current turn.

            while end_of_turn is False:
                time.sleep(delay/4)
                print("{}'s total score: {}".format(name, player._score))
                time.sleep(delay/4)
                print("{}'s current turn score: {}".format(name, total_current_roll))
                time.sleep(delay/4)
                print("{} has rolled {} time(s).\n".format(name, player._roll_count))
                time.sleep(delay/4)

                current_roll = die6.roll()
                player._roll_count += 1
                total_current_roll += current_roll

                time.sleep(delay/4)
                print("{} rolled a {}.".format(name, current_roll))
                time.sleep(delay/4)

                if current_roll is 1: # the player ends their turn and scores nothing if a 1 was rolled
                    print("{} was rolled. {} scores nothing.".format(current_roll, name))
                    break
                else:
                    c_flag = False # implemented as a substituted for "choice != "roll" or "hold""
                    while c_flag == False:
                        print("Input \"roll\" or \"hold\", {}.\n".format(name))
                        if player._is_comp is False:
                            choice = input().lower()
                            print("\n")
                        elif player._is_comp is True: # comp AI
                            time.sleep(delay/2)
                            if player._score + total_current_roll >= goal_points: # if comp has rolled enough to win if it holds
                                print("hold\n")
                                choice = "hold"
                            elif player._roll_count % 4 is 0: # comp manually holds every 4 rolls
                                print("hold\n")
                                choice = "hold"
                            else: # greed
                                print("roll\n")
                                choice = "roll"
                        if choice == "roll":
                            c_flag = True
                        elif choice == "hold":
                            c_flag = True
                        elif c_flag == False:
                            print("Invalid input. Try again.\n")
                if choice == "hold":
                    player.add_points(total_current_roll)
                    time.sleep(delay/2)
                    print("{} holds and scores {} points.".format(name, total_current_roll))
                    end_of_turn = True
                if player.has_won():
                    time.sleep(delay/2)
                    print("Congratulations {}, you won with a score of {} points.".format(name, player._score))
                    final_state = True
                    break

    time.sleep(delay/4)
    print("\n----------------------------------")
    time.sleep(delay/4)
    print("\nFinal Scores:\n")
    for name, player, order in turn_order:
        time.sleep(delay/4)
        print("{}: {} points\n".format(name, player._score))
        time.sleep(delay/4)
        print("\tRolls taken: {} rolls\n".format(player._roll_count))
    time.sleep(delay/4)
    print("\n----------------------------------")
    time.sleep(delay/4)
    print("\nThanks for playing!\n")
    time.sleep(delay/4)
    print(":)\n")

main()