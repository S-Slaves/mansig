import random

class mineCell:
    def _init_(self, x_index, y_index):
        self.x_index = x_index
        self.y_index = y_index
        self.number = 0
        self.isBomb = False
        self.isRevealed = False
    def increment(self):
        self.number += 1
    def reveal(self):
        self.isRevealed = True

def neighboring(cell):
    if cell.isBomb == True:
        pass

    
def mineSweepers(x_size, y_size, bombnum):
    pass