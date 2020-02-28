import random, os, sys


def main():
    menu()


def menu():
    print("Do you want to play a new game? Type 1 for yes and type 2 for no")
    ask_player = int(input())
    if (ask_player == 1):
        print("You have chosen to start a new game")
        new_game_setup()
    elif (ask_player == 2):
        print("You have chosen to exit game")
        exit()
    else:
        print("Sorry did not understand input, try again")
        menu()


def new_game_setup():
    print("How many rounds do you want to play?")
    round_num = int(input())
    print(
        "Do you want to play against the computer or a real life opponent? \n To play against a real opponent, enter 1."
        " If you want to play against a computer, enter 2.")
    choice = int(input())
    if choice == 1:
        print("Ok now creating a new real-life game with", round_num, "rounds")
        game(round_num)
    elif choice == 2:
        print("Ok now creating a new AI game with", round_num, "rounds")
        game_AI(round_num)
    else:
        print("Sorry try again")
        new_game_setup()


def game(rounds):
    print("Ok, the rules are as they have always been in rock, paper, scissors. To play rock, enter 'r,' to play"
          "scissors, enter 's' and to play paper, enter 'p'")
    x = 1
    player1_wins = 0
    player2_wins = 0
    while x <= rounds:
        print("Round:", x)
        print("Player 1 turn:")
        player_1 = str(input())
        print("Player 2 turn:")
        player_2 = str(input())
        if ((player_1 == 'r' and player_2 == 's') or (player_1 == 's' and player_2 == 'p') or (
                player_1 == 'p' and player_2 == 'r')):
            player1_wins += 1
            print("Player 1 wins this round\n")
            print("Current score:", "Player 1:", player1_wins, "|", "Player 2:", player2_wins, "\n")
            x += 1
        elif ((player_2 == 'r' and player_1 == 's') or (player_2 == 's' and player_1 == 'p') or (
                player_2 == 'p' and player_1 == 'r')):
            player2_wins += 1
            print("Player 2 wins this round \n")
            print("Current score:", "Player 1:", player1_wins, "|", "Player 2:", player2_wins, "\n")
            x += 1
        elif (player_1 == player_2):
            print("Draw!")
            print("Current score:", "Player 1:", player1_wins, "|", "Player 2:", player2_wins, "\n")
            x += 1
        else:
            game(rounds)
    post_game(player2_wins, player1_wins)


def game_AI(rounds):
    print("Ok, the rules are as they have always been in rock, paper, scissors. To play rock, enter 'r,' to play"
          "scissors, enter 's' and to play paper, enter 'p'")
    x = 1
    player1_wins = 0
    player2_wins = 0
    player2_options = ['r', 's', 'p']
    while x <= rounds:
        print("Round:", x)
        print("Player 1 turn:")
        player_1 = str(input())
        print("Player 2 turn:")
        player_2 = str(random.choice(player2_options))
        print(player_2)
        if ((player_1 == 'r' and player_2 == 's') or (player_1 == 's' and player_2 == 'p') or (
                player_1 == 'p' and player_2 == 'r')):
            player1_wins += 1
            print("Player 1 wins this round\n")
            print("Current score:", "Player 1:", player1_wins, "|", "Player 2:", player2_wins, "\n")
            x += 1
        elif ((player_2 == 'r' and player_1 == 's') or (player_2 == 's' and player_1 == 'p') or (
                player_2 == 'p' and player_1 == 'r')):
            player2_wins += 1
            print("Player 2 wins this round \n")
            print("Current score:", "Player 1:", player1_wins, "|", "Player 2:", player2_wins, "\n")
            x += 1
        elif (player_1 == player_2):
            print("Draw!")
            print("Current score:", "Player 1:", player1_wins, "|", "Player 2:", player2_wins, "\n")
            x += 1
        else:
            game(rounds)
    post_game(player2_wins, player1_wins)


def post_game(two_win, one_win):
    if one_win > two_win:
        print("Player 1 wins the game!", one_win, ":", two_win)
        menu()
    elif one_win < two_win:
        print("Player 2 wins the game!", two_win, ":", one_win)
        menu()
    elif one_win == two_win:
        print("Draw game!", one_win, ":", two_win)
        menu()


main()


