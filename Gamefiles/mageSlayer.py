import pygame
import pygame_menu
pygame.init()

windowSize = (600,800)
darkTheme = pygame_menu.themes.THEME_DARK
SURFACE = pygame.display.set_mode(windowSize)

def createCharacter(charClass,name):
    print(charClass[0],name)
    if charClass[0] == "Fighter":
        pass
    elif charClass[0] == "Mage":
        pass
    else:
        print(f"Expected char option got {charClass}")

def updateTextWidget(ID):
    pass

def startGame():
    pass

def startMenu():
    menu = pygame_menu.Menu("Mage slayer",600,300,theme=darkTheme)
    textInput = menu.add.text_input("Character name: ", default="Chabquest",textinput_id="Name")
    selector = menu.add.selector('Class :', [('Fighter'), ('Mage')])
    menu.add.button('Play', createCharacter(selector.get_value(),textInput.get_value()))
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(SURFACE)


if __name__ == "__main__":
    startMenu()



    
