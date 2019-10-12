# analyze valid moves according to which player
def valid_moves(matrix):
    valid_positions_int = []
    for row in range(1, 9):
        for column in range(1, 9):  # starting from each tile in the board
            if matrix[row][column] == '.':
                for x, y in directions:  # which direction it is
                    row1 = row + x  # go to the next tile
                    column1 = column + y  # go to the next tile
                    count_inbetween_tiles = 0
                    while 0 < row1 < 9 and 0 < column1 < 9:  # go that direction or not
                        if matrix[row1][column1] == the_other_player:  # yes
                            count_inbetween_tiles += 1  # count inbetween tiles
                            # continue to check the next tile
                            row1 += x  # go to the next tile
                            column1 += y  # go to the next tile
                            # go back to while loop
                        elif matrix[row1][column1] == '.':  # no
                            break  # exit the while loop, go back to for loop for another direction
                        elif matrix[row1][column1] == player and count_inbetween_tiles > 0:
                            valid_positions_int.append([column, row])  # that is the spot
                            break  # exit the while loop, go back to for loop for another direction
                        elif matrix[row1][column1] == player and count_inbetween_tiles == 0:
                            break  # exit the while loop, go back to for loop for another direction
    return(valid_positions_int)

# do the flipping, return new matrix, DONE HERE
def flip_tiles(xcoordinate, ycoordinate):  # starting from the player's input
    for x, y in directions:  # which direction it is
        row2 = xcoordinate + x  # go to the next tile
        column2 = ycoordinate + y  # go to the next tile
        positions2flip = []
        while 0 < row2 < 9 and 0 < column2 < 9:  # go that direction or not
            if matrix[row2][column2] == the_other_player:  # yes
                positions2flip.append([row2, column2])  # add inbetween tiles
                # continue to check the next tile
                row2 += x  # go to the next tile
                column2 += y  # go to the next tile
                # go back to while loop
            elif matrix[row2][column2] == '.':  # no
                break  # exit the while loop, go back to for loop for another direction
            elif matrix[row2][column2] == player and positions2flip != []:
                # this is the spot
                for x_flip, y_flip in positions2flip:
                    matrix[x_flip][y_flip] = player
                break  # exit the while loop, go back to for loop for another direction
            elif matrix[row2][column2] == player and positions2flip == []:
                break  # exit the while loop, go back to for loop for another direction

    return(matrix)

# scores
def scores(matrix):
    # count the scores
    B_points = 0
    W_points = 0
    empty_points = 0
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
        return('Draw')
    elif B_points > W_points:
        B_points += empty_points
        return('End of the game. W: ' + str(W_points) + ', B: ' + str(B_points)+ '\n' + 'B wins.')
    elif W_points > B_points:
        W_points += empty_points
        return('End of the game. W: ' + str(W_points) + ', B: ' + str(B_points) + '\n' + 'W wins.')

    return([B_points, W_points])

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
valid_positions_str = []
convert_char2num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
convert_num2char = {v: k for k, v in convert_char2num.items()}
players = ['B', 'W']
pass_times = ''
B_points = 0
W_points = 0
empty_points = 0
count_output_lines = 0
final_scores = []

while True:
# which player is it
    for player in players:
        if player == 'B':
            the_other_player = 'W'
        else:
            the_other_player = 'B'

        # analyze valid moves according to which player
        valid_positions_int = valid_moves(matrix)

        # if no valid moves:
        if valid_positions_int == []:
            count_empty_tiles = 0
            for row in matrix:  # count empty tiles
                for tile in row:
                    if tile == '.':
                        count_empty_tiles += 1

            if count_empty_tiles != 0:
                print('Player', player, 'cannot play.')
                pass_times += '1'
                if pass_times[-2:] == '11':  # if 2 invalid moves in a row:
                    print(scores(matrix))
                    final_scores = scores(matrix)
                    break

            elif count_empty_tiles == 0:  # if no tiles left to play
                print(scores(matrix))
                final_scores = scores(matrix)
                # STOP THE GAME
                break

        # if valid moves:
        else:  # if there's valid moves
            pass_times += '0'
            # display valid moves by string
            valid_positions_str = []
            for pair in valid_positions_int:  # convert from int to str
                position_str = convert_num2char[pair[0]] + str(pair[1])
                valid_positions_str.append(position_str)
            valid_positions_str = set(valid_positions_str)
            print('Valid choices:', ' '.join(sorted(valid_positions_str)))
            # player's input: chosen position
            position = input('Player ' + player + ': ')
            # invalid input positions
            while position not in valid_positions_str:
                print(position, ': Invalid choices')
                position = input('Player ' + player + ': ')
            # convert str input positions to integers
            input_column = convert_char2num[position[0]]
            input_row = int(position[1])
            matrix[input_row][input_column] = player

            # do the flipping, return new matrix, DONE HERE
            matrix = flip_tiles(input_row, input_column)
            for list in matrix:
                print(' '.join(list))

# condition to stop the while loop
    if final_scores != []:
        if final_scores[0] != 0 or final_scores[1] != 0:
            break
