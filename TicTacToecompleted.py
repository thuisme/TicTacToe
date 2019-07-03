#Place the marker for each player
def playermarker():
    marker = ""
    marker = input("\nPlayer 1, please choose X or O as your marker: ").upper()
    while marker != "X" and marker != "O":
        marker = input("\nOops! Just X or O, buddy!\nPlease choose again: ").upper()
    if marker == "X":
        return ("X", "O")
        print("Player 1's marker is X and Player 2's is O.")
    else:
        return ("O", "X")
        print("Player 1's marker is O and Player 2's is X.")


#Display the 5x5 board
def displayboard(board):
    print("|" + board[1] + "|" + board[2] + "|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|" + board[9] + "|" + board[10] + "|")
    print("|" + board[11] + "|" + board[12] + "|" + board[13] + "|" + board[14] + "|" + board[15] + "|")
    print("|" + board[16] + "|" + board[17] + "|" + board[18] + "|" + board[19] + "|" + board[20] + "|")
    print("|" + board[21] + "|" + board[22] + "|" + board[23] + "|" + board[24] + "|" + board[25] + "|")


#Choose randomly which player will go first
import random
def goesfirst():
    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"


#How to place the marker on the board
def placemarker(board, marker, position):
    board[position] = marker


#Creating the combination for winning the game
winningcom = ((1,2,3),(2,3,4),(3,4,5),(6,7,8),(7,8,9),(8,9,10),(11,12,13),(12,13,14),(13,14,15),(16,17,18),(17,18,19),(18,19,20),(21,22,23),(22,23,24),(23,24,25),
              (1,6,11),(6,11,16),(11,16,21),(2,7,12),(7,12,17),(12,17,22),(3,8,13),(8,13,18),(13,18,23),(4,9,14),(9,14,19),(14,19,24),(5,10,15),(10,15,20),(15,20,25),
              (1,7,13),(7,13,19),(13,19,25),(2,8,14),(8,14,20),(3,9,15),(6,12,18),(12,18,24),(11,17,23),
              (5,9,13),(9,13,17),(13,17,21),(4,8,12),(8,12,16),(3,7,11),(10,14,18),(14,18,22),(15,19,23))


#Check if the position is a free space
def freespace(board, position):
    return board[position] == " "


#Check if the board is full
def fullboard(board):
    for i in range(1, 26):
        return freespace(board, i)


#Asking to play a new game
def replay():
    replayans = input("\nDo you want to have another match? Type Y for 'Yes' and N for 'No': ").upper()
    while replayans != "Y" and replayans != "N":
        replayans = input("\nType Y for 'Yes' and N for 'No': ").upper()
    return replayans == "Y"



#Where the game starts
print("\nWelcome to 1v1 5x5 Tic Tac Toe!")

input("\nPress Enter to go to the instructions.")

print("\nThis Tic Tac Toe version is a little bit different than traditional one.\nThis is version for 2 players and the board is 5x5 instead of 3x3.")
print("But there is just one simple rule to win: the first one to make 3 markers consecutively in either horizontal or vertical or diagonal will be the winner! Good luck!")
print("\nThese are the moves available for the board. Don't worry! The board will be shown for every step you make.")

exampleboard = ["", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10", "11", "12", "13", "14", "15", "16",
                    "17", "18", "19", "20", "21", "22", "23", "24", "25"]
displayboard(exampleboard)

while True:
    player1marker, player2marker = playermarker()
    print("\nPlayer 1's marker is {} and Player 2's is {}.".format(player1marker,player2marker))

    emptyboard = [" "] * 26

    print("\nNow we will random to choose which Player will go first.")

    input("\nPress Enter to go to continue.")

    turn = goesfirst()
    print("\nYay! " + turn + " will have the privilege to take the first step.")

    input("\nPress Enter to go to continue.")

    playgame = input("\nAre you guys ready? Type Y for 'Yes' and N for 'No': ").upper()
    while playgame != "Y" and playgame != "N":
        playgame = input("\nJust Yes or No, buddy!\nPlease choose again: ").upper()
    if playgame == "Y":
        continuousgame = True
    else:
        continuousgame = False
        break

    while continuousgame == True:
        if turn == "Player 1":
            displayboard(exampleboard)
            print("")
            displayboard(emptyboard)
            position = int(input("\n" + turn + " with marker " + player1marker + ", please choose your position to place your marker: "))
            if position not in range(1, 26):
                position = int(input("\nPlease choose a valid number from 1-25: "))
            if freespace(emptyboard, position) == False:
                position = int(input("\nThat place is taken! Please choose another position: "))
                if position not in range(1, 26):
                    position = int(input("\nPlease choose a valid number from 1-25: "))
            placemarker(emptyboard, player1marker, position)
            for combo in winningcom:
                if emptyboard[combo[0]] == emptyboard[combo[1]] == emptyboard[combo[2]] == player1marker:
                    displayboard(emptyboard)
                    print("\nCongratulations! Player 1 has won the game!")
                    continuousgame = False
                else:
                    if fullboard(emptyboard) == True:
                        displayboard(emptyboard)
                        print("\nThis is a tie game.")
                        continuousgame = False
                    else:
                        turn = "Player 2"

        else:
            displayboard(exampleboard)
            print("")
            displayboard(emptyboard)
            position = int(input("\n" + turn + " with marker " + player2marker + ", please choose your position to place your marker: "))
            if position not in range(1, 26):
                position = int(input("\nPlease choose a valid number from 1-25: "))
            if freespace(emptyboard, position) == False:
                position = int(input("\nThat place is taken! Please choose another position: "))
                if position not in range(1, 26):
                    position = int(input("\nPlease choose a valid number from 1-25: "))
            placemarker(emptyboard, player2marker, position)
            for combo in winningcom:
                if emptyboard[combo[0]] == emptyboard[combo[1]] == emptyboard[combo[2]] == player2marker:
                    displayboard(emptyboard)
                    print("\nCongratulations! Player 2 has won the game!")
                    continuousgame = False
                else:
                    if fullboard(emptyboard) == True:
                        displayboard(emptyboard)
                        print("\nThis is a tie game.")
                        continuousgame = False
                    else:
                        turn = "Player 1"

    if not replay():
        print("\nThank you so much for playing my game!\nI'd love to hear your feedback so as to improve my game!")
        break