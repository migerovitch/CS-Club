import pygame, sys 
from pygame.locals import *
import random
import time

width = 600 #This can change
height = 600 #This can change
playersize = 20 #This can change
fps = 15 #This can change
clock = pygame.time.Clock()

DISPLAY=pygame.display.set_mode((width,height))
pygame.display.set_caption("waka waka waka")

white = (255,255,255)
yellow = (255,255,0)
black = (0,0,0)
grey = (128,128,128)

pacX = 100
pacY = 50

yChange = 0
xChange = 0

restrictY = []
restrictX = []


for i in range(150,451):
	print(i)
	restrictY.append(i)
for i in range(150,451):
	print(i)
	restrictX.append(i)

gameExit = False

top = False
bottom = False
left = False
right = False

while gameExit == False:
	for event in pygame.event.get():
		if event.type == QUIT:
			gameExit = True
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


	if pacX > width or pacX < 0 or pacY > height or pacY < 0: 
		if pacX > width: pacX = 0
		if pacX < 0: pacX = width - playersize
		if pacY > height: pacY = 0
		if pacY < 0: pacY = height - playersize

	if pacX in restrictX and pacY in restrictY:
		gameExit = True
	
	pacX += xChange
	pacY += yChange			
	DISPLAY.fill(white)
	pygame.draw.rect(DISPLAY,yellow,[pacX,pacY,playersize,playersize])
	pygame.draw.rect(DISPLAY,grey,[150,150,300,300])
	pygame.display.update()
	clock.tick(fps)

pygame.quit()
sys.exit()
