import pygame
import random
import os
pygame.font.init()


width, height = 520, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dice Simulator")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
FPS = 60
SMALL_FONT = pygame.font.SysFont('comicsans', 30)
win.fill(RED)


# passing two parametes dice which includes coodinates of dice on the screen
def draw_window(dice, index):
    Dice_Image = pygame.image.load(os.path.join(
        'images', 'd{}.png'.format(index)))  # including image using os
    # Rendering the text so that we can add it on the screen
    text_for_Space = SMALL_FONT.render('Press Space Bar', True, WHITE)
    text_for_OR = SMALL_FONT.render('OR', True, WHITE)
    text_for_Click = SMALL_FONT.render('Click on dice to Roll', True, WHITE)
    win.fill(RED)  # Filling the background color
    win.blit(text_for_Space, (175, 10))  # Placing the text on the screen
    win.blit(text_for_OR, (235, 35))
    win.blit(text_for_Click, (165, 60))
    win.blit(pygame.transform.scale(Dice_Image, (200, 200)),
             (dice.x, dice.y))  # Adding the image of the dice
    pygame.display.update()  # now finally updating the screen


def main():
    dice = pygame.Rect(160, 150, 200, 200)# creating a rectangle in which we have to place the image 
    n = 1 #creating a integer variable to keep track of the random image have to display on the screen 
    clock = pygame.time.Clock()#Pygame clock initiated 
    run = True # to run infinite loop
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():# reading event from the screen to keep track if ther any command is given to roll the dice 
            if event.type == pygame.QUIT:#Execute when we close the game window
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:#Execute when any keyboad key pressed
                if event.key == pygame.K_SPACE:
                    n = random.randrange(1, 7)#generating random number 
                    draw_window(dice, n)#calling draw window function 
            if event.type == pygame.MOUSEBUTTONDOWN:#To keep track of any mouse button pressed
                mouse_pos = event.pos
                if dice.collidepoint(mouse_pos):#It became true when dice rectangle coordinates are same of the mouse pointer 
                    n = random.randrange(1, 7)
                    draw_window(dice, n)
        draw_window(dice, n)
    main()


if __name__ == "__main__":
    main()
