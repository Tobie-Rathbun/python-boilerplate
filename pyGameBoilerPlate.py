#import libraries
import pygame
import random


#define screen properties
width, height = 600, 280
fps = 30


#define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


#initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
# app_icon = pygame.image.load('img/laserRed10.png')
# pygame.display.set_icon(app_icon)

#initialize a font
basicFont = pygame.font.SysFont(None, 48)

#Set up the text
text = basicFont.render('The Adventures of Python', True, white)
textRect = text.get_rect()
textRect.centerx = screen.get_rect().centerx
textRect.centery = screen.get_rect().centery



#game loop
running = True
	#set running to false to end game
while running:
	#keep loop running at right speed
	clock.tick(fps)
	#process input
	for event in pygame.event.get():
		#check for closing window
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			match event.key:
				case pygame.K_ESCAPE:
					running = False
				case pygame.K_a:
					print("a")
	"""
	#other method of handling input
	#loses some key presses though
	#also returns a long list of Boolean states
	keystate = pygame.key.get_pressed()
	if keystate[pygame.K_ESCAPE]:		
		running = False
	elif keystate[pygame.K_a]:
		a = 1
	#explains what I mean
	keystate = pygame.key.get_pressed()
	print(keystate)
	"""
	
		
	#update
	#draw render
	screen.fill(black)
	screen.blit(text,textRect)
		#draws the text onto the surface
	#after drawing, flips the display
	pygame.display.flip()


pygame.quit()
