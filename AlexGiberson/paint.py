import pygame, sys
from pygame.locals import *
import random
pygame.init()

width = 500
height = 500

DISPLAY=pygame.display.set_mode((width,height))
pygame.display.set_caption("paimt")

framerate = int(input("What is the game's framerate? "))
incr = int(input("Choose the movement increment: "))

WHITE=(255,255,255)
BLUE=(0,0,255)
RED=(255,0,0)
BLACK=(0,0,0)
PURPLE=(255,0,255)
GREEN=(0,255,0)

r=0
g=0
b=0
rchange=0
gchange=0
bchange=0

color = (r,g,b)
cnum = 0

x = width/2
y = height/2

xChange = 0
yChange = 0

colors = [BLUE, RED, BLACK, PURPLE, GREEN]

clock = pygame.time.Clock()

while True:
	clear = False
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit() 
		if event.type == pygame.KEYDOWN:
			#print(str(event.key))
			if event.key == pygame.K_LEFT and x!= 0:
				xChange = -incr
				print(str(x)+", "+str(y))
			if event.key == pygame.K_RIGHT and x!= 490:
				xChange = incr
				print(str(x)+", "+str(y))
			if event.key == pygame.K_UP and y!= 0:
				yChange = -incr
				print(str(x)+", "+str(y))
			if event.key == pygame.K_DOWN and y!=490:
				yChange = incr
				print(str(x)+", "+str(y))
			
			if event.key == pygame.K_q:
				rchange += 1
				print(r)
			if event.key == pygame.K_w:
				gchange += 1
				print(g)
			if event.key == pygame.K_e:
				bchange += 1
				print(b)
			if event.key == pygame.K_a:
				rchange -= 1
				print(r)
			if event.key == pygame.K_s:
				gchange -= 1
				print(g)
			if event.key == pygame.K_d:
				bchange -= 1
				print(b)
			if event.key == pygame.K_c:
				clear = True
	
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_q or event.key == pygame.K_a:
			rchange = 0
		elif event.key == pygame.K_w or event.key == pygame.K_s:
			gchange = 0
		elif event.key == pygame.K_e or event.key == pygame.K_d:
			bchange = 0

	if x >= width or x <= 0 or y >= height or y <= 0: 
		x = width/2
		y = height/2
	
	if r < 254:
		r += rchange
	else: 
		if r >= 254:
			r = 253
	if r > 1:
		r += rchange
	elif r <= 1:
		r = 2
	if g < 254:
		g += gchange
	else: 
		if g >= 254:
			g = 253
	if g > 1:
		g += gchange
	elif g <= 1:
		g = 2
	if b < 254:
		b += bchange
	else: 
		if b >= 254:
			b = 253
	if b > 1:
		b += bchange
	elif b <= 1:
		b = 2
	
	color = (r,g,b)
	x += xChange
	y += yChange			
	#DISPLAY.fill(WHITE)
	#try:
	try:
		pygame.draw.rect(DISPLAY,color,(x,y,10,10),0)
	
	except:
		print(r,g,b)
		if r >= 250:
			r = 255
		elif r <= 5:
			r = 0
		elif g >= 250:
			g = 255
		elif g <= 5:
			g = 0
		elif b >= 250:
			b = 255
		elif b <= 5:
			b = 0	
	
	if clear == True:
		DISPLAY.fill(BLACK)
	pygame.display.update()
	clock.tick(framerate)