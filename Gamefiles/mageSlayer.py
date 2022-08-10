import pygame
import pygame_menu
pygame.init()

windowSize = (600,800)
darkTheme = pygame_menu.themes.THEME_DARK
SURFACE = pygame.display.set_mode(windowSize)

def createCharacter(stats=[]):
    pass

def startGame():
    pass


menu = pygame_menu.Menu("Mage slayer",600,300,theme=darkTheme)

menu.add.text_input("Character name: ", default="Chabquest")
menu.add.selector('Class :', [('Fighter', 1), ('Mage', 2)], onchange=createCharacter)
menu.add.button('Play', startGame)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(SURFACE)
