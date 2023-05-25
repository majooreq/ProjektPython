# WAŻNE! Praca była wykonywana na: Programiz - Python Online Compiler /
# Autor: Dominik Majorek, 4IAP /

def Tablica(board):
    poleGry = """
_________________________
|       |       |       |
|   1   |   2   |   3   |
|_______|_______|_______|
|       |       |       |
|   4   |   5   |   6   |
|_______|_______|_______|
|       |       |       |
|   7   |   8   |   9   |
|_______|_______|_______|
"""

    for i in range(1,10):
        if (board[i] == 'O' or board[i] == 'X'):
            poleGry = poleGry.replace(str(i), board[i])
        else:
            poleGry = poleGry.replace(str(i), ' ')
    print(poleGry)

def player_input():
    gr1 = input("Wybierz 'X' lub 'O': ")
    while True:
        if gr1.upper() == 'X':
            gr2 = 'O'
            print("Wybrałeś/aś " + gr1 + "! Drugi gracz będzie " + gr2 + ".")
            print("")
            return gr1.upper(),gr2
        elif gr1.upper() == 'O':
            gr2 = 'X'
            print("Wybrałeś/aś " + gr1 + "! Drugi gracz będzie " + gr2 + ".")
            print("")
            return gr1.upper(),gr2
        else:
            gr1 = input("Masz jedynie do wyboru 'X' lub 'O'! Spróbujmy jeszcze raz: ")

def place_marker(board, marker, position):
    board[position] = marker
    return board

def space_check(board, position):
    return board[position] == '#'

def checkowanie(board):
    return len([x for x in board if x == '#']) == 1

def ktowygr(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    return False

def player_choice(board):
    choice = input("Wybierz pole od 1 do 9: ")
    while not space_check(board, int(choice)):
        choice = input("To pole jest zajęte! Spróbujmy jeszcze raz: ")
    return choice

def replay():
    gra_znowu = input("Chcesz zagrać jeszcze raz (t/n)? - ")
    if gra_znowu.lower() == 't':
        return True
    if gra_znowu.lower() == 'n':
        return False

if __name__ == "__main__":
    print("Witaj w grze 'Kółko i Krzyżyk (Tic-Tac-Toe)'!")
    print("")
    print("Kolejność pól jest następująca:")
    print("|1|2|3|")
    print("|4|5|6|")
    print("|7|8|9|")
    print("")
    i = 1
    # Wybór strony.
    players = player_input()
    # Pusta tablica, pole.
    board = ['#'] * 10
    while True:
        # Ustawienie gry.
        game_on = checkowanie(board)
        while not game_on:
            # Gracz wybiera, gdzie umieścić znak 'X' lub 'O' na polu.
            position = player_choice(board)
            # Wskazanie gracza.
            if i % 2 == 0:
                marker = players[1]
            else:
                marker = players[0]
            # Rozgrywka.
            place_marker(board, marker, int(position))
            # Sprawdzanie tablicy.
            Tablica(board)
            i += 1
            if ktowygr(board, marker):
                print("Wygrałeś/aś!")
                break
            game_on = checkowanie(board)
        if not replay():
            break
        else:
            i = 1
            # Wybór strony.
            players = player_input()
            # Pusta tablica, pole.
            board = ['#'] * 10
