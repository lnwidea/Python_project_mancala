import pygame
import os
from pygame.locals import *
from pygame import mixer
from constants import *
import copy
import time

pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mancala')
bg = pygame.image.load(os.path.join('image', 'bg.png'))
p1 = True
error = False
gameover = False
intro = True
p2 = True
a2 = False
turn = int(1)
mixer.music.load('Like A Dino!.wav')
mixer.music.play(-1)


font = pygame.font.SysFont('comicsans', 40)
anotherfont = pygame.font.SysFont('comicsans', 20)
errorfont = pygame.font.SysFont('comicsans', 30)

def game_intro():
    global p1
    global gameover
    global intro
    global p2
    global error
    global a2
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
            if event.type == pygame.KEYDOWN :
                if event.key == K_1:
                    p1 = True
                    p2 = False
                    gameover = False
                    error = False
                    intro = False
                    a2 = False
                    main()
                if event.key == K_2:
                    p1 = True
                    p2 = True
                    gameover = False
                    error = False
                    intro = False
                    a2 = False
                    main()
                if event.key == K_3:
                    p1 = True
                    a2 = True
                    gameover = False
                    error = False
                    intro = False
                    main()
        
        win.fill(white)
        welcome = font.render('Welcome to Mancala game', 1, black)
        oneplay = font.render('If 1 player, press 1', 1, black)
        twoplay = font.render('If 2 players, press 2', 1, black)
        aiplay = font.render('AI vs AI, press 3', 1, black)
        win.blit(bg, (0,0))
        win.blit(welcome, (210, 110))
        win.blit(oneplay, (270, 200))
        win.blit(twoplay, (270, 290))
        win.blit(aiplay, (270, 380))
        pygame.display.update()
    pygame.quit()


# To display
def draw__lines():
    global p2 
    global a2
    win.fill(white)
    pygame.draw.line(win, red, (0,165), (900,165), 5)
    pygame.draw.line(win, red, (0,333), (900,333), 5)
    pygame.draw.line(win, red, (112,0), (112,900), 5)
    pygame.draw.line(win, red, (224,0), (224,165), 5)
    pygame.draw.line(win, red, (224,333), (224,500), 5)
    pygame.draw.line(win, red, (336,0), (336,165), 5)
    pygame.draw.line(win, red, (336,333), (336,500), 5)
    pygame.draw.line(win, red, (448,0), (448,165), 5)
    pygame.draw.line(win, red, (448,333), (448,500), 5)
    pygame.draw.line(win, red, (560,0), (560,165), 5)
    pygame.draw.line(win, red, (560,333), (560,500), 5)
    pygame.draw.line(win, red, (672,0), (672,165), 5)
    pygame.draw.line(win, red, (672,333), (672,500), 5)
    pygame.draw.line(win, red, (784,0), (784,900), 5)
    p1_house = anotherfont.render('P1 house', 1, red)
    p2_house = anotherfont.render('P2 house', 1, red)
    AI_house = anotherfont.render('AI house', 1, red)
    a1_house = anotherfont.render('A1 house', 1, red)
    a2_house = anotherfont.render('A2 house', 1, red)
    back_to_menu = anotherfont.render('M = menu', 1, red)
    if p2 == True and not a2:
        win.blit(p1_house, (810, 190))
        win.blit(p2_house, (20, 190))
    elif not a2:
        win.blit(AI_house, (20, 190))
    else:
        win.blit(a1_house, (810, 190))
        win.blit(a2_house, (20, 190))
    win.blit(back_to_menu, (10, 40))
    
    

def Pit(bin_amout):
    zero = font.render(str(bin_amout[0]), 1, red)
    one = font.render(str(bin_amout[1]), 1, red)
    two = font.render(str(bin_amout[2]), 1, red)
    three = font.render(str(bin_amout[3]), 1, red)
    four = font.render(str(bin_amout[4]), 1, red)
    five = font.render(str(bin_amout[5]), 1, red)
    six = font.render(str(bin_amout[6]), 1, red)
    seven = font.render(str(bin_amout[7]), 1, red)
    eight = font.render(str(bin_amout[8]), 1, red)
    nine = font.render(str(bin_amout[9]), 1, red)
    ten = font.render(str(bin_amout[10]), 1, red)
    eleven = font.render(str(bin_amout[11]), 1, red)
    twelve = font.render(str(bin_amout[12]), 1, red)
    thirten = font.render(str(bin_amout[13]), 1, red)
    win.blit(zero, (160, 400))
    win.blit(one, (270, 400))
    win.blit(two, (380, 400))
    win.blit(three, (490, 400))
    win.blit(four, (600, 400))
    win.blit(five, (710, 400))
    win.blit(six, (825, 220))
    win.blit(seven, (710, 50))
    win.blit(eight, (600, 50))
    win.blit(nine, (490, 50))
    win.blit(ten, (380, 50))
    win.blit(eleven, (270, 50))
    win.blit(twelve, (160, 50))
    win.blit(thirten, (50, 220))

