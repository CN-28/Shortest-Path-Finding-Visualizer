import pygame
import bfs, dijkstra, a_star, bellman_ford
from config import *

class Node:
    def __init__(self, row, col, size, numberOfRows):
        self.row = row
        self.col = col
        self.y = row * size
        self.x = col * size
        self.color = white
        self.size = size
        self.numberOfRows = numberOfRows
    

    def display(self, win):
        pygame.draw.rect(win, self.color, (self.y, self.x, self.size, self.size))
    


def makeBoard():
    board = [[Node(i, j, size // rows, rows) for j in range(rows)] for i in range(rows)]
    return board


def drawBoard(win, board):
    win.fill(white)
    for row in board:
        for node in row:
            node.display(win)

    spacing = size // rows
    for i in range(rows):
        pygame.draw.line(win, grey, (0, i * spacing), (size, i * spacing))
        pygame.draw.line(win, grey, (i * spacing, 0), (i * spacing, size))

    pygame.display.update()

    

def main():
    win = pygame.display.set_mode((size, size))
    pygame.display.set_caption("Shortest Path Finding Algorithms")
    board = makeBoard()
  
    running = True
    while running:
        drawBoard(win, board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            

    pygame.quit()



if __name__ == "__main__":
    main()