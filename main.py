import pygame
import bfs, dijkstra, a_star, bellman_ford
from config import *

class Node:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.y = row * size
        self.x = col * size
        self.color = white
        self.size = size
    

    def display(self, win):
        pygame.draw.rect(win, self.color, (self.y, self.x, self.size, self.size))
    


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


def clickedPos(pos):
    spacing = size // rows
    x, y = pos
    row, col = x // spacing, y // spacing
    return row, col
    


def main():
    win = pygame.display.set_mode((size, size))
    pygame.display.set_caption("Shortest Path Finding Algorithms")
    board = [[Node(i, j, size // rows) for j in range(rows)] for i in range(rows)]
  

    startNode = None
    endNode = None
    running = True
    while running:
        drawBoard(win, board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if pygame.mouse.get_pressed()[0]:
                row, col = clickedPos(pygame.mouse.get_pos())
                node = board[row][col]
                if not startNode:
                    startNode = node
                    startNode.color = yellow

                elif not endNode and node != startNode:
                    endNode = node
                    endNode.color = orange

                elif node != endNode and node != startNode:
                    node.color = black
            
            elif pygame.mouse.get_pressed()[2]:
                row, col = clickedPos(pygame.mouse.get_pos())
                node = board[row][col]
                node.color = white
                if node == startNode:
                    startNode = None
                elif node == endNode:
                    endNode = None


    pygame.quit()



if __name__ == "__main__":
    main()