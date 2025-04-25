import pygame as pg
from pygame.sprite import Sprite as SP

class Bullet(SP):
    ''' crete a bullet object at the ship's current position'''
    super(Bullet, self).__init__()
    self.screen=screen

    #cerate a bullet rect at (0,0) and then set corect position
    self.rect = pg.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet-height)
    self.rect.centerx=ship.rect.centerx
    self.rect.top=ship.rect.top

    # store the bullet's posiotion as a decimal value
    self.y = float(self.rect.y)

    self.color = ai_settings.bullet_color
    self.speed_factor = ai_settings.bullet_speed_factor
