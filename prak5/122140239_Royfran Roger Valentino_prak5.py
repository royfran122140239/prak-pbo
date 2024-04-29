import pygame
import sys
from pygame.locals import *

class TicTacToeBoard:
    def __init__(self, screen):
        self.screen = screen
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.font = pygame.font.Font(None, 150)

    def draw(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.line(self.screen, (0, 0, 0), (100, 0), (100, 300), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (200, 0), (200, 300), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, 100), (300, 100), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, 200), (300, 200), 5)

        for i in range(3):
            for j in range(3):
                text = self.font.render(self.board[i][j], True, (0, 0, 0))
                self.screen.blit(text, (j * 100 + 30, i * 100 + 15))

        pygame.display.update()

    def make_move(self, row, col, player):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def reset(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

class TicTacToeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 300))
        pygame.display.set_caption('Tic Tac Toe')
        self.board = TicTacToeBoard(self.screen)
        self.current_player = 'X'

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row, col = y // 100, x // 100
                    if self.board.make_move(row, col, self.current_player):
                        if self.board.check_winner():
                            print(f'Player {self.current_player} wins!')
                            self.reset_game()
                        elif self.board.is_full():
                            print('It\'s a draw!')
                            self.reset_game()
                        else:
                            self.current_player = 'O' if self.current_player == 'X' else 'X'

            self.board.draw()

    def reset_game(self):
        self.board.reset()
        self.current_player = 'X'

if __name__ == '__main__':
    game = TicTacToeGame()
    game.run()
