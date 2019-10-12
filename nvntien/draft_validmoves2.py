def valid_moves(matrix):
    valid_positions_int = []
    player = 'B'
    the_other_player = 'W'
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
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
                            row1 += x
                            column1 += y
                            # go back to while loop
                        elif matrix[row1][column1] == '.':  # no
                            break  # exit the while loop, go back to for loop for another pair
                        elif matrix[row1][column1] == player and count_inbetween_tiles > 0:
                            valid_positions_int.append([column, row])  # that is the spot
                            break  # exit the while loop, go back to for loop for another pair
                        elif matrix[row1][column1] == player and count_inbetween_tiles == 0:
                            break
    #valid_positions_int = set(valid_positions_int)
    return(valid_positions_int)


matrix = [[' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
['1', '.', '.', '.', '.', '.', '.', '.', '.'],
['2', '.', '.', '.', '.', '.', '.', '.', '.'],
['3', '.', '.', '.', '.', '.', '.', '.', '.'],
['4', '.', '.', 'W', 'W', 'B', '.', '.', '.'],
['5', '.', '.', '.', 'B', 'W', 'W', '.', '.'],
['6', '.', '.', '.', '.', 'W', '.', '.', '.'],
['7', '.', '.', '.', '.', 'B', '.', '.', '.'],
['8', '.', '.', '.', '.', '.', '.', '.', '.']]
for list in m:
    print(' '.join(list))


print(valid_moves(m))  # temp

count = 0
while True:
    for i in range(2):
        print(i)
        count += 1
        if count == 10:
            break

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
        return('End of the game. W: ' + str(W_points) + ', B: ' + str(B_points))
        return('B wins.')
    elif W_points > B_points:
        W_points += empty_points
        return('End of the game. W: ' + str(W_points) + ', B: ' + str(B_points))
        return('W wins.')

print(scores(matrix))
