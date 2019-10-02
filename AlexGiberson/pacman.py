import pygame, sys 
from pygame.locals import *
import random
import time

width = 600 #This can change
height = 600 #This can change
playersize = 20 #This can change
fps = 15 #This can change
clock = pygame.time.Clock()

#Create display
DISPLAY=pygame.display.set_mode((width,height))
pygame.display.set_caption("waka waka waka")

#define colors with rgb values
white = (255,255,255)
yellow = (255,255,0)
black = (0,0,0)
grey = (128,128,128)
darkBlue = (0,20,121)

#starting coords of player
pacX = 100
pacY = 50

yChange = 0
xChange = 0

#list of off-limits coords
restrictY = []
restrictX = []

#if true then no entry
touching = False



#adds restricted coords to x and y lists for hardcoded block
for i in range(140,441):
	print(i)
	restrictY.append(i)
for i in range(140,441):
	print(i)
	restrictX.append(i)

#if true then system exit
gameExit = False

#main game loop
while gameExit == False:
	for event in pygame.event.get():
		if event.type == QUIT:
			gameExit = True
		#Gets keypresses and moves the player accordingly
		if event.type == pygame.KEYDOWN:
			#print(str(event.key))
			if event.key == pygame.K_LEFT:
				xChange = -playersize/2
				yChange = 0
				#print(str(x)+", "+str(y))
			elif event.key == pygame.K_RIGHT:
				xChange = playersize/2
				yChange = 0
				#print(str(x)+", "+str(y))
			elif event.key == pygame.K_UP:
				yChange = -playersize/2
				xChange = 0
				#print(str(x)+", "+str(y))
			elif event.key == pygame.K_DOWN:
				yChange = playersize/2
				xChange = 0

		#Make player stop moving after keyup
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or pygame.K_RIGHT:
				xChange = 0
			if event.key == pygame.K_UP or pygame.K_DOWN:
				yChange = 0

	#if player goes out of bounds then move them to the other side of the screen
	if pacX > width or pacX < 0 or pacY > height or pacY < 0: 
		if pacX > width: pacX = 0
		if pacX < 0: pacX = width - playersize
		if pacY > height: pacY = 0
		if pacY < 0: pacY = height - playersize

	#is it touching a boundary?
	if pacX + xChange in restrictX and pacY + yChange in restrictY:
		touching = True
	else:
		touching = False
	
	#if not touching a boundary then allow move
	if not touching:
		pacX += xChange
		pacY += yChange
	elif touching == True:
		print("Sorry, that's out of bounds...")

	#draw everything on the display
	DISPLAY.fill(grey)
	pygame.draw.rect(DISPLAY,yellow,[pacX,pacY,playersize,playersize])
	pygame.draw.rect(DISPLAY,darkBlue,[150,150,300,300])
	pygame.display.update()
	clock.tick(fps)

pygame.quit()
sys.exit()