def who_turn(bin_amout):
    global p1
    global error
    global gameover
    if p1 and error == True:
        turn = errorfont.render('You must choose a non-empty bin, Player One.', 1, red)
        a = font.render('a', True, red)
        b = font.render('b', True, red)
        c = font.render('c', True, red)
        d = font.render('d', True, red)
        e = font.render('e', True, red)
        f = font.render('f', True, red)
        win.blit(a, (160, 250))
        win.blit(b, (270, 250))
        win.blit(c, (380, 250))
        win.blit(d, (490, 250))
        win.blit(e, (600, 250))
        win.blit(f, (710, 250))
        win.blit(turn, (140, 180))
        return
    elif not p1 and error == True and p2:
        turn = errorfont.render('You must choose a non-empty bin, Player Two.', 1, red)
        a = font.render('a', True, red)
        b = font.render('b', True, red)
        c = font.render('c', True, red)
        d = font.render('d', True, red)
        e = font.render('e', True, red)
        f = font.render('f', True, red)
        win.blit(a, (160, 165))
        win.blit(b, (270, 165))
        win.blit(c, (380, 165))
        win.blit(d, (490, 165))
        win.blit(e, (600, 165))
        win.blit(f, (710, 165))
        win.blit(turn, (140, 250))
        return
    
    sideone = 0
    sidetwo = 0
    for j in range(6):
        sideone = int(sideone) + int(bin_amout[j])
        sidetwo = int(sidetwo) + int(bin_amout[j+7])

    if int(sideone) == 0 or int(sidetwo) == 0:
        bin_amout[6] = int(bin_amout[6]) + int(sideone)
        bin_amout[13] = int(bin_amout[13]) + int(sidetwo)
        for k in range(6):
            bin_amout[k] = 0
            bin_amout[k+7] = 0
        who_won(bin_amout)
        return
    else:
        if p1 and not a2:
            turn = font.render('Player 1 turn', 1, red)
            a = font.render('a', True, red)
            b = font.render('b', True, red)
            c = font.render('c', True, red)
            d = font.render('d', True, red)
            e = font.render('e', True, red)
            f = font.render('f', True, red)
            win.blit(a, (160, 250))
            win.blit(b, (270, 250))
            win.blit(c, (380, 250))
            win.blit(d, (490, 250))
            win.blit(e, (600, 250))
            win.blit(f, (710, 250))
            win.blit(turn, (300, 165))
        elif not p1 and p2 and not a2:
            turn = font.render('Player 2 turn', 1, red)
            a = font.render('a', True, red)
            b = font.render('b', True, red)
            c = font.render('c', True, red)
            d = font.render('d', True, red)
            e = font.render('e', True, red)
            f = font.render('f', True, red)
            win.blit(a, (160, 165))
            win.blit(b, (270, 165))
            win.blit(c, (380, 165))
            win.blit(d, (490, 165))
            win.blit(e, (600, 165))
            win.blit(f, (710, 165))
            win.blit(turn, (300, 250))
        elif not p1 and not p2 and not a2:
            turn = font.render('AI is thinking', 1, red)
            a = font.render('a', True, red)
            b = font.render('b', True, red)
            c = font.render('c', True, red)
            d = font.render('d', True, red)
            e = font.render('e', True, red)
            f = font.render('f', True, red)
            win.blit(a, (160, 250))
            win.blit(b, (270, 250))
            win.blit(c, (380, 250))
            win.blit(d, (490, 250))
            win.blit(e, (600, 250))
            win.blit(f, (710, 250))
            win.blit(turn, (300, 165))
        elif p1 and a2:
            turn = font.render('A1 is thinking', 1, red)
            a = font.render('a', True, red)
            b = font.render('b', True, red)
            c = font.render('c', True, red)
            d = font.render('d', True, red)
            e = font.render('e', True, red)
            f = font.render('f', True, red)
            win.blit(a, (160, 250))
            win.blit(b, (270, 250))
            win.blit(c, (380, 250))
            win.blit(d, (490, 250))
            win.blit(e, (600, 250))
            win.blit(f, (710, 250))
            win.blit(turn, (300, 165))
        elif not p1 and a2:
            turn = font.render('A2 is thinking', 1, red)
            a = font.render('a', True, red)
            b = font.render('b', True, red)
            c = font.render('c', True, red)
            d = font.render('d', True, red)
            e = font.render('e', True, red)
            f = font.render('f', True, red)
            win.blit(a, (160, 165))
            win.blit(b, (270, 165))
            win.blit(c, (380, 165))
            win.blit(d, (490, 165))
            win.blit(e, (600, 165))
            win.blit(f, (710, 165))
            win.blit(turn, (300, 250))

