import pygame, random, sys, thorpy, time
from pygame.locals import *
from Charactergui import *
from Charactercreationgui import *
from Combatgui import *
from Enemygui import *
from Itemsgui import *
from settings import *
from sprites import *
from Stuffgui import *






def terminate():
    pygame.quit()
    sys.exit()

def drawscreen(surface, color, font, chars, charlist):

    if len(charlist) == 1:
        char1 = charlist[0][1]
    if len(charlist) == 2:
        char2 = charlist[1][1]
    if len(charlist) == 3:
        char3 = charlist[2][1]
    if len(charlist) == 4:
        char4 = charlist[3][1]



    for row in range(3):
        pygame.draw.line(surface, color, (0, row*200), (600, row*200), 4)

    for column in range(2):
        pygame.draw.line(surface, color, (2+column*300, 0), (2+column*300, 400), 4)

    if len(charlist) == 1:
        drawtext('Name: ' + str(char1.name), font, surface, 10, 2)
        drawtext('Attack Bonus: ' + str(char1.attackbonus), font, surface, 10, 22)
        drawtext('Damage Bonus: ' + str(char1.damagebonus), font, surface, 10, 42)
        drawtext('4', font, surface, 10, 62)
        drawtext('5', font, surface, 10, 82)
        drawtext('6', font, surface, 10, 102)
        drawtext('7', font, surface, 10, 122)
        drawtext('8', font, surface, 10, 142)
        drawtext('9', font, surface, 10, 162)
        drawtext('10', font, surface, 10, 182)
    if len(charlist) == 2:
        drawtext('Name: ' + str(char2.name), font, surface, 10, 202)
        drawtext('Attack Bonus: ' + str(char2.attackbonus), font, surface, 10, 222)
        drawtext('Damage Bonus: ' + str(char2.damagebonus), font, surface, 10, 242)
        drawtext('14', font, surface, 10, 262)
        drawtext('15', font, surface, 10, 282)
        drawtext('16', font, surface, 10, 302)
        drawtext('17', font, surface, 10, 322)
        drawtext('18', font, surface, 10, 342)
        drawtext('19', font, surface, 10, 362)
        drawtext('20', font, surface, 10, 382)
    if len(charlist) == 3:
        drawtext('Name: ' + str(char3.name), font, surface, 310, 2)
        drawtext('Attack Bonus: ' + str(char3.attackbonus), font, surface, 310, 22)
        drawtext('Damage Bonus:' + str(char3.damagebonus), font, surface, 310, 42)
        drawtext('4', font, surface, 310, 62)
        drawtext('5', font, surface, 310, 82)
        drawtext('6', font, surface, 310, 102)
        drawtext('7', font, surface, 310, 122)
        drawtext('8', font, surface, 310, 142)
        drawtext('9', font, surface, 310, 162)
        drawtext('10', font, surface, 310, 182)
    if len(charlist) == 4:
        drawtext('Name: ' + str(char4.name), font, surface, 310, 202)
        drawtext('Attack Bonus: ' + str(char4.attackbonus), font, surface, 310, 222)
        drawtext('Damage Bonus: ' + str(char4.damagebonus), font, surface, 310, 242)
        drawtext('14', font, surface, 310, 262)
        drawtext('15', font, surface, 310, 282)
        drawtext('16', font, surface, 310, 302)
        drawtext('17', font, surface, 310, 322)
        drawtext('18', font, surface, 310, 342)
        drawtext('19', font, surface, 310, 362)
        drawtext('20', font, surface, 310, 382)

def drawbattlefield(surface, color):

    for row in range(7):
        pygame.draw.line(surface, color, (600, row*100), (1200, row*100), 4)

    for column in range(7):
        pygame.draw.line(surface, color, (600+column*100, 0), (600+column*100, 600), 4)

    filledsquaresleft = pygame.Rect(600, 300, 100, 300)
    filledsquaresright = pygame.Rect(1100, 300, 100, 300)

    pygame.draw.rect(surface, color, filledsquaresleft)
    pygame.draw.rect(surface, color, filledsquaresright)

