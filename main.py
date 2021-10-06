import pygame
import bfs, dijkstra, a_star, bellman_ford

size = 900
window = pygame.display.set_mode((size, size))
pygame.display.set_caption("Shortest Path Finding Algorithms")


white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 255, 0
yellow = 255, 255, 0
purple = 128, 0, 128
orange = 255, 165, 0
grey = 128, 128, 128


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
    


def makeBoard(rows, size):
    board = [[Node(i, j, size // rows, rows) for j in range(rows)] for i in range(rows)]
    return board


def drawBoard(win, rows, size):
    spacing = size // rows
    for i in range(rows):
        pygame.draw.line(win, grey, (0, i * spacing), (size, i * spacing))
        pygame.draw.line(win, grey, (i * spacing, 0), (i * spacing, size))


def draw(win, board, rows, size):
    win.fill(white)
    for row in board:
        for node in row:
            node.display(win)
        
    drawBoard(win, rows, size)
    pygame.display.update()



def main(win, size):
    rows = 60
    board = makeBoard(rows, size)

    running = True
    while running:
        draw(win, board, rows, size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            

    pygame.quit()



if __name__ == "__main__":
    main(window, size)