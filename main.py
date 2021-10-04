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