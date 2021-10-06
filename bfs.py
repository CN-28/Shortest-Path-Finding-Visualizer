from collections import deque
import pygame
from time import sleep
from config import *

def BFS(draw, board, start, end):
    Q = deque()
    parent = [[None for _ in range(rows)] for _ in range(rows)]
    Q.append((start.row, start.col))
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    succes = False

    while Q:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        row, col = Q.popleft()
        if (row, col) == (end.row, end.col):
            succes = True
            break
        

        for step_row, step_col in dirs:
            i, j = row + step_row, col + step_col
            if 0 <= i < rows and 0 <= j < rows:
                node = board[i][j]
                if node.color != black and node.color != red and node.color != yellow:
                    parent[i][j] = (row, col)
                    if node != end:
                        node.color = red
                        for step_row, step_col in dirs:
                            k, l = i + step_row, j + step_col
                            if 0 <= k < rows and 0 <= l < rows:
                                node = board[k][l]
                                if node.color == white:
                                    node.color = blue
                    Q.append((i, j))
        draw()

    if not succes:
        return False
    
    temp = end.row, end.col
    while temp != None:
        i, j = temp
        board[i][j].color = green
        draw()
        temp = parent[i][j]

    sleep(1)
    start.color = yellow
    end.color = orange
    draw()
    return True