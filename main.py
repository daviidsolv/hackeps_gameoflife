from random import seed
from window import Window
from matrix import Matrix

class GameOfLife:
    def __init__(self):
        self.matrix = Matrix(50, 50)
        self.seed = self.matrix.generateLife()
        self.window = Window(self.matrix)

    def run(self):
        self.window.run()


if __name__ == "__main__":
    game = GameOfLife()
    print("Starting game with seed: " + str(game.seed))
    game.run()