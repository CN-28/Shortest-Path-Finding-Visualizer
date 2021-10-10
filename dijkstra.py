from queue import PriorityQueue
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


def dijkstra(draw, board, start, end):
    Q = PriorityQueue()
    parent = [[None for _ in range(rows)] for _ in range(rows)]
    dist = [[float("inf") for _ in range(rows)] for _ in range(rows)]
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    count = 0

    dist[start.row][start.col] = 0
    Q.put((0, count, start))
    while not Q.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        curr = Q.get()[2]
        row, col = curr.row, curr.col
        if curr == end:
            getPath(lambda: draw(), board, parent, start, end)
            return True
        
        if curr != start:
            curr.color = red
            
        for step_row, step_col in dirs:
            i, j = row + step_row, col + step_col
            next = board[i][j]
            if next.color == black:
                continue

            if dist[row][col] + next.cost < dist[i][j]:
                dist[i][j] = dist[row][col] + next.cost
                parent[i][j] = row, col
                count += 1
                Q.put((dist[i][j], count, next))

                if next != end:
                    next.color = blue
        draw()