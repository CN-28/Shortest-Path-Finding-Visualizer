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


def h(node, end):
    return abs(node.row - end.row) + abs(node.col - end.col)


def a_star(draw, board, start, end):
    openSet = PriorityQueue()
    openSetHash = {start}
    parent = [[None for _ in range(rows)] for _ in range(rows)]
    gScore = [[float("inf") for _ in range(rows)] for _ in range(rows)]
    fScore = [[float("inf") for _ in range(rows)] for _ in range(rows)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    helperVar = 0

    openSet.put((0, helperVar, (start.row, start.col)))
    gScore[start.row][start.col] = 0
    fScore[start.row][start.col] = h(start, end)
    while not openSet.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        (row, col) = openSet.get()[2]
        curr = board[row][col]
        openSetHash.remove(curr)
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
            if gScore[row][col] + next.cost < gScore[i][j]:
                parent[i][j] = row, col
                gScore[i][j] = gScore[row][col] + next.cost
                fScore[i][j] = gScore[i][j] + h(next, end)
                if next not in openSetHash:
                    helperVar += 1
                    openSet.put((fScore[i][j], helperVar, (i, j)))
                    openSetHash.add(next)
                    next.color = blue
        draw()