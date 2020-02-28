import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Initialize game and creats a screen object(old)
    #Initialize pygame, settings, and screen_object.
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # Make a Ship
    ship = Ship(screen)

    #Set the background color RGB.
    bg_color = ( 0, 0, 115 )

    #Start the main loop for thself.rect.centerx = self.screen_rect.centerxe game.
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #Redraw the Screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #Make the mos recently drawn screen visible.
        pygame.display.flip()

run_game()
