from collections import deque
import pygame
from time import sleep
from config import *

def getPath(draw, board, parent, start, end):
    temp = end.row, end.col
    while temp != None:
        i, j = temp
        board[i][j].color = green
        draw()
        sleep(0.015)
        temp = parent[i][j]

    sleep(1)
    start.color = yellow
    end.color = orange
    draw()


def BFS(draw, board, start, end):
    Q = deque()
    parent = [[None for _ in range(rows)] for _ in range(rows)]
    Q.append((start.row, start.col))
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while Q:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        row, col = Q.popleft()
        curr = board[row][col]
        if curr == end:
            getPath(lambda: draw(), board, parent, start, end)
            return True
        
        if curr != start:
            curr.color = red

        for step_row, step_col in dirs:
            i, j = row + step_row, col + step_col
            node = board[i][j]
            if node.color != white and node != end:
                continue
            parent[i][j] = (row, col)
            if node != end:
                node.color = blue
                
            Q.append((i, j))
        draw()