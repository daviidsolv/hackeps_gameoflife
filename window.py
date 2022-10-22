import tkinter as tk
from unittest import runner
from matrix import Matrix

class Window(tk.Tk):
    def __init__(self, matrix:Matrix, width=600, height=600):
        super().__init__()
        self.title("Game Of Life")
        self._width = width
        self._height = height
        self.canvas = tk.Canvas(self, width=self._width, height=self._height, bg="black")
        self.resizable(False, False)
        self.canvas.pack()    
        self.matrix = matrix
        self.runned = False

    def draw(self):
        #self.canvas.delete("all")
        matrixSize = self.matrix.getMatrixSize()
        if not self.runned:
            for row in range(matrixSize[0]):
                for col in range(matrixSize[1]):
                    x1 = col * self._width / matrixSize[0]
                    y1 = row * self._height / matrixSize[1]
                    x2 = x1 + self._width / matrixSize[0]
                    y2 = y1 + self._height / matrixSize[1]
                        
                    if self.matrix.getMatrix()[row][col] == 0:
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="white")
                    else:
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white")

            self.runned = True
        
        else:
            pass

    def run(self):
        while True:
            self.update()
            self.update_idletasks()
            self.draw()