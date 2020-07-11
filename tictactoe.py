class TicTacToe:
    def __init__(self, name, sign):
        self.__board = initial_board()
        self.available_choices = list(range(1, 10))
        self.player = self.validate_name(name)
        self.player_sign, self.cpu_sign = self.validate_sign(sign)
        self.win_combo_var = win_combos()

    @staticmethod
    def validate_name(name):
        if len(name) <= 2:
            raise InvalidName('Please restart the program and provide a valid name.')

        return name

    @staticmethod
    def validate_sign(sign):
        if sign.upper() not in {'X', 'O'}:
            raise InvalidSign('Please restart the program and provide a valid sign.')

        if sign.upper() == 'X':
            return 'X', 'O'
        return 'O', 'X'

    def player_move(self):
        try:
            p_choice = int(input('Choose a number from 1 to 9 to place your sign: '))
            if p_choice <= 0 or p_choice > len(self.__board):
                raise InvalidSignNumber('Please restart the program and provide only a valid sign numbers.')
        except ValueError:
            raise InvalidSignNumber('Please restart the program and provide only a valid sign numbers.')

        if self.__board[p_choice - 1] == ' ':
            self.__board[p_choice - 1] = self.player_sign
            self.available_choices.remove(p_choice)
        else:
            print('The provided sign number is occupied.\n')
            self.player_move()

    def cpu_move(self):
        random_num = choice(self.available_choices)
        self.available_choices.remove(random_num)

        print('The cpu is thinking...')
        time.sleep(1)
        print('cpu move is done!')

        self.__board[random_num - 1] = self.cpu_sign

    def check_for_win(self):
        for i in self.win_combo_var:
            x = f'{self.__board[i[0]]} {self.__board[i[1]]} {self.__board[i[2]]}'

            if x in {'X X X', 'O O O'}:
                print(f'{self.player if self.player_sign == x[0] else "cpu"} won the game.')
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
    from misc import welcome_screen, initial_board, win_combos
    from exceptions import InvalidSign, InvalidName, InvalidSignNumber
    from random import choice
    import time

    nickname, sign = welcome_screen()
    game = TicTacToe(nickname, sign)
    game.draw_board()

    while True:
        game.player_move()
        game.draw_board()

        if game.check_for_win():
            break

        game.cpu_move()
        game.draw_board()

        if game.check_for_win():
            break