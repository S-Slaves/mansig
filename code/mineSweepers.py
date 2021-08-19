import random

englishNum = ['zero', 'one', 'two', 'three',
              'four', 'five', 'six', 'seven', 'eight']


class mineCell:
    def __init__(self):
        self.num = 0
        self.isBomb = False
        self.isRevealed = False

    def __str__(self):
        if self.isBomb == True:
            return '||:boom:||'
        else:
            if self.isRevealed:
                return f':{englishNum[self.num]}:'
            else:
                return f'||:{englishNum[self.num]}:||'

    def increment(self):
        self.num += 1


class mineField:
    def __init__(self, x, y, bombNum):
        self.field = [[mineCell()
                       for i in range(x)] for j in range(y)]
        self.x_size = x
        self.y_size = y
        self.bombNum = bombNum

    def fetchCell(self, x, y):
        return self.field[y][x]

    def fetchNeighboringCells(self, x, y):
        returnlist = []
        x_range = [k for k in range(x-1, x+2) if k >= 0 and k <= self.x_size-1]
        y_range = [k for k in range(y-1, y+2) if k >= 0 and k <= self.y_size-1]
        for i in x_range:
            for j in y_range:
                returnlist.append(self.fetchCell(i, j))
        return returnlist


def mineSweepers(x_size, y_size, bombNum):
    if bombNum >= x_size * y_size:
        return '아이구 지뢰 숫자가 너무 많아유!!'
    if x_size > 9 or y_size > 9:
        return '현재 !지뢰찾기는 디스코드의 문제와 2000자 자수 제한으로 9*9 판까지만 지원해유~'
    returnString = ''
    revealList = []
    field = mineField(x_size, y_size, bombNum)
    while bombNum > 0:
        cell = field.fetchCell(random.randrange(
            0, x_size), random.randrange(0, y_size))
        if not cell.isBomb:
            cell.isBomb = True
            bombNum -= 1

    for x in range(x_size):
        for y in range(y_size):
            if field.fetchCell(x, y).isBomb:
                for k in field.fetchNeighboringCells(x, y):
                    k.increment()

    for i in range(0, 9):
        for x in range(x_size):
            for y in range(y_size):
                if field.fetchCell(x, y).num == i and not field.fetchCell(x, y).isBomb:
                    revealList.append((x, y))
        if len(revealList) != 0:
            break

    revealItem = random.choice(revealList)
    field.fetchCell(revealItem[0], revealItem[1]).isRevealed = True

    for i in field.field:
        for j in i:
            returnString += str(j)
        returnString += '\n'

    return returnString
