from random import randint
import random
import os
import sys
import copy

os.system('clear')
ship_board = []
board = []
row = []

def board_appending():
    for j in range(10):
        row.append(" \033[1;35m 0  ")

    for i in range(10):
        board.append(copy.copy(row))
        ship_board.append(copy.copy(row))

def print_the_board():
    os.system('clear')
    print("\n")
    print ("  1     2     3     4     5     6     7     8     9    10  ")
    print("\033[1;30m┏━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━┓")
    for elem in board:
        print(*elem)
        print("\033[1;30m┣━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━┫ ")
    #print("┗━━━━")    
    #formats and prints board

def random_ship_coord2():
    ship_row = int(random.choice("012345678"))
    print(ship_row)
    ship_col = int(random.choice("012345678"))
    print(ship_col)
    ship_board[ship_row][ship_col] = '  1  '
    ship_board[ship_row][ship_col+1] = '  1  '

def random_ship_coord_second2():
    ship_row = int(random.choice("012345678"))
    print(ship_row)
    ship_col = int(random.choice("012345678"))
    print(ship_col)
    ship_board[ship_row][ship_col] = '  2  '
    ship_board[ship_row][ship_col+1] = '  2  '
    
def random_ship_coord3():
    ship_row = int(random.choice("012345678"))
    print(ship_row)
    ship_col = int(random.choice("0123456"))
    print(ship_col)
    ship_board[ship_row][ship_col] = '  3  '
    ship_board[ship_row][ship_col+1] = '  3  '
    ship_board[ship_row][ship_col+2] = '  3  '

def random_ship_coord_vertical3():
    ship_row = int(random.choice("0123456"))
    print(ship_row)
    ship_col = int(random.choice("012345678"))
    print(ship_col)
    ship_board[ship_row][ship_col] = '  4  '
    ship_board[ship_row+1][ship_col] = '  4  '
    ship_board[ship_row+2][ship_col] = '  4  '
#vertical ship
def random_ship_coord4():
    ship_row = int(random.choice("012356"))
    print(ship_row)
    ship_col = int(random.choice("0123456"))
    print(ship_col)
    ship_board[ship_row][ship_col] = '  5  '
    ship_board[ship_row][ship_col+1] = '  5  '
    ship_board[ship_row][ship_col+2] = '  5  '
    ship_board[ship_row][ship_col+3] = '  5  '

def shootingandmissing():    
    
    while int(max(max(ship_board)))>0:

        try:
            print("___________________________________________________________")
            guess_row = int(input("\n \033[1;36m Guess Row:"))-1
            print("___________________________________________________________")
            guess_col = int(input("\n \033[1;36mGuess Col:"))-1
        except (IndexError, TypeError, ValueError, NameError):
            print("Error try again")

        if ship_board[guess_row][guess_col]== '  1  ':
            board[guess_row][guess_col]='  \033[1;32mX  '
            ship_board[guess_row][guess_col]='  0  '
            print_the_board()
            print("\n \033[1;32mYou hit the Battelship!")
            destroy_ship2=+1
        elif ship_board[guess_row][guess_col]== '  2  ':
            board[guess_row][guess_col]='  \033[1;32mX  '
            ship_board[guess_row][guess_col]='  0  '
            print_the_board()
            print("\n \033[1;32mYou hit the Battelship!")
        elif ship_board[guess_row][guess_col]== '  3  ':
            board[guess_row][guess_col]='  \033[1;32mX  '
            ship_board[guess_row][guess_col]='  0  '
            print_the_board()
            print("\n \033[1;32mYou hit the Battelship!")
        elif ship_board[guess_row][guess_col]== '  4  ':
            board[guess_row][guess_col]='  \033[1;32mX  '
            ship_board[guess_row][guess_col]='  0  '
            print_the_board()
            print("\n \033[1;32mYou hit the Battelship!")
        elif ship_board[guess_row][guess_col]== '  5  ':
            board[guess_row][guess_col]=' \033[1;32m X  '
            ship_board[guess_row][guess_col]='  0  '
            print_the_board()
            print("\n \033[1;32mYou hit the Battelship!")
            #if hit correct
        else: 
            ship_board[guess_row][guess_col]== '  0  '
            board[guess_row][guess_col]=' \033[1;31m #  '
            print_the_board()
            print("\n \033[1;31mYou missed it! ")



def sinking_ship():
    while '  1  ' in ship_board:
        pass
    else:
        print("you sunk the two battleship")

def main_call_method():
    #place ships:
    sinking_ship()
    board_appending()
    random_ship_coord2()
    random_ship_coord_second2()
    random_ship_coord3()
    random_ship_coord_vertical3()
    random_ship_coord4()
    destroy_ship2=0 #bug
    #variable used for destroying ships
    #cheking ship board
    print("\n")
    print ("\033[1;36m  1     2     3     4     5     6     7     8     9    10  ")
    print ("\033[1;30m┏━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━┓")
    for elem in ship_board:  
        print(*elem)
        print("\033[1;30m┣━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━┫ ")
        #print("┗━━━━")
    shootingandmissing()
    print("you are the best!!!!!!!")
    print("\033[1;37m")
    '''if destroy_ship2==2:
                print("you destroyed the 2 length battleship") #bug
            else:
                pass
                '''

main_call_method()