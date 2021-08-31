import pygame


def create_text(text, size):
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    return font.render(text, True, (255, 255, 255))


def new_surface(width, height, color):
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    surface.fill(color)
    return surface
