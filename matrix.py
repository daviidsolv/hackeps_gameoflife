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

    def countNeighbours(self, row, col):
        neighbours = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                elif row + i < 0 or row + i >= self.rows or col + j < 0 or col + j >= self.cols:
                    continue
                elif self.matrix[row + i][col + j] == 1:
                    neighbours += 1
        return neighbours

    def generateLife(self, specificSeed=None):
        if specificSeed is None:
            seed = random.randrange(sys.maxsize)
        else:
            seed = specificSeed

        rand = random.Random(seed)
        
        for row in range(self.rows):
            for col in range(self.cols):
                self.matrix[row][col] = rand.randint(0, 1)
                
        return seed

    def checkCell(self, row, col):
        neighbours = self.countNeighbours(row, col)
        if self.matrix[row][col] == 1:
            if neighbours < 2:
                return 0
            elif neighbours > 3:
                return 0
            else:
                return 1
        else:
            if neighbours == 3:
                return 1
            else:
                return 0

    def updateMatrix(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.matrix[row][col] = self.checkCell(row, col)