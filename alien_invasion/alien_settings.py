class Settings:
    # a class to store all settings for Alien Invasion

    def __init__(self):
        # Initialize the game's settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 25, 40)

        #ship settings
        self.ship_speed = 1.5

        #Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3.0
        self.bullet_height = 15
        self.bullet_color = (200, 0, 175)
        self.bullets_allowed = 6

        #Alien settings
        self.alien_speed = 1.0
        
