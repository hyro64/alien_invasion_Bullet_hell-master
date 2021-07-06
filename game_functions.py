import sys

import pygame

import ship


def check_keydown_events(event, ship):
    for event in pygame.event.get():
        if event.type == pygame.K_RIGHT:
            ship.rect.center -= 1


def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right.
                ship.rect.centerx += 1


def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # make the most recently drawn screen visible.
    pygame.display.flip()
