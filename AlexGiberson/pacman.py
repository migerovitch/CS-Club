import pygame, sys 
from pygame.locals import *
import random
import csv

width = 600 #This can change
height = 600 #This can change
playersize = 20 #This can change
fps = 15 #This can change
clock = pygame.time.Clock()

#Create dis
DISPLAY=pygame.display.set_mode((width,height))
pygame.display.set_caption("waka waka waka")

#define colors with rgb values
white = (255,255,255)
yellow = (255,255,0)
black = (0,0,0)
grey = (128,128,128)
darkBlue = (0,20,121)

#starting coords of player
pacX = 0
pacY = 0

yChange = 0
xChange = 0

xy = []
rx = []
ry = []
restrictedxy = []

levelname = (input("Levelname (omit file tage):"))

#if true then no entry
touching = False

#if true then system exit
gameExit = False

csvfile =open(levelname +".csv",'r')
obj=csv.reader(csvfile)
for row in obj:
	xy.append((row))

def buildlevel(xy,screen,color):
	for coord in xy:
		pygame.draw.rect(screen,color,[float(coord[0]),float(coord[1]),float(coord[2]),float(coord[3])])


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
		"""
		#Make player stop moving after keyup
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or pygame.K_RIGHT:
				xChange = 0
			if event.key == pygame.K_UP or pygame.K_DOWN:
				yChange = 0
		"""
	#if player goes out of bounds then move them to the other side of the screen
	if pacX > width or pacX < 0 or pacY > height or pacY < 0: 
		if pacX > width: pacX = 0
		if pacX < 0: pacX = width - playersize
		if pacY > height: pacY = 0
		if pacY < 0: pacY = height - playersize

	#is the movement selected going to intersect with a boundary?
	"""
	if pacX in rx and pacY in ry:
		touching = True
	else:
		touching = False
	"""
	

	
	#if not touching a boundary then allow move
	
	if not touching:
		pacX += xChange
		pacY += yChange
	elif touching == True:
		print("Sorry, that's out of bounds...")
	
	#draw everything on the display
	DISPLAY.fill(grey)
	pygame.draw.rect(DISPLAY,yellow,[pacX,pacY,playersize,playersize])
	buildlevel(xy,DISPLAY,darkBlue)
	pygame.display.update()
	clock.tick(fps)

pygame.quit()
sys.exit()
