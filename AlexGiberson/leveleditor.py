import pygame, sys
from pygame.locals import *
import csv

width = 600
height = 600

fps = 15
clock = pygame.time.Clock()

screen = pygame.display.set_mode((width,height))

exit = False
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

value = 'barrier'
x = 0
y = 0
xy = []
accept = False



edit = input("Type level name to edit. To create new, leave blank: ")

if edit != '':
	levelname = edit
	csvfile =open(edit +".csv",'r')
	obj=csv.reader(csvfile)
	for row in obj:
		xy.append((row))
	print(xy)
elif edit == '':
	levelname = input("Enter level name (omit file tag): ")

while not accept:  
	try:
		rectwidth = int(input("Enter rect width: "))
		rectheight = int(input("Enter rect height: "))
		accept = True

	except:
		print("Invalid!")

accept = False

while exit == False:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit = True
	if event.type == pygame.KEYDOWN:
		#print(str(event.key))
		if event.key == pygame.K_LEFT:
			x += -20
			#print(str(x)+", "+str(y))
		elif event.key == pygame.K_RIGHT:
			x += 20
			#print(str(x)+", "+str(y))
		elif event.key == pygame.K_UP:
			y += -20
			#print(str(x)+", "+str(y))
		elif event.key == pygame.K_DOWN:
			y += 20
		if event.key == pygame.K_c:
			if (value,x,y,rectwidth,rectheight) not in xy:
				xy.append((value,x,y,rectwidth,rectheight))
				print("Block saved to list")
		if event.key == pygame.K_r:
			while not accept:
				try:
					print("Resize block: ")
					rectwidth = int(input("Enter rect width: "))
					rectheight = int(input("Enter rect height: "))
					accept = True
				except:	
					print("Invalid!")
			accept = False
		if event.key == pygame.K_z:
			if len(xy) > 1:
				print(str(xy.pop(-1))+" was removed from list")
		if event.key == pygame.K_g:
			if value == 'barrier':
				value = 'food'
			elif value == 'food':
				value = 'barrier'
			print(value)
		if event.key == pygame.K_o:
			rectwidth = rectwidth + rectheight
			rectheight = rectwidth - rectheight
			rectwidth = rectwidth - rectheight
		if event.key == pygame.K_f:
			print("Saving..")
			csvfile = open(levelname + ".csv","w", newline='')
			file_writer = csv.writer(csvfile)
			for tup in xy:
				file_writer.writerow(tup)
			csvfile.close()
			xy.insert(0,spawn)
			print("Saved!")
			exit = True
	#if event.type == pygame.KEYUP:


	screen.fill(black)		
	for coord in xy:

		pygame.draw.rect(screen,blue,[float(coord[1]),float(coord[2]),float(coord[3]),float(coord[4])])
	if value == 'barrier':
		pygame.draw.rect(screen,blue,[x,y,rectwidth,rectheight])
	elif value == 'food':
		pygame.draw.rect(screen,white,[x,y,rectwidth,rectheight])
	pygame.display.update()
	clock.tick(fps)
pygame.quit()
sys.exit()