def who_won(bin_amout):
    global gameover
    global p2
    global a2
    if int(bin_amout[13]) < int(bin_amout[6]):
        p1_vic = font.render('Player One victory', 1, red)
        p1_vic_AI = font.render('You win', 1, red)
        a1_vic = font.render('A1 victory', 1, red)
        winner = font.render('Press R to restart', 1, red)
        if p2 == True and not a2:
            win.blit(p1_vic, (270, 165))
        elif not a2:
            win.blit(p1_vic_AI, (300, 165))
        else:
            win.blit(a1_vic, (300, 165))
        win.blit(winner,(270, 250))
    elif int(bin_amout[13]) > int(bin_amout[6]):
        p2_vic = font.render('Player Two victory', 1, red)
        AI_vic = font.render('You lose', 1, red)
        a2_vic = font.render('A2 victory', 1, red)
        winner = font.render('Press R to restart', 1, red)
        if p2 == True and not a2:
            win.blit(p2_vic, (270, 165))
        elif not a2:
            win.blit(AI_vic, (300, 165))
        else:
            win.blit(a2_vic, (300, 165))
        win.blit(winner,(270, 250))
    else:
        Tie = font.render('Tie', 1, red)
        winner = font.render('Press R to restart', 1, red)
        win.blit(Tie,(400, 165))
        win.blit(winner,(270, 250))
    gameover = True

    

def score_value(bin_amout, x):
    global p1
    global error
    if bin_amout[x] == 0:
        error = True
        return
    error = False
    giveawayPile = bin_amout[x]
    bin_amout[x] = 0
    recipient = x + 1
    while (int(giveawayPile) > 0):
        if p1 and int(recipient) == 13:
            recipient = 0
        if not p1 and int(recipient) == 6:
            recipient = 7
        
        bin_amout[recipient] = int(bin_amout[recipient]) + 1
        giveawayPile = int(giveawayPile) -1

        if int(giveawayPile) == 0:
            lastrecipient = recipient
        else:
            recipient = int(recipient) + 1
            if int(recipient) > 13:
                recipient = 0
    if p1 and int(lastrecipient) == 6:
        p1 = True
    elif p1 and int(bin_amout[lastrecipient]) == 1 and int(lastrecipient) < 6 and int(bin_amout[12 - int(lastrecipient)]) != 0:
        bin_amout[6] = int(bin_amout[6]) + int(bin_amout[lastrecipient]) + int(bin_amout[12 - int(lastrecipient)])
        bin_amout[lastrecipient] = 0
        bin_amout[12 - int(lastrecipient)] = 0
        p1 = not(p1)
    elif not(p1) and int(lastrecipient) == 13:
        p1 = False
    elif not(p1) and int(bin_amout[lastrecipient]) == 1 and int(lastrecipient) > 6 and int(bin_amout[12 - int(lastrecipient)]) != 0:
        bin_amout[13] = int(bin_amout[13]) + int(bin_amout[lastrecipient]) + int(bin_amout[12 - int(lastrecipient)])
        bin_amout[lastrecipient] = 0
        bin_amout[12 - int(lastrecipient)] = 0
        p1 = not(p1)
    else:
        p1 = not(p1)




