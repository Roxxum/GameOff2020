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
    grass_width = 800
    grass_height = 20
    grass_current_x = (display_width - grass_width)
    grass_current_y = (display_height - grass_height)
    cannon_width = 60
    cannon_height = 100
    cannon_current_x = (display_width * 0.45)
    cannon_current_y = (display_height - (cannon_height + (grass_height / 2)))
    cannon_change_x = 0
    cannon_change_y = 0
    moon_width = 200
    moon_height = 200
    moon_current_x = (moon_width * 0.0)
    moon_current_y = (moon_height * 0.0)
    moon_change_x = 0
    moon_change_y = 0
    mice_width = 50
    mice_height = 60
    mice_current_x = (0 - mice_width)
    mice_current_y = (0 - mice_height)
    mice_change_x = 0
    mice_change_y = 0
     
    # define a variable to control the main loop
    running = True

    # define functions to control the assets
    def cannon(cannon_current_x,cannon_current_y):
        screen.blit(cannonIMG, (cannon_current_x, cannon_current_y))

    def moon(moon_current_x,moon_current_y):
        screen.blit(moonIMG, (moon_current_x, moon_current_y))
    
    def mice(mice_current_x,mice_current_y):
        screen.blit(miceIMG, (mice_current_x, mice_current_y))

    def grass(grass_current_x,grass_current_y):
        screen.blit(grassIMG, (grass_current_x, grass_current_y))
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            # add statements to move cannon with key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if cannon_current_x > 5:
                        cannon_change_x = -5
                    if cannon_current_x < 5:
                        break
                elif event.key == pygame.K_RIGHT:
                    if cannon_current_x < (display_width - cannon_width):
                        cannon_change_x = 5
                    if cannon_current_x > (display_width - cannon_width):
                        break
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    cannon_change_x = 0

            # add statements to shoot mice
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if mice_current_y <= (0 - mice_height):
                        mice_current_y = (cannon_current_y + ((cannon_height - mice_height) / 2))
                        mice_current_x = (cannon_current_x + ((cannon_width - mice_width) / 2))
                    if mice_current_y > 5:
                        break

        # add statements to change position of moon
        if moon_current_x < display_width:
            moon_change_x = 5
        if moon_current_x > display_width:
            moon_change_x = 0
            moon_current_x = (0 - moon_width)

        # add statements to change position of mice
        if mice_current_y > (0 - mice_height):
            mice_change_y = -5
        if mice_current_y <= (0 - mice_height):
            mice_change_y = 0

        # change asset locations
        cannon_current_x += cannon_change_x
        mice_current_y += mice_change_y
        moon_current_x += moon_change_x
        # set background colour
        screen.fill(grey)
        # display assets
        grass(grass_current_x, grass_current_y)
        mice(mice_current_x, mice_current_y)
        cannon(cannon_current_x, cannon_current_y)
        moon(moon_current_x, moon_current_y)
        # load new frames each tick
        pygame.display.update()
        # set the frame rate 
        clock.tick(15)
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()