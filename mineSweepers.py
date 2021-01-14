import random


numlist = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight"]
minefield = []


async def mine_sweepers(x_size, y_size, bombnum):
    global minefield
    minefield = []
    output_minefield = ''

    def neighboring(x, y):
        global minefield
        if minefield[y][x] == 'X':
            if x == 0:
                x_scope = (0, 1)
            elif x == x_size - 1:
                x_scope = (x - 1, x)
            else:
                x_scope = (x - 1, x, x + 1)
            if y == 0:
                y_scope = (0, 1)
            elif y == y_size - 1:
                y_scope = (y - 1, y)
            else:
                y_scope = (y - 1, y, y + 1)
            for x_range in x_scope:
                for y_range in y_scope:
                    if minefield[y_range][x_range] != 'X':
                        minefield[y_range][x_range] += 1
        else:
            pass
    for i in range(y_size):
        minefield.append([0 for x in range(x_size)])

    for i in range(bombnum):
        random_x = random.randint(0, x_size - 1)
        random_y = random.randint(0, y_size - 1)
        minefield[random_y][random_x] = 'X'

    for x_ in range(x_size):
        for y_ in range(y_size):
            neighboring(y_, x_)

    zero_revealed = False
    for i in minefield:
        for j in i:
            if j == 'X':
                output_minefield += '||:boom:||'
            elif j == 0 and not zero_revealed:
                output_minefield += ':zero:'
                zero_revealed = True
            else:
                output_minefield += f'||:{numlist[j]}:||'
        output_minefield += '\n'

    if x_size >= 13 or y_size >= 13:
        output_minefield = ''
        for i in minefield:
            for j in i:
                if j == 'X':
                    output_minefield += 'X'
                else:
                    output_minefield += str(j)
            output_minefield += '\n'
        output_minefield = f'```{output_minefield}```'
    return output_minefield
