def tic_tac_toe():

    import IPython.display

    import random

    def player_input():
        player1 = ''
        while player1 != 'X' and player1 != 'O':
            player1 = input('Please pick a marker X or O.').upper()
        if player1 == 'X':
            player2 = 'O'
        elif player1 == 'O':
            player2 = 'X'
        return player1,player2

    def choose_first():
        if random.randint(0,1) == 0:
            first_move = player[0]
        else:
            first_move = player[1]
        return first_move

    def full_board_check(board):
        return ' ' not in board

    def display_board(board):
        '''
        Prints out a Tic Tac Toe Board
        '''
        print(f' {board[0]}|{board[1]}|{board[2]} \n-------\n {board[3]}|{board[4]}|{board[5]} \n-------\n {board[6]}|{board[7]}|{board[8]} ') 

    def place_marker(new_board,marker,position):
        new_board
        new_board[position-1] = f'{marker}'
        return new_board

    def space_check(board,position):
        return board[position-1]==' '

    def player_choice(board):
        position = int(input('Choose your next position.'))
        while not space_check(board,position):
            position = int(input('Choose an empty position.'))
        return position

    def win_check(board,mark):
        return board[0]==board[1]==board[2]==mark or board[3]==board[4]==board[5]==mark or board[6]==board[7]==board[8]==mark or board[0]==board[3]==board[6]==mark or board[1]==board[4]==board[7]==mark or board[2]==board[5]==board[8]==mark or board[0]==board[4]==board[8]==mark or board[2]==board[4]==board[6]==mark

    def replay():
        reply = ''
        while reply != 'yes' and reply != 'no':
            reply = input('Do you want to play again? (Yes/No)').lower()
        if reply == 'yes':
            return True
        elif reply == 'no':
            return False 

    print('Welcome to Tic Tac Toe!')

    while True:
        
        board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

        player = player_input()

        move = choose_first()

        print(f'{move} goes first.')
        
        while not full_board_check(board):

            print(f"{move}'s move.")

            display_board(board)

            board = place_marker(board,move,player_choice(board))

            if win_check(board, move):
                print(f'Congratulatons! {move} won!')
                break
            else:
                if move == 'X':
                    move = 'O'
                else:
                    move = 'X'

            IPython.display.clear_output()
            
        print('Game Over')
        if not replay():
            break

if __name__ == "__main__":
    tic_tac_toe()