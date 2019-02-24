import pygame as pg
import sys, thorpy
from os import path
from settings import *
from sprites import *
from tilemap import *
from menus import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        img_folder = path.join(game_folder, 'img')
        map_folder = path.join(game_folder, 'maps')
        self.map = TiledMap(path.join(map_folder, 'testmap.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.player_img = pg.transform.scale(self.player_img, (TILESIZE, TILESIZE))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player = Player(self, 64, 64)
        self.camera = Camera(self.map.width, self.map.height)


    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)



    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))


    def draw(self):

        self.draw_grid()
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        #self.screen.blit(self.player.image, self.camera.apply(self.player))

        self.draw_text('fuck', FONT1, 100, 100)
        self.draw_text(str(self.walls.sprites), FONT1, 100, 120)
        self.draw_text(str(self.player), FONT1, 100, 140)
        pg.display.flip()

    def draw_text(self, text, font, x, y):

        textobject = font.render(text, 1, WHITE)
        textrect = textobject.get_rect()
        textrect.topleft = (x, y)
        self.screen.blit(textobject, textrect)

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move_player(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move_player(dx=1)
                if event.key == pg.K_UP:
                    self.player.move_player(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move_player(dy=1)
                if event.key == pg.K_q:
                    draw_main_menu(self.screen)
            #self.button_menu.react(event)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

if __name__ == "__main__":

    # create the game object
    g = Game()
    g.show_start_screen()
    while True:
        g.new()
        g.run()
        g.show_go_screen()