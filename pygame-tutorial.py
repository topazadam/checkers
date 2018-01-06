# Pygame introduction
import pygame

# define some colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

#First initialise pygame module
pygame.init()

# create surface
# must pass a tuple to "set_mode" to set the size of the window
# **Coord (0,0) is in the top left of the window**
gameDisplay = pygame.display.set_mode( (800,600) )

# set title
pygame.display.set_caption('My game')

 # takes params of area to update othersise updates entire window
pygame.display.update()

 # ==========================================================
 # game logic goes here

# flag to keep the game running - set True to exit during the game
gameExit = False

# Variables for moving objects
lead_x = 300
lead_y = 300

# Main loop - continues until "gameExit" set to True
while not gameExit:
	# For all events in the game - event handling loop
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
			gameExit = True
		# Other event types go here...
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				# to go left this is minus on the x axis
				lead_x -= 10
			if event.key == pygame.K_RIGHT:
				# to go right this is plus on the x axis
				lead_x += 10
			if event.key == pygame.K_UP:
				# to go up this is minus on the y axis (up the screen)
				lead_y -= 10
			if event.key == pygame.K_DOWN:
				# to go down this is plus on the y axis (down the screen)
				lead_y += 10

	# Other loops go here...
	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay, red, [lead_x,lead_y,50,50])

	# Draw a rectangle
	# Args:
	#	- where? - game surface
	#	- colour?
	#	- list specifiying the rectangle []:
	#		- start x, start y, width, height
	#pygame.draw.rect(gameDisplay, red, [400,300,50,50])


	# Once all items have been drawn...
	pygame.display.update()


# Exit method - unitilise pygame
pygame.quit()

# Trigger exit
quit()