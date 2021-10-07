from queue import PriorityQueue
import pygame
from time import sleep
from config import *

def dijkstra(draw, board, start, end):
    Q = PriorityQueue()
    parent = [[None for _ in range(rows)] for _ in range(rows)]
    dist = [[float("inf") for _ in range(rows)] for _ in range(rows)]
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    success = False

    dist[start.row][start.col] = 0
    Q.put((0, (start.row, start.col)))
    while not Q.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        c, (row, col) = Q.get()
        if (row, col) == (end.row, end.col):
            success = True
            break
            
        for step_row, step_col in dirs:
            i, j = row + step_row, col + step_col
            if 0 <= i < rows and 0 <= j < rows:
                node = board[i][j]
                if node.color != black and dist[row][col] + node.cost < dist[i][j]:
                    dist[i][j] = dist[row][col] + node.cost
                    parent[i][j] = row, col
                    Q.put((dist[i][j], (i, j)))

                    if node != end:
                        node.color = red

                    for step_row, step_col in dirs:
                        k, l = i + step_row, j + step_col
                        if 0 <= k < rows and 0 <= l < rows:
                            node = board[k][l]
                            if node.color == white:
                                node.color = blue
        
        draw()
    
    if not success:
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