def drawtext(text, font, surface, x, y):
    textobject = font.render(text, 1, TEXTCOLOR)
    textrect = textobject.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobject, textrect)

def drawcharacters(chars, charlist, surface, image, squares, textlist, font):

    order1 = squares[19]
    order2 = squares[20]
    order3 = squares[18]
    order4 = squares[21]
    order5 = squares[23]
    order6 = squares[24]
    order7 = squares[22]
    order8 = squares[25]
    order9 = squares[27]
    order10 = squares[28]
    order11 = squares[26]
    order12 = squares[29]
    orderlist = [order1, order2, order3, order4, order5, order6, order7, order8, order9, order10, order11, order12]

    textorder1 = textlist[19]
    textorder2 = textlist[20]
    textorder3 = textlist[18]
    textorder4 = textlist[21]
    textorder5 = textlist[23]
    textorder6 = textlist[24]
    textorder7 = textlist[22]
    textorder8 = textlist[25]
    textorder9 = textlist[27]
    textorder10 = textlist[28]
    textorder11 = textlist[26]
    textorder12 = textlist[29]
    textorderlist = [textorder1, textorder2, textorder3, textorder4, textorder5, textorder6, textorder7, textorder8, textorder9,
     textorder10, textorder11, textorder12]

    index = 0
    for char in charlist:
        surface.blit(image, orderlist[index])
        drawtext('HP: ' + str(char[1].hp) + '/' + str(char[1].hpmax), font, surface, textorderlist[index][0],
                 textorderlist[index][1])
        index += 1

def drawencounter(encounter, encounterlist, surface, image, squares, textlist, font):

    order1 = squares[14]
    order2 = squares[15]
    order3 = squares[13]
    order4 = squares[16]
    order5 = squares[12]
    order6 = squares[17]
    order7 = squares[8]
    order8 = squares[9]
    order9 = squares[7]
    order10 = squares[10]
    order11 = squares[6]
    order12 = squares[11]
    order13 = squares[2]
    order14 = squares[3]
    order15 = squares[1]
    order16 = squares[4]
    order17 = squares[0]
    order18 = squares[5]
    orderlist = [order1, order2, order3, order4, order5, order6, order7, order8, order9, order10, order11, order12, order13, order14, order15, order16, order17, order18]

    textorder1 = textlist[14]
    textorder2 = textlist[15]
    textorder3 = textlist[13]
    textorder4 = textlist[16]
    textorder5 = textlist[12]
    textorder6 = textlist[17]
    textorder7 = textlist[8]
    textorder8 = textlist[9]
    textorder9 = textlist[7]
    textorder10 = textlist[10]
    textorder11 = textlist[6]
    textorder12 = textlist[11]
    textorder13 = textlist[2]
    textorder14 = textlist[3]
    textorder15 = textlist[1]
    textorder16 = textlist[4]
    textorder17 = textlist[0]
    textorder18 = textlist[5]
    textorderlist = [textorder1, textorder2, textorder3, textorder4, textorder5, textorder6, textorder7, textorder8, textorder9, textorder10, textorder11, textorder12,
                 textorder13, textorder14, textorder15, textorder16, textorder17, textorder18]

    index = 0
    for enemy in encounterlist:
        surface.blit(image, orderlist[index])
        drawtext('HP: ' + str(enemy[1].hp) + '/' + str(enemy[1].hp), font, surface, textorderlist[index][0], textorderlist[index][1])
        index += 1

def waitforkeypress():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return



