class Settings():
    '''a class to store all the settings for alien invasion'''

    def __init__(self):
        '''initialize the game's settings'''
        #screen settings

        self.screen_width=800
        self.screen_height=800
        self.bg_color=(94, 104, 109)

        # ship settings

        self.ship_speed_factor = 1.5

        #bullet settings

        self.bullet_speed_factor=1
        self.bullet_width = 3
        self.bullet_height=15
        self.bullet_color = 60, 60, 60