def minimax(bin_amout, alpha, beta, depth):
    global p1

    test = copy.deepcopy(bin_amout)
    action = 0

    if gameover == True or depth == 0:
        bestvalue = test[13] - test[6]
        return bestvalue
    
    if not p1 :
        bestvalue = - 10000
        for i in range (7, 13):
            test = copy.deepcopy(bin_amout)
            if test[i] == 0:
                continue
            score_value(test, i)
            alpha = max(alpha, minimax(test, alpha, beta, depth - 1))
            if alpha > bestvalue:
                bestvalue = alpha
                action = i
            if beta < alpha :
                break
        return action
    else:
        bestvalue = 10000
        for i in range (0, 6):
            test = copy.deepcopy(bin_amout)
            if test[i] == 0:
                continue
            score_value(test, i)
            beta = min(beta, minimax(test, alpha, beta, depth - 1))
            if bestvalue > beta:
                bestvalue = beta
            if beta < alpha :
                break
        return bestvalue

def minimax2(bin_amout, alpha, beta, depth):
    global p1

    test = copy.deepcopy(bin_amout)
    action = 0

    if gameover == True or depth == 0:
        bestvalue = test[13] - test[6]
        return bestvalue

    if p1 :
        bestvalue = - 10000
        for i in range (0, 6):
            test = copy.deepcopy(bin_amout)
            if test[i] == 0:
                continue
            score_value(test, i)
            alpha = max(alpha, minimax2(test, alpha, beta, depth - 1))
            if alpha > bestvalue:
                bestvalue = alpha
                action = i
            if beta < alpha :
                break
        return action
    else:
        bestvalue = 10000
        for i in range (7, 13):
            test = copy.deepcopy(bin_amout)
            if test[i] == 0:
                continue
            score_value(test, i)
            beta = min(beta, minimax2(test, alpha, beta, depth - 1))
            if bestvalue > beta:
                bestvalue = beta
            if beta < alpha :
                break
        return bestvalue

def main():
    global p1
    global gameover
    global intro
    global error
    global a2
    global turn
    run = True
    bin_amout = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
    while run:
        if turn != 1:
            if a2 and gameover == False:
                if not p1 :
                    x = minimax(bin_amout, -10000, 10000, 8)
                    x = int(x)
                    p1 = False
                    time.sleep(1)
                    score_value(bin_amout, x)
                elif p1:
                    x = minimax2(bin_amout, -10000, 10000, 5)
                    x = int(x)
                    p1 = True
                    time.sleep(1)
                    score_value(bin_amout, x)

        
        if not p1 and not p2 and not a2 and gameover == False:
            y = minimax(bin_amout, -10000, 10000, 8)
            y = int(y)
            p1 = False
            time.sleep(1)
            score_value(bin_amout, y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN and gameover == False :
                if p1 and event.key == K_a:
                    x = 0
                    score_value(bin_amout, x)
                elif p1 and event.key == K_b:
                    x = 1
                    score_value(bin_amout, x)
                elif p1 and event.key == K_c:
                    x = 2
                    score_value(bin_amout, x)
                elif p1 and event.key == K_d:
                    x = 3
                    score_value(bin_amout, x)
                elif p1 and event.key == K_e:
                    x = 4
                    score_value(bin_amout, x)
                elif p1 and event.key == K_f:
                    x = 5
                    score_value(bin_amout, x)
                elif not p1 and event.key == K_a and p2:
                    x = 12
                    score_value(bin_amout, x)
                elif not p1 and event.key == K_b and p2:
                    x = 11
                    score_value(bin_amout, x)
                elif not p1 and event.key == K_c and p2:
                    x = 10
                    score_value(bin_amout, x)
                elif not p1 and event.key == K_d and p2:
                    x = 9
                    score_value(bin_amout, x)
                elif not p1 and event.key == K_e and p2:
                    x = 8
                    score_value(bin_amout, x)
                elif not p1 and event.key == K_f and p2:
                    x = 7
                    score_value(bin_amout, x)
            
            if event.type == pygame.KEYDOWN:
                 if event.key == K_m:
                    intro = True
                    turn = 1
                    game_intro()
             
            if event.type == pygame.KEYDOWN and gameover == True :
                 if event.key == K_r:
                    p1 = True
                    gameover = False
                    error = False
                    turn = 1
                    main()

        draw__lines()
        Pit(bin_amout)
        who_turn(bin_amout)
        turn += 1
        pygame.display.update()
        

    pygame.quit()

if __name__ == '__main__':
    if intro == True:
        game_intro()
