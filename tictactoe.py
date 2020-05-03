class InvalidSign(Exception):
    """
    Raises an Exception when the sign is not a valid one.
    """


class InvalidName(Exception):
    """
    Raises an Exception when the name is less than 3 characters.
    """


class InvalidSignNumber(Exception):
    """
    Raises an Exception when the sign number to play is invalid.
    """


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


class TicTacToe:
    def __init__(self, arg):
        self.__board = initial_board()
        self.available_choices = list(range(1, 10))
        self.player = self.validate_name(arg[0])
        self.signs = self.validate_sign(arg[1])
        self.player_sign = self.signs[0]
        self.cpu_sign = self.signs[1]
        self.win_combo_var = win_combos()

    def validate_name(self, name):
        if len(name) <= 2:
            raise InvalidName('Please restart the program and provide a valid name.')

        return name

    def validate_sign(self, sign):
        if sign.upper() not in {'X', 'O'}:
            raise InvalidSign('Please restart the program and provide a valid sign.')

        if sign == 'X':
            return 'X', 'O'
        return 'O', 'X'

    def player_move(self):
        try:
            p_choice = int(input('Choose a number from 1 to 9 to place your sign: '))
            if p_choice <= 0 or p_choice > len(self.__board):
                raise InvalidSignNumber('Please restart the program and provide only a valid sign numbers.')
        except:
            raise InvalidSignNumber('Please restart the program and provide only a valid sign numbers.')

        if self.__board[p_choice - 1] == ' ':
            self.__board[p_choice - 1] = self.player_sign
            self.available_choices.remove(p_choice)
        else:
            print('The provided sign number is occupied.')
            print('')
            self.player_move()

    def cpu_move(self):
        random_num = choice(self.available_choices)
        self.available_choices.remove(random_num)

        print('')
        print('The cpu is thinking...')
        time.sleep(1)
        print('cpu move is done!')

        self.__board[random_num - 1] = self.cpu_sign

    def check_for_win(self):
        for i in self.win_combo_var:
            x = f'{self.__board[i[0]]} {self.__board[i[1]]} {self.__board[i[2]]}'

            if x in {'X X X', 'O O O'}:
                print(f'{"".join([self.player if self.player_sign == x[0] else "cpu"])} won the game.')
                return True

        if len(self.available_choices) == 0:
            print('draw!')
            return True

    def draw_board(self):
        print("""
    {} | {} | {}    
    ---------
    {} | {} | {}    
    ---------
    {} | {} | {}    
        """.format(*self.__board))


if __name__ == '__main__':
    from random import choice
    import time

    nickname = welcome_screen()
    game = TicTacToe(nickname)
    game.draw_board()

    while True:
        game.player_move()
        game.draw_board()

        if game.check_for_win():
            break

        if game.available_choices:
            game.cpu_move()
            game.draw_board()

        if game.check_for_win():
            break