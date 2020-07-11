def welcome_screen():
    print('Hello and Welcome to my workshop project.')
    nickname = input('Enter your nickname: ')
    sign = input('Enter your desired sign to play the game: ')

    return nickname, sign


def initial_board():
    return [' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' ']


def win_combos():
    return ((0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6))