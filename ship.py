import pygame as pg

class Ship():
    def __init__(self, screen, ai_settings):

        '''initialize the ship and set its starting position'''
        self.screen=screen
        self.ai_settings = ai_settings

        #load the ship image and get its rect.
        self.image = pg.image.load('img/picture.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each  new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal valye for the ship's center
        self.center = float(self.rect.centerx)

        #movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        '''update ship's position based on movement flag'''
        #update the ship's center value,. not the rect
        if self.moving_right and self.moving_left < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.moving_right > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect object from self.center
        self.rect.centerx = self.center


    def blitme(self):
        '''draw the ship at its curent location'''
        self.screen.blit(self.image, self.rect)