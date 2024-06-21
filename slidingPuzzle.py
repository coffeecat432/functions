import random

class SlidingPuzzle:
    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        random.shuffle(self.board)
        self.empty_tile = self.board.index(0)

    def display(self):
        for i in range(3):
            print(self.board[i*3:(i+1)*3])

    def is_solved(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def move(self, direction):
        row, col = divmod(self.empty_tile, 3)
        if direction == 'up' and row > 0:
            self.swap(self.empty_tile, self.empty_tile - 3)
        elif direction == 'down' and row < 2:
            self.swap(self.empty_tile, self.empty_tile + 3)
        elif direction == 'left' and col > 0:
            self.swap(self.empty_tile, self.empty_tile - 1)
        elif direction == 'right' and col < 2:
            self.swap(self.empty_tile, self.empty_tile + 1)
        else:
            print("Invalid move!")

    def swap(self, i, j):
        self.board[i], self.board[j] = self.board[j], self.board[i]
        self.empty_tile = j

def main():
    puzzle = SlidingPuzzle()
    while not puzzle.is_solved():
        puzzle.display()
        move = input("Enter move (up, down, left, right): ").strip().lower()
        puzzle.move(move)
    print("Congratulations! You've solved the puzzle!")
    puzzle.display()

if __name__ == "__main__":
    main()