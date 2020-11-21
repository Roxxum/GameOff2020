# import needed modules
import pygame
import math
 
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
    screen = pygame.display.set_mode((display_width,display_height))
    grey = (25,25,25)
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
    moon_change_height = 0
    moon_change_width = 0
    miceList = []
    mice_width = 50
    mice_height = 60
     
    # define a variable to control the main loop
    running = True

    # define functions to control the assets
    def cannon(cannon_current_x, cannon_current_y):
        screen.blit(cannonIMG, (cannon_current_x, cannon_current_y))

    def moon(moon_current_x, moon_current_y):
        screen.blit(pygame.transform.scale(moonIMG, (moon_width, moon_height)), (moon_current_x, moon_current_y))
    
    def mice(mice_current_x, mice_current_y):
        screen.blit(miceIMG, (mice_current_x, mice_current_y))

    def grass(grass_current_x, grass_current_y):
        screen.blit(grassIMG, (grass_current_x, grass_current_y))

    def collision(moon_current_x, moon_current_y, mice_current_x, mice_current_y):    
        distance = math.sqrt((math.pow(moon_current_x - mice_current_x, 2)) + (math.pow(moon_current_y - mice_current_y, 2)))
        if distance < (moon_height / 2) and mice_current_y > 0:
            return True

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
                    mouse = {}
                    mouse["mice_current_x"] = (cannon_current_x + ((cannon_width - mice_width) / 2))
                    mouse["mice_current_y"] = (cannon_current_y + ((cannon_height - mice_height) / 2))
                    mouse["mice_change_x"] = 0
                    mouse["mice_change_y"] = 0
                    miceList.append(mouse)

        # add statements to change position of moon
        if moon_current_x < display_width:
            moon_change_x = 5
        if moon_current_x > display_width:
            moon_change_x = 0
            moon_current_x = (0 - moon_width)

        # add statements to change position of mice
        badMice = []
        for mouseIndex in range(len(miceList)):
            mouse = miceList[mouseIndex]
            if mouse["mice_current_y"] > (0 - mice_height):
                mouse["mice_change_y"] = -5
            if mouse["mice_current_y"] <= (0 - mice_height):
                badMice.append(mouseIndex)

            # check to see if collision occured and reset assets if true
            collisioncheck = collision(moon_current_x, moon_current_y, mouse["mice_current_x"], mouse["mice_current_y"])
            if collisioncheck:
                badMice.append(mouseIndex)
                moon_change_width = -10
                moon_change_height = -10
            
            mouse["mice_current_y"] += mouse["mice_change_y"]

        # add statement to remove mice that are off the screen
        for mouse in range(len(badMice)):
            miceList.remove(miceList[badMice[mouse]])

        # change asset variables
        cannon_current_x += cannon_change_x
        moon_current_x += moon_change_x
        moon_height += moon_change_height
        moon_width += moon_change_width
        moon_change_height = 0
        moon_change_width = 0

        # draw assets
        screen.fill(grey)
        grass(grass_current_x, grass_current_y)
        for mouseIndex in range(len(miceList)):
            mouse = miceList[mouseIndex]
            mice(mouse["mice_current_x"], mouse["mice_current_y"])
        cannon(cannon_current_x, cannon_current_y)
        moon(moon_current_x, moon_current_y)
        
        # load new frames each tick
        pygame.display.update()
        
        # set the frame rate 
        clock.tick(30)

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()