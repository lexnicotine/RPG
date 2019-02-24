
import thorpy
from RPGmain import *


def draw_main_menu(screen):


        button1 = thorpy.make_button("Poop", test_butt)
        button2 = thorpy.make_button('Fuck', )
        button1.set_size((200, 200))

        box = thorpy.Box.make(elements=[button1, button2])
        # we regroup all elements on a menu, even if we do not launch the menu

        # important : set the screen as surface for all elements

        # use the elements normally...
        box.set_topleft((300, 300))
        box.blit()
        box.update()
        #unclick = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
         #                             reac_func=test_butt, event_args={"id":thorpy.constants.EVENT_UNPRESS})

        #background = thorpy.Background.make(color=(255, 255, 255), image='paper background.png',
        #                                  elements=[button1, button2])
        button_menu = thorpy.Menu(box)

        for element in button_menu.get_population():
            element.surface = screen

        #background.add_reaction(unclick) #add my_reaction to background's reaction



        selecting = True
        while selecting:


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                button_menu.react(event)
                if event.type == thorpy.constants.THORPY_EVENT:
                    if event.el == button1:
                        pass
                    if event.el == button2:
                        selecting = False




def test_butt():
    #draw_menu_text(screen, 'it worked', FONT1, 300, 400)
    print('Poop')

def fuck():
    selecting = False

    return selecting

def draw_menu_text(surface, text, font, x, y):
        textobject = font.render(text, 1, WHITE)
        textrect = textobject.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobject, textrect)

