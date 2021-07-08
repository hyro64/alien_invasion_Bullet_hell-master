import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        """Initialize the ship and sit it's starting position."""
        self.screen = screen

        # -> added from pg.253
        self.ai_setting = ai_settings
        # -> end

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # -> added from pg.253
        self.center = float(self.rect.centerx)
        # -> end

        # Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left >0:
            self.center -= self.ai_setting.ship_speed_factor

        # Update rect object from self.centerd
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
