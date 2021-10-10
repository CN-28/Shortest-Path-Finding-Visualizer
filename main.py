import pygame, pygame_gui
import bfs, dijkstra, bellman_ford, a_star
from random import randint
from time import sleep
from config import *

class Node:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.y = row * size
        self.x = col * size
        self.color = white
        self.size = size
        self.cost = 1
        
    def addPosCost(self):
        self.cost = randint(0, 40)
    
    def addNegPosCost(self):
        self.cost = randint(-6, 999)

    def display(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.size, self.size))
    

def drawSquare(win, node):
    node.display(win)
    pygame.draw.line(win, grey, (0, node.row * spacing), (size, node.row * spacing))
    pygame.draw.line(win, grey, (node.col * spacing, 0), (node.col * spacing, size))


def drawBoard(win, manager, board):
    win.fill(white)
    pygame.draw.rect(win, (142, 121, 121), (0, size, size, 100))
    for i in range(rows):
        board[i][0].color = black
        board[0][i].color = black
        board[rows - 1][i].color = black
        board[i][rows - 1].color = black
    
    for row in board:
        for node in row:
            node.display(win)
    
    for i in range(rows):
        pygame.draw.line(win, grey, (0, i * spacing), (size, i * spacing))
        pygame.draw.line(win, grey, (i * spacing, 0), (i * spacing, size))
        
    manager.draw_ui(win)
    pygame.display.update()


def clickedPos(pos):
    x, y = pos
    row, col = y // spacing, x // spacing
    return row, col
    


def main():
    pygame.init()
    win = pygame.display.set_mode((size, size + 100))
    pygame.display.set_caption("Shortest Path Finding Algorithms")

    manager = pygame_gui.UIManager((size, size + 100))
    clock = pygame.time.Clock()
    bfs_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(((5/80) * size, size + (1/32) * size), button_size), text = "BFS", manager=manager)
    dijkstra_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(((2/8) * size, size + (1/32) * size), button_size), text = "DIJKSTRA", manager=manager)
    bellman_ford_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(((35/80) * size, size + (1/32) * size), button_size), text = "BELLMAN-FORD", manager=manager)
    astar_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(((5/8) * size, size + (1/32) * size), button_size), text = "A*", manager=manager)
    reset_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(((65/80) * size, size + (1/32) * size), button_size), text = "RESET", manager=manager)

    board = [[Node(i, j, size // rows) for j in range(rows)] for i in range(rows)]
    startNode = None
    endNode = None
    running = True
    while running:
        time_delta = clock.tick(240)/1000.0
        drawBoard(win, manager, board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            manager.process_events(event)
            
            if pygame.mouse.get_pressed()[0]:
                row, col = clickedPos(pygame.mouse.get_pos())
                if 0 <= row < rows and 0 <= col < rows:
                    node = board[row][col]
                    if node.color != black:
                        if not startNode:
                            startNode = node
                            startNode.color = yellow
                        
                        elif not endNode and node != startNode:
                            endNode = node
                            endNode.color = purple

                        elif node != endNode and node != startNode:
                            node.color = black
            
            elif pygame.mouse.get_pressed()[2]:
                row, col = clickedPos(pygame.mouse.get_pos())
                if 0 <= row < rows and 0 <= col < rows:
                    node = board[row][col]
                    node.color = white
                    if node == startNode:
                        startNode = None
                    elif node == endNode:
                        endNode = None
            
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if startNode and endNode:
                        foundPath = None
                        if event.ui_element == bfs_button:
                            foundPath = bfs.BFS(lambda: drawBoard(win, manager, board), board, startNode, endNode)
                         
                        elif event.ui_element == dijkstra_button:
                            for i in range(rows):
                                for j in range(rows):
                                    board[i][j].addPosCost()
                            foundPath = dijkstra.dijkstra(lambda: drawBoard(win, manager, board), board, startNode, endNode)

                        elif event.ui_element == bellman_ford_button:
                            for i in range(rows):
                                for j in range(rows):
                                    board[i][j].addNegPosCost()
                            foundPath = bellman_ford.BellmanFord(lambda: drawBoard(win, manager, board), win, board, startNode, endNode)

                            if foundPath == False:
                                myFont = pygame.font.SysFont("Comic Sans MS", int((5/80) * size))
                                text = myFont.render("The negative cycle has occured!", True, green)
                                win.blit(text, (size // rows + (15/800) * size , size // 2))
                                pygame.display.update()
                                sleep(4)
                        
                        elif event.ui_element == astar_button:
                            foundPath = a_star.a_star(lambda: drawBoard(win, manager, board), board, startNode, endNode)

                        elif event.ui_element == reset_button:
                            startNode, endNode = None, None
                            board = [[Node(i, j, size // rows) for j in range(rows)] for i in range(rows)]

                        if not foundPath:
                            sleep(0.5)
                            startNode, endNode = None, None
                            board = [[Node(i, j, size // rows) for j in range(rows)] for i in range(rows)]
        
        manager.update(time_delta)
    pygame.quit()



if __name__ == "__main__":
    main()