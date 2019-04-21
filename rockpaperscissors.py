import random
import pygame
from time import sleep
# a must evry time  u use pygame
pygame.init()
#window size
win = pygame.display.set_mode((700, 700))
pygame.display.set_caption('Rock Paper Scissors')
run = True
win.fill((0,0,0))
font = pygame.font.SysFont('Schriftbild', 100)
inputed = False
wins = 3
while run:
    #---------------------------------------
    pygame.time.delay(90)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              run = False
    #---------------------------------------
    #___________________________________________
    #RESOURCE(VARIABLES EG.)
    blue = 0,255,0
    #___________________________________________
    #----------------------------------------------------------------------
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------
    #DRAWING TABLE
    text1 = font.render('Computer', False, (255, 255, 255))
    text2 = font.render('Player', False, (255, 255, 255))
    Wintxt = font.render('Player Wins', False, (0, 255, 0))
    Tietxt = font.render('Tie', False, (0, 0, 255))
    Losetxt = font.render('Player Loses', False, (255, 0, 0))
    option = 4
    comoption = 0

    pygame.draw.line(win, (255, 255, 255), (0, 90), (700, 90), 10)

    pygame.draw.line(win, (255, 255, 255), (0, 550), (700, 550), 10)

    pygame.draw.line(win, (255, 255, 255), (233, 550), (233, 700), 10)

    pygame.draw.line(win, (255, 255, 255), (466, 550), (466, 700), 10)
    pygame.display.update()
    if wins == 1:
        pygame.draw.line(win, (255, 255, 255), (0, 90), (700, 90), 10)

        pygame.draw.line(win, (255, 255, 255), (0, 550), (700, 550), 10)

        pygame.draw.line(win, (255, 255, 255), (233, 550), (233, 700), 10)

        pygame.draw.line(win, (255, 255, 255), (466, 550), (466, 700), 10)
        pygame.display.update()
        sleep(1)
        win.blit(Wintxt, (150, 100))
        pygame.display.update()
        sleep(3)
        inputed = False
        wins = 3
        win.fill((0, 0, 0))
    if wins == 2:
        pygame.draw.line(win, (255, 255, 255), (0, 90), (700, 90), 10)

        pygame.draw.line(win, (255, 255, 255), (0, 550), (700, 550), 10)

        pygame.draw.line(win, (255, 255, 255), (233, 550), (233, 700), 10)

        pygame.draw.line(win, (255, 255, 255), (466, 550), (466, 700), 10)
        pygame.display.update()
        sleep(1)
        win.blit(Tietxt, (300, 100))
        pygame.display.update()
        sleep(3)
        inputed = False
        wins = 3
        win.fill((0, 0, 0))
    if wins == 0:
        pygame.draw.line(win, (255, 255, 255), (0, 90), (700, 90), 10)

        pygame.draw.line(win, (255, 255, 255), (0, 550), (700, 550), 10)

        pygame.draw.line(win, (255, 255, 255), (233, 550), (233, 700), 10)

        pygame.draw.line(win, (255, 255, 255), (466, 550), (466, 700), 10)
        pygame.display.update()
        sleep(1)
        win.blit(Losetxt, (150, 100))
        pygame.display.update()
        sleep(3)
        inputed = False
        wins = 3
        win.fill((0, 0, 0))


    win.blit(text1, (5, 10))
    win.blit(text2, (410, 10))


    #LOADING IMAGES--------------------------------------------------------------------
    win.blit(pygame.transform.scale(pygame.image.load('images\Paper.png'),(150, 150)), (30, 550))
    win.blit(pygame.transform.scale(pygame.image.load('images\Rock.png'), (150, 150)), (280, 550))
    win.blit(pygame.transform.scale(pygame.image.load('images\Scissors.png'), (150, 150)), (500 , 550))

    pygame.display.update()
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------


    #---------------------------------------------------------
    #GETTING MOUSE POS
    mx, my = pygame.mouse.get_pos()
    #----------------------------------------------------------
    #MOUSE OVER
    # SCISSORS
    if mx > 472 and my > 550 and mx < 700 and my < 700 and inputed == False:
        pygame.draw.line(win, blue, (472, 560), (700, 560), 10)
        pygame.draw.line(win, blue, (472, 695), (700, 695), 10)

        pygame.draw.line(win, blue, (476, 560), (476, 700), 10)
        pygame.draw.line(win, blue, (694, 560), (694, 700), 10)
    #ROCK
    elif mx > 242 and my > 550 and mx < 466 and my < 700 and inputed == False:
        pygame.draw.line(win, blue, (242, 560), (460, 560), 10)
        pygame.draw.line(win, blue, (242, 695), (460, 695), 10)

        pygame.draw.line(win, blue, (243, 557), (243, 700), 10)
        pygame.draw.line(win, blue, (456, 557), (456, 700), 10)
    #PAPER
    elif mx > 0 and my > 550 and mx < 233 and my < 700 and inputed == False:
        pygame.draw.line(win, blue, (0, 560), (228, 560), 10)
        pygame.draw.line(win, blue, (0, 695), (228, 695), 10)

        pygame.draw.line(win, blue, (3, 560), (3, 700), 10)
        pygame.draw.line(win, blue, (223, 560), (223, 700), 10)

    #CLEAR MOUSE OVER
    elif inputed == False:
        blue = 0,0,0

        pygame.draw.line(win, blue, (0, 560), (228, 560), 10)
        pygame.draw.line(win, blue, (0, 695), (228, 695), 10)

        pygame.draw.line(win, blue, (3, 560), (3, 700), 10)
        pygame.draw.line(win, blue, (223, 560), (223, 700), 10)

        pygame.draw.line(win, blue, (242, 560), (460, 560), 10)
        pygame.draw.line(win, blue, (242, 695), (460, 695), 10)

        pygame.draw.line(win, blue, (243, 557), (243, 700), 10)
        pygame.draw.line(win, blue, (456, 557), (456, 700), 10)

        pygame.draw.line(win, blue, (472, 560), (700, 560), 10)
        pygame.draw.line(win, blue, (472, 695), (700, 695), 10)

        pygame.draw.line(win, blue, (476, 560), (476, 700), 10)
        pygame.draw.line(win, blue, (694, 560), (694, 700), 10)
    #NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
    #ACTUAL
    #DETECT WHERE THE USER CLICKED AND DISABLE THE USER FROM CHOOSING ANOTHER OPTION
    # #AND BREAKING THE GAME AND DELETING WRONG MOUSE OVERS
    if mx > 472 and my > 550 and mx < 700 and my < 700 and str(pygame.mouse.get_pressed()) == '(1, 0, 0)' and inputed == False:
        inputed = True
        option = 1
        pygame.draw.line(win, blue, (472, 560), (700, 560), 10)
        pygame.draw.line(win, blue, (472, 695), (700, 695), 10)

        pygame.draw.line(win, blue, (476, 560), (476, 700), 10)
        pygame.draw.line(win, blue, (694, 550), (694, 700), 10)
        blue = 0, 0, 0

        pygame.draw.line(win, blue, (0, 560), (233, 560), 10)
        pygame.draw.line(win, blue, (0, 695), (233, 695), 10)

        pygame.draw.line(win, blue, (3, 560), (3, 700), 10)
        pygame.draw.line(win, blue, (223, 550), (223, 700), 10)

        pygame.draw.line(win, blue, (242, 560), (466, 560), 10)
        pygame.draw.line(win, blue, (242, 695), (466, 695), 10)

        pygame.draw.line(win, blue, (243, 560), (243, 700), 10)
        pygame.draw.line(win, blue, (456, 550), (456, 700), 10)
        comoption = random.randint(1, 3)

    elif mx > 242 and my > 550 and mx < 466 and my < 700 and str(pygame.mouse.get_pressed()) == '(1, 0, 0)' and inputed == False:
        inputed = True
        option = 2
        pygame.draw.line(win, blue, (242, 560), (466, 560), 10)
        pygame.draw.line(win, blue, (242, 695), (466, 695), 10)

        pygame.draw.line(win, blue, (243, 550), (243, 700), 10)
        pygame.draw.line(win, blue, (456, 550), (456, 700), 10)

        blue = 0, 0, 0
        pygame.draw.line(win, blue, (472, 560), (700, 560), 10)
        pygame.draw.line(win, blue, (472, 695), (700, 695), 10)

        pygame.draw.line(win, blue, (476, 550), (476, 700), 10)
        pygame.draw.line(win, blue, (694, 550), (694, 700), 10)
        pygame.draw.line(win, blue, (0, 560), (233, 560), 10)
        pygame.draw.line(win, blue, (0, 695), (233, 695), 10)

        pygame.draw.line(win, blue, (3, 550), (3, 700), 10)
        pygame.draw.line(win, blue, (223, 550), (223, 700), 10)
        comoption = random.randint(1, 3)
    elif mx > 0 and my > 550 and mx < 233 and my < 700 and str(pygame.mouse.get_pressed()) == '(1, 0, 0)' and inputed == False:
        inputed = True
        option = 3
        pygame.draw.line(win, blue, (0, 560), (233, 560), 10)
        pygame.draw.line(win, blue, (0, 695), (233, 695), 10)

        pygame.draw.line(win, blue, (3, 550), (3, 700), 10)
        pygame.draw.line(win, blue, (223, 550), (223, 700), 10)

        blue = 0, 0, 0
        pygame.draw.line(win, blue, (242, 560), (466, 560), 10)
        pygame.draw.line(win, blue, (242, 695), (466, 695), 10)

        pygame.draw.line(win, blue, (243, 550), (243, 700), 10)
        pygame.draw.line(win, blue, (456, 550), (456, 700), 10)

        pygame.draw.line(win, blue, (472, 560), (700, 560), 10)
        pygame.draw.line(win, blue, (472, 695), (700, 695), 10)

        pygame.draw.line(win, blue, (476, 550), (476, 700), 10)
        pygame.draw.line(win, blue, (694, 550), (694, 700), 10)
        comoption = random.randint(1, 3)
    ####################################################################################################################################
    ###GRAPHIC
    ####################################################################################################################################
    #USER
    if option == 0:
        pass
    elif option == 1:
        win.blit(pygame.transform.scale(pygame.image.load('images\Scissors.png'), (400, 400)), (300, 100))
    elif option == 2:
        win.blit(pygame.transform.scale(pygame.image.load('images\Rock.png'), (400, 400)), (300, 100))
    elif option == 3:
        win.blit(pygame.transform.scale(pygame.image.load('images\Paper.png'), (400, 400)), (300, 100))
    #COMPUTER
    #CHOICe



    if comoption == 1:
        win.blit(pygame.transform.scale(pygame.image.load('images\Scissors.png'), (400, 400)), (0, 100))

    elif comoption == 2:

        win.blit(pygame.transform.scale(pygame.image.load('images\Rock.png'), (400, 400)), (0, 100))

    elif comoption == 3:
        win.blit(pygame.transform.scale(pygame.image.load('images\Paper.png'), (400, 400)), (0, 100))


    if comoption == option:
        #Tie
        print('Tie')
        wins = 2

    #1 = scissors      2 = rock      3 = paper
    elif comoption == 1 and option == 2:
        wins = 1
        print('Player Wins')
    elif comoption == 2 and option == 3:
        print('Player Wins')
        wins = 1
    elif comoption == 3 and option == 1:
        print('Player Wins')
        wins = 1


    elif comoption == 3 and option == 2:
        print('Player Loses')
        wins = 0
    elif comoption == 2 and option == 1:
        print('Player Loses')
        wins = 0
    elif comoption == 1 and option == 3:
        wins = 0
    pygame.display.update()