def main():

    pygame.init()
    main_clock = pygame.time.Clock()
    windowsurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('RPG')
    pygame.mouse.set_visible(True)

    font1 = pygame.font.SysFont(None, 48)
    font2 = pygame.font.SysFont(None, 24)
    font3 = pygame.font.SysFont(None, 32)
    pc = Character('Pooper', 20, 10, 5, 5, 20, 5, 20, 15)
    chars = {'Pooper': pc}
    charlist = [('Pooper', pc)]
    charnamelist = []
    for char in charlist:
        charnamelist.append(char[0])

    pooperimage = pygame.image.load('Pooper.png')
    pooperimage = pygame.transform.scale(pooperimage, (100, 70))

    piblinimage = pygame.image.load('piblin.png')
    piblinimage = pygame.transform.scale(piblinimage, (100, 70))
    piblinrect = piblinimage.get_rect()

    square1 = (600, 0)
    square2 = (700, 0)
    square3 = (800, 0)
    square4 = (900, 0)
    square5 = (1000, 0)
    square6 = (1100, 0)
    square7 = (600, 100)
    square8 = (700, 100)
    square9 = (800, 100)
    square10 = (900, 100)
    square11 = (1000, 100)
    square12 = (1100, 100)
    square13 = (600, 200)
    square14 = (700, 200)
    square15 = (800, 200)
    square16 = (900, 200)
    square17 = (1000, 200)
    square18 = (1100, 200)
    square19 = (700, 300)
    square20 = (800, 300)
    square21 = (900, 300)
    square22 = (1000, 300)
    square23 = (700, 400)
    square24 = (800, 400)
    square25 = (900, 400)
    square26 = (1000, 400)
    square27 = (700, 500)
    square28 = (800, 500)
    square29 = (900, 500)
    square30 = (1000, 500)

    text1 = (600, 70)
    text2 = (700, 70)
    text3 = (800, 70)
    text4 = (900, 70)
    text5 = (1000, 70)
    text6 = (1100, 70)
    text7 = (600, 170)
    text8 = (700, 170)
    text9 = (800, 170)
    text10 = (900, 170)
    text11 = (1000, 170)
    text12 = (1100, 170)
    text13 = (600, 270)
    text14 = (700, 270)
    text15 = (800, 270)
    text16 = (900, 270)
    text17 = (1000, 270)
    text18 = (1100, 270)
    text19 = (700, 370)
    text20 = (800, 370)
    text21 = (900, 370)
    text22 = (1000, 370)
    text23 = (700, 470)
    text24 = (800, 470)
    text25 = (900, 470)
    text26 = (1000, 470)
    text27 = (700, 570)
    text28 = (800, 570)
    text29 = (900, 570)
    text30 = (1000, 570)
    textlist = [(605, 75), (705, 75), (805, 75), (905, 75), (1005, 75), (1105, 75), (605, 175), (705, 175), (805, 175), (905, 175), (1005, 175), (1105, 175), (605, 275), (705, 275), (805, 275), (905, 275), (1005, 275), (1105, 275), (705, 375), (805, 375), (905, 375), (1005, 375), (705, 475), (805, 475), (905, 475), (1005, 475), (705, 575), (805, 575), (905, 575), (1005, 575)]

    squarelist = [(600, 0), (700, 0), (800, 0), (900, 0), (1000, 0), (1100, 0), (600, 100), (700, 100), (800, 100), (900, 100), (1000, 100), (1100, 100), (600, 200), (700, 200), (800, 200), (900, 200), (1000, 200), (1100, 200), (700, 300), (800, 300), (900, 300), (1000, 300), (700, 400), (800, 400), (900, 400), (1000, 400), (700, 500), (800, 500), (900, 500), (1000, 500)]
    square19 = (700, 300)
    square20 = (800, 300)
    square21 = (900, 300)
    square22 = (1000, 300)
    square23 = (700, 400)
    square24 = (800, 400)
    square25 = (900, 400)
    square26 = (1000, 400)
    square27 = (700, 500)
    square28 = (800, 500)
    square29 = (900, 500)
    square30 = (1000, 500)

    event = False

    windowsurface.fill(BACKGROUNDCOLOR)
    #draw_text('RPG', font, window_surface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    papersurface = pygame.image.load('paper background.png')
    papersurface = pygame.transform.scale(papersurface, (1202, 685))
    paperrect = papersurface.get_rect()


    pygame.display.update()





    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_1:
                    if len(chars) <= 4:
                        char = charactercreation(windowsurface, papersurface)
                        if char != None:
                            chars.update({char.name: char})
                            charlist.append((char.name, char))
                if event.key == K_2:
                    deletecharacters(chars, charlist)
                if event.key == K_3:
                    viewcharacters(charlist)
                if event.key == K_4:
                    pass
                if event.key == K_5:
                    pass
                if event.key == K_6:
                    encounter, encounterlist = generateencounter()
                    combat(chars, charlist, encounter, encounterlist)
                if event.key == K_7:
                    terminate()
           # menu.react(event)


        windowsurface.fill(BACKGROUNDCOLOR)





        windowsurface.blit(papersurface, paperrect)
        drawscreen(windowsurface, LINECOLOR, font2, chars, charlist)
        drawbattlefield(windowsurface, LINECOLOR)
        drawtext('1. Create Characters', font3, windowsurface, 2, 420)
        drawtext('2. Delete Characters', font3, windowsurface, 2, 450)
        drawtext('3. View Characters', font3, windowsurface, 2, 480)
        drawtext('4. Journey to Location', font3, windowsurface, 2, 510)
        drawtext('5. Visit the Market', font3, windowsurface, 2, 540)
        drawtext('6. Generate Custom Encounter', font3, windowsurface, 2, 570)
        drawtext('7. Quit', font3, windowsurface, 2, 600)
        drawtext(str(chars.keys()), font3, windowsurface, 2, 630)
        drawtext('9', font3, windowsurface, 2, 660)
        # papersurface.blit(piblinimage, square1)
        # papersurface.blit(piblinimage, square2)
        # papersurface.blit(piblinimage, square3)
        # papersurface.blit(piblinimage, square4)
        # papersurface.blit(piblinimage, square5)
        # papersurface.blit(piblinimage, square6)
        # papersurface.blit(piblinimage, square7)
        # papersurface.blit(piblinimage, square8)
        # papersurface.blit(piblinimage, square9)
        # papersurface.blit(piblinimage, square10)
        # papersurface.blit(piblinimage, square11)
        # papersurface.blit(piblinimage, square12)
        # papersurface.blit(piblinimage, square13)
        # papersurface.blit(piblinimage, square14)
        # papersurface.blit(piblinimage, square15)
        # papersurface.blit(piblinimage, square16)
        # papersurface.blit(piblinimage, square17)
        # papersurface.blit(piblinimage, square18)
        # papersurface.blit(piblinimage, square19)
        # papersurface.blit(piblinimage, square20)
        # papersurface.blit(piblinimage, square21)
        # papersurface.blit(piblinimage, square22)
        # papersurface.blit(piblinimage, square23)
        # papersurface.blit(piblinimage, square24)
        # papersurface.blit(piblinimage, square25)
        # papersurface.blit(piblinimage, square26)
        # papersurface.blit(piblinimage, square27)
        # papersurface.blit(piblinimage, square28)
        # papersurface.blit(piblinimage, square29)
        # papersurface.blit(piblinimage, square30)

        encounter, encounterlist = generateencounter('Piblin', 5)
        drawencounter(encounter, encounterlist, papersurface, piblinimage, squarelist, textlist, font2)
        drawcharacters(chars, charlist, papersurface, pooperimage, squarelist, textlist, font2)
        drawtext(str(encounterlist[0][1].hp), font3, windowsurface, 600, 625)
        pygame.display.update()

        # declaration of some ThorPy elements ...
        slider = thorpy.SliderX.make(100, (12, 35), "My Slider")
        button = thorpy.make_button("Quit", func=thorpy.functions.quit_func)
        box = thorpy.Box.make(elements=[slider, button])
        # we regroup all elements on a menu, even if we do not launch the menu
        menu = thorpy.Menu(box)
        # important : set the screen as surface for all elements
        for element in menu.get_population():
            element.surface = windowsurface
        # use the elements normally...
        box.set_topleft((100, 100))
        box.blit()
        box.update()
        main_clock.tick(FPS)


if __name__ == '__main__':
    main()


