# board
matrix = [[' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
['1', '.', '.', '.', '.', '.', '.', '.', '.'],
['2', '.', '.', '.', '.', '.', '.', '.', '.'],
['3', '.', '.', '.', '.', '.', '.', '.', '.'],
['4', '.', '.', '.', 'W', 'B', '.', '.', '.'],
['5', '.', '.', '.', 'B', 'W', '.', '.', '.'],
['6', '.', '.', '.', '.', '.', '.', '.', '.'],
['7', '.', '.', '.', '.', '.', '.', '.', '.'],
['8', '.', '.', '.', '.', '.', '.', '.', '.']]
for list in matrix:
    print(' '.join(list))

# arguments used in this program
directions = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
valid_positions_int = []
valid_positions_str = []
positions2flip = []
convert_char2num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
convert_num2char = {v: k for k, v in convert_char2num.items()}
players = ['B', 'W']
pass_times = ''
B_points = 0
W_points = 0
empty_points = 0

# which player is it
for player in players:
    if player == 'B':
        the_other_player = 'W'
    else:
        the_other_player = 'B'

    # analyze valid moves according to which player
    for row in range(1, 9):
        for column in range(1, 9):
            for x, y in directions:
                row1 = row
                column1 = column
                while 1 < row1 < 8 and 1 < column1 < 8:
                    row1 += x
                    column1 += y
                    if matrix[row1][column1] == the_other_player:
                        while 1 < row1 < 8 and 1 < column1 < 8:
                            row1 += x
                            column1 += y
                            if matrix[row1][column1] == player:
                                break
                            elif matrix[row1][column1] == the_other_player:
                                continue
                            elif matrix[row1][column1] == '.':
                                valid_positions_int.append([column1, row1])
                                break
    print(valid_positions_int)

    # if no valid moves:
    if valid_positions_int == []:
        print('Player', player, 'cannot play.')
        pass_times += '1'
        # if 2 invalid moves in a row:
        if pass_times[-2:] == '11':
            # STOP THE GAME
            break
            # count the scores
            for r in range(1, 9):
                for c in range(1, 9):
                    if matrix[r][c] == 'B':
                        B_points += 1
                    elif matrix[r][c] == 'W':
                        W_points += 1
                    elif matrix[r][c] == '.':
                        empty_points += 1
            # print the scores
            if B_points == W_points:
                print('Draw')
            elif B_points > W_points:
                B_points += empty_points
                print('End of the game.W: ' + W_points + ', B: ' + B_points)
                print('B wins.')
            elif W_points > B_points:
                W_points += empty_points
                print('End of the game.W: ' + W_points + ', B: ' + B_points)
                print('W wins.')

    # if valid moves:
    else:  # there's valid moves
        pass_times += '0'
        # display valid moves by string
        for pair in valid_positions_int:  # convert into str
            position_str = convert_num2char[pair[0]] + str(pair[1])
            valid_positions_str.append(position_str)
        print('Valid choices:', ' '.join(valid_positions_str))
        # player's input: chosen position
        position = input('Player ' + player + ': ')
        # invalid inpit positions
        while position not in valid_positions_str:
            print(position, ': Invalid choices')
            position = input('Player ' + player + ': ')
        # convert str input positions to integers
        input_column = convert_char2num[position[0]]
        input_row = int(position[1])

        # do the flipping, return new matrix, DONE HERE

        for x, y in directions:
            row2 = input_row + x
            column2 = input_column + y
            while 0 < row2 < 9 and 0 < column2 < 9:
                row2 += x
                column2 += y
                if matrix[row2][column2] == the_other_player:
                    positions2flip.append([row2, column2])
                elif matrix[row2][column2] == '.':
                    break
                elif matrix[row2][column2] == player:
                    for x_flip, y_flip in positions2flip:
                        matrix[x_flip][y_flip] = player
        for list in matrix:
            print(' '.join(list))
