def current_field(cells):
    print('---------')
    print('|', cells[0], cells[1], cells[2], '|')
    print('|', cells[3], cells[4], cells[5], '|')
    print('|', cells[6], cells[7], cells[8], '|')
    print('---------')


def check_win_state(cells, current_round):
    x_counter = 0
    o_counter = 0
    if cells[0] == cells[1] == cells[2]:
        if 'X' in cells[0]:
            x_counter += 1
        elif 'O' in cells[0]:
            o_counter += 1
    if cells[3] == cells[4] == cells[5]:
        if 'X' in cells[3]:
            x_counter += 1
        elif 'O' in cells[3]:
            o_counter += 1
    if cells[6] == cells[7] == cells[8]:
        if 'X' in cells[6]:
            x_counter += 1
        elif 'O' in cells[6]:
            o_counter += 1
    if cells[0] == cells[3] == cells[6]:
        if 'X' in cells[0]:
            x_counter += 1
        elif 'O' in cells[0]:
            o_counter += 1
    if cells[1] == cells[4] == cells[7]:
        if 'X' in cells[1]:
            x_counter += 1
        elif 'O' in cells[1]:
            o_counter += 1
    if cells[2] == cells[5] == cells[8]:
        if 'X' in cells[2]:
            x_counter += 1
        elif 'O' in cells[2]:
            o_counter += 1
    if cells[0] == cells[4] == cells[8]:
        if 'X' in cells[0]:
            x_counter += 1
        elif 'O' in cells[0]:
            o_counter += 1
    if cells[2] == cells[4] == cells[6]:
        if 'X' in cells[2]:
            x_counter += 1
        elif 'O' in cells[2]:
            o_counter += 1
    if o_counter > 0:
        print('O wins')
        quit()
    elif x_counter > 0:
        print('X wins')
        quit()
    elif current_round == 9 and x_counter == 0 and o_counter == 0:
        print('Draw')
        quit()


def next_move(lattice, current_round):
    move = input('Enter the coordinates: ')
    move = move.replace(' ', '')
    move_lst = list(move)
    if move.isnumeric():
        if 0 < int(move_lst[0]) < 4 and 0 < int(move_lst[1]) < 4:
            if move_lst[0] == '1':
                index = int(move_lst[0]) + int(move_lst[1]) - 2

            elif move_lst[0] == '2':
                index = int(move_lst[0]) + int(move_lst[1])

            elif move_lst[0] == '3':
                index = int(move_lst[0]) + int(move_lst[1]) + 2
            if lattice[index] != ' ':
                print('This cell is occupied! Choose another one!')
                next_move(lattice, current_round)
            else:
                grid_lst = list(lattice)
                if current_round % 2 == 1:
                    grid_lst[index] = 'X'
                else:
                    grid_lst[index] = 'O'
                global grid
                grid = ''.join(grid_lst)
                current_field(grid)
        else:
            print('Coordinates should be from 1 to 3!')
            next_move(lattice, current_round)
    else:
        print('You should enter numbers!')
        next_move(lattice, current_round)


rounds = 0
grid = '         '
current_field(grid)
while rounds < 10:
    rounds += 1
    next_move(grid, rounds)
    check_win_state(grid, rounds)
