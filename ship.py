import pygame

class Ship():
    """Initialize the ship and set it's starting position."""
    def __init__(self,screen):
        self.screen = screen

        # Load th ship image and get its rect.
        self.image = pygame.image.load(images/ship.bmp)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_bottom

def blitme(self):
    """Draw the ship at its current location."""
    self.screen.blit(self.image, self.rect)
