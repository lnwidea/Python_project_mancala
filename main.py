import pygame, sys
from pygame.locals import *
from constants import *


pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mancala')


font = pygame.font.SysFont('comicsans', 40)


# To display
def draw__lines():
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

def who_turn(p1):
    if p1:
        turn = font.render('Player 1 turn', 1, red)
        win.blit(turn, (300, 250))
    elif not p1:
        turn = font.render('Player 2 turn', 1, red)
        win.blit(turn, (300, 250))
    

def score_value(bin_amout, x, p1):
    giveawayPile = bin_amout[x]
    bin_amout[x] = 0
    givepile(giveawayPile, x, bin_amout, p1)

def givepile(giveawayPile, x, bin_amout, p1):
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


def main():
    run = True
    bin_amout = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
    p1 = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN :
                if p1 and event.key == K_a:
                    x = 0
                    score_value(bin_amout, x, p1)
                elif p1 and event.key == K_b:
                    x = 1
                    score_value(bin_amout, x, p1)
                elif p1 and event.key == K_c:
                    x = 2
                    score_value(bin_amout, x, p1)
                elif p1 and event.key == K_d:
                    x = 3
                    score_value(bin_amout, x, p1)
                elif p1 and event.key == K_e:
                    x = 4
                    score_value(bin_amout, x, p1)
                elif p1 and event.key == K_f:
                    x = 5
                    score_value(bin_amout, x, p1)
                elif not p1 and event.key == K_a:
                    x = 12
                    score_value(bin_amout, x, p1)
                elif not p1 and event.key == K_b:
                    x = 11
                    score_value(bin_amout, x, p1)
                elif not p1 and event.key == K_c:
                    x = 10
                    score_value(bin_amout, x, p1)
                elif not p1 and event.key == K_d:
                    x = 9
                    score_value(bin_amout, x, p1)
                elif not p1 and event.key == K_e:
                    x = 8
                    score_value(bin_amout, x, p1)
                elif not p1 and event.key == K_f:
                    x = 7
                    score_value(bin_amout, x, p1)
                p1 = not p1
                
                    
                
        draw__lines()
        Pit(bin_amout)
        who_turn(p1)
        pygame.display.update()
        

    pygame.quit()

if __name__ == '__main__':
    main()
