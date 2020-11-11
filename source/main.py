# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()

    # load assets
    logoIMG = pygame.image.load("assets/logo.png")
    playerIMG = pygame.image.load("assets/player.png")
    moonIMG = pygame.image.load("assets/cheese.png")

    # set assets
    pygame.display.set_icon(logoIMG)
    pygame.display.set_caption("MoonShot")

    # set variables 
    clock = pygame.time.Clock()
    display_width = 800
    display_height = 600
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    screen = pygame.display.set_mode((display_width,display_height))
    player_start_x = (display_width * 0.45)
    player_start_y = (display_height * 0.8)
    player_x = 0
    player_y = 0
    moon_start_x = (display_width * 0.9)
    moon_start_y = (display_height * 0.1)
    moon_x = 0
    moon_y = 0
     
    # define a variable to control the main loop
    running = True

    # define a function to control the player
    def player(player_start_x,player_start_y):
        screen.blit(playerIMG, (player_start_x,player_start_y))

    # define a function to control the moon
    def moon(moon_start_x,moon_start_y):
        screen.blit(moonIMG, (moon_start_x,moon_start_y))
     
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
                    player_x = -5
                elif event.key == pygame.K_RIGHT:
                    player_x = 5
            # add statement to handle key up
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x = 0
        # change asset locations
        player_start_x += player_x
        # set background colour
        screen.fill(white)
        # display assets
        player(player_start_x, player_start_y)
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