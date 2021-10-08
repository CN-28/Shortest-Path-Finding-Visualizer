import pygame
from time import sleep
from main import drawSquare
from config import *

def BellmanFord(draw, win, board, start, end, cntBlacks):
    dist = [[float("inf") for _ in range(rows)] for _ in range(rows)]
    parent = [[None for _ in range(rows)] for _ in range(rows)]
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    dist[start.row][start.col] = 0
    cnt = 0
    for _ in range(rows * rows - 1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for row in range(1, rows - 1):
            for col in range(1, rows - 1):
                isChanged = False
                for step_row, step_col in dirs:
                    i, j = row + step_row, col + step_col
                    if 0 < i < rows - 1 and 0 < j < rows - 1:
                        node = board[i][j]
                        if node.color != black and dist[row][col] + node.cost < dist[i][j]:
                            dist[i][j] = dist[row][col] + node.cost
                            parent[i][j] = row, col

                            if node != end and node != start and node.color != red:
                                isChanged = True
                                node.color = red
                                cnt += 1
                                drawSquare(win, node)
                            
                                for step_row, step_col in dirs:
                                    k, l = i + step_row, j + step_col
                                    if 0 < k < rows - 1 and 0 < l < rows - 1:
                                        node = board[k][l]
                                        if node.color == white:
                                            node.color = blue
                                            drawSquare(win, node)

                if cnt + cntBlacks < (rows - 1) * (rows - 1) - 2 and isChanged:
                    pygame.display.update()
                    sleep(0.015)       
        pygame.display.update()
            
    
    for row in range(1, rows - 1):
        for col in range(1, rows - 1):
            for step_row, step_col in dirs:
                i, j = row + step_row, col + step_col
                if 0 < i < rows - 1 and 0 < j < rows - 1:
                    node = board[i][j]
                    if node.color != black and dist[row][col] + node.cost < dist[i][j]:
                        return False
    
    if dist[end.row][end.col] != float("inf"):
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
        return True