# board:
for i in range(1, 9):
    sublist = [str(i)]
    for j in range(8):
        sublist.append('.')
    matrix.append(sublist)

# analyze valid moves:
  # up
    if matrix[row - 1][column] == the_other_player:
        for r_up in range(row - 2, 0, -1):
            if matrix[r_up][column] == player:
                pass
            else:
                if matrix[r_up][column] == '.':
                    valid[column] = {r_up} #temporary
    # down
    if matrix[row + 1][column] == the_other_player:
        for r_down in range(row + 2, 9):
            if matrix[r_down][column] == player:
                pass
            else:
                if matrix[r_down][column] == '.':
                    valid[column] = {r_down} #temporary
    # left
    if matrix[row][column - 1] == the_other_player:
        for c_left in range(column - 2, 0, -1):
            if matrix[row][c_left] == player:
                pass
            else:
                if matrix[row][c_left] == '.':
                    valid[c_left] = {row} #temporary
    # right
    if matrix[row][column + 1] == the_other_player:
        for c_right in range(column + 2, 9):
            if matrix[row][c_right] == player:
                pass
            else:
                if matrix[row][c_right] == '.':
                    valid[c_right] = {row} #temporary
    # top left diagonal
    if matrix[row - 1][column - 1] == the_other_player:
        for r_tlif matrix[row - 1][column] == the_other_player:
        for r_up in range(row - 2, 0, -1):
            if matrix[r_up][column] == player:
                pass
            else:
                if matrix[r_up][column] == '.':
                    valid[column] = {r_up} #temporary
    # down
    if matrix[row + 1][column] == the_other_player:
        for r_down in range(row + 2, 9):
            if matrix[r_down][column] == player:
                pass
            else:
                if matrix[r_down][column] == '.':
                    valid[column] = {r_down} #temporary
    # left
    if matrix[row][column - 1] == the_other_player:
        for c_left in range(column - 2, 0, -1):
            if matrix[row][c_left] == player:
                pass
            else:
                if matrix[row][c_left] == '.':
                    valid[c_left] = {row} #temporary
    # right
    if matrix[row][column + 1] == the_other_player:
        for c_right in range(column + 2, 9):
            if matrix[row][c_right] == player:
                pass
            else:
                if matrix[row][c_right] == '.':
                    valid[c_right] = {row} #temporary
    # top left diagonal
    if matrix[row - 1][column - 1] == the_other_player:
        for r_tl, c_tl in zip(range(row - 2, 0, -1), range(column - 2, 0, -1)):
            if matrix[r_tl][c_tl] == player:
                pass
            else:
                if matrix[r_tl][c_tl] == '.':
                    valid[c_tl] = {r_tl} # temporary
    # bottom right diagonal
    if matrix[row + 1][column + 1] == the_other_player:
        for r_br, c_br in zip(range(row + 2, 9), range(column + 2, 9)):
            if matrix[r_br][c_br] == player:
                pass
            else:, c_tl in zip(range(row - 2, 0, -1), range(column - 2, 0, -1)):
            if matrix[r_tl][c_tl] == player:
                pass
            else:
                if matrix[r_tl][c_tl] == '.':
                    valid[c_tl] = {r_tl} # temporary
    # bottom right diagonal
    if matrix[row + 1][column + 1] == the_other_player:
        for r_br, c_br in zip(range(row + 2, 9), range(column + 2, 9)):
            if matrix[r_br][c_br] == player:
                pass
            else:
                if matrix[r_br][c_br] == '.':
                    valid[c_br] = {r_br} # temporary
    # top right diagonal
    if matrix[row - 1][column + 1] == the_other_player:
        for r_tr, c_tr in zip(range(row - 2, 0, -1), range(column + 2, 9)):
            if matrix[r_tr][c_tr] == player:
                pass
            else:
                if matrix[r_tr][c_tr] == '.':
                    valid[c_tr] = {r_tr} # temporary
    # bottom left diagonal
    if matrix[row + 1][column - 1] == the_other_player:
        for r_bl, c_bl in zip(range(row + 2, 9), range(column - 2, 0, -1)):
            if matrix[r_bl][c_bl] == player:
                pass
            else:
                if matrix[r_bl][c_bl] == '.':
                    valid[c_bl] = {r_bl} # temporary


for r in range(1, 9):
    for c in range(1, 9):
        if matrix[r][c] == 'B':
            B_points += 1
        elif matrix[r][c] == 'W':
            W_points += 1
        elif matrix[r][c] == '.':
            empty_points += 1

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
