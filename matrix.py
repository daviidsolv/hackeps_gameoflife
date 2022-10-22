import random
import sys


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for x in range(cols)] for y in range(rows)]

    def getMatrixSize(self):
        return self.rows, self.cols

    def getMatrix(self):
        return self.matrix

    def generateLife(self, specificSeed=None):
        if specificSeed is None:
            seed = random.randrange(sys.maxsize)
        else:
            seed = specificSeed

        rand = random.Random(seed)
        x = rand.randint(0, self.rows - 1)
        y = rand.randint(0, self.cols - 1)
        self.matrix[x][y] = 1
        return seed

    def updateMatrix(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.matrix[row][col] = self.checkCell(row, col)