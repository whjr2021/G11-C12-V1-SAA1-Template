# Import "pygame" modules 
import pygame

# Initialize "pygame"
pygame.init() 

# Create a game screen and set its title 
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Student Additional Activity 1")

# Game loop
carryOn = True
while carryOn:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            carryOn = False
    
    # Student Additional Activity 1: Display tree, hut and cloud images
    # Load the tree image


    
    # Load the hut image and scale it to dimension (300, 200) 



    
    # Load the cloud image and scale it to dimension (500, 150)





    # Display the tree image at (50, 300)

    # Display the hut image at (200, 250)

    # Display the cloud image at (50, 50)


    # Update the contents of the display
    pygame.display.flip()

# On the occurence of "pygame.QUIT" event close the game screen
pygame.quit()