# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()

    # load assets
    logoIMG = pygame.image.load("assets/logo.png")
    cannonIMG = pygame.image.load("assets/cannon.png")
    moonIMG = pygame.image.load("assets/moon.png")
    miceIMG = pygame.image.load("assets/mice.png")
    grassIMG = pygame.image.load("assets/grass.png")

    # set assets
    pygame.display.set_icon(logoIMG)
    pygame.display.set_caption("MoonShot")

    # set all the variables 
    clock = pygame.time.Clock()
    display_width = 800
    display_height = 600
    black = (0,0,0)
    white = (255,255,255)
    grey = (25,25,25)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    screen = pygame.display.set_mode((display_width,display_height))
    cannon_start_x = (display_width * 0.45)
    cannon_start_y = (display_height * 0.8)
    cannon_x = 0
    cannon_y = 0
    cannon_width = 60
    cannon_height = 100
    moon_start_x = (display_width * 0.9)
    moon_start_y = (display_height * 0.1)
    moon_x = 0
    moon_y = 0
    moon_width = 200
    moon_height = 200
    mice_start_x = (display_width * 0.45)
    mice_start_y = (display_height * 0.8)
    mice_x = 0
    mice_y = 0
    mice_width = 25
    mice_height = 100
    grass_start_x = (display_width * 0.45)
    grass_start_y = (display_height * 0.8)
    grass_x = 0
    grass_y = 0
    grass_width = 50
    grass_height = 100
     
    # define a variable to control the main loop
    running = True

    # define a function to control the player
    def cannon(cannon_start_x,cannon_start_y):
        screen.blit(cannonIMG, (cannon_start_x, cannon_start_y))

    # define a function to control the moon
    def moon(moon_start_x,moon_start_y):
        screen.blit(moonIMG, (moon_start_x, moon_start_y))
    
    # define a function to control the mice
    def mice(mice_start_x,mice_start_y):
        screen.blit(miceIMG, (mice_start_x, mice_start_y))
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            # add statements to change position on key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if cannon_start_x > 5:
                        cannon_x = -5
                    if cannon_start_x < 5:
                        break
                elif event.key == pygame.K_RIGHT:
                    if cannon_start_x < display_width - cannon_width:
                        cannon_x = 5
                    if cannon_start_x > display_width - cannon_width:
                        break
            # add statement to handle key up
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    cannon_x = 0
        # change asset locations
        cannon_start_x += cannon_x
        # set background colour
        screen.fill(grey)
        # display assets
        cannon(cannon_start_x, cannon_start_y)
        moon(moon_start_x, moon_start_y)
        # load new frames each tick
        pygame.display.update()
        # set the frame rate 
        clock.tick(15)